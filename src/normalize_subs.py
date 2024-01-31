import json
import pysubs2
import re

def normalize_subs(subs_file):
    subs = pysubs2.load(subs_file)
    for line in subs:
        line.text = re.sub(r'\\N', ' ', line.text)
        line.text = re.sub(r'{.*?}', '', line.text)
        line.text = re.sub(r'\[.*?\]', '', line.text)
        line.text = line.text.strip()

    # Filter out lines that don't have the "Default" style
    subs.events = [line for line in subs.events if line.style == 'Default']
    subs.remove_miscellaneous_events()
    subs.save("Temp_files/norm_subs.srt")

def json_to_srt(file_path):
    # Load JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Create a new Subs2 object
    subs = pysubs2.SSAFile()

    # Loop through each chunk in the JSON data
    for chunk in data['chunks']:
        start, end = chunk['timestamp']
        text = chunk['text']

        # Convert the timestamps to milliseconds
        start_ms = int(start * 1000)
        end_ms = int(end * 1000)

        # Create a new subtitle event
        event = pysubs2.SSAEvent(start=start_ms, end=end_ms, text=text)
        subs.append(event)

    # Save the subtitles as an SRT file
    subs.save("Input/output.srt", encoding="utf-8")


def is_complete_sentence(text):
    return re.search(r"(\.\.\.|[.!?])", text.strip()) is not None

def find_sentence_end(text):
    matches = list(re.finditer(r"(\.\.\.|[.!?])", text))
    if matches:
        return matches[-1].end()
    return -1

def is_time_difference_large(sub1, sub2, threshold=1000):
    return sub2.start - sub1.end > threshold

def split_sentences(text, start_time, end_time):
    sentence_end_positions = [m.end() for m in re.finditer(r"(\.\.\.|[.!?])", text)]
    sentences = []
    prev_end = 0
    for end_pos in sentence_end_positions:
        sentences.append((text[prev_end:end_pos].strip(), start_time, end_time))
        prev_end = end_pos
    return sentences

def process_subtitles(subs):

    for i in range(len(subs) - 1):
        if is_time_difference_large(subs[i], subs[i + 1]):
            continue

        current_text = subs[i].text.strip()
        next_text = subs[i + 1].text.strip()

        if is_complete_sentence(current_text):
            sentence_end_idx = find_sentence_end(current_text)
            remaining_text = current_text[sentence_end_idx:].strip()

            if remaining_text:
                proportion_remaining = len(remaining_text) / len(current_text)
                time_adjustment = int(proportion_remaining * (subs[i].end - subs[i].start))
                subs[i].end -= time_adjustment
                subs[i + 1].start -= time_adjustment

            subs[i + 1].text = remaining_text + " " + next_text if remaining_text else next_text
            subs[i].text = current_text[:sentence_end_idx]
        else:
            if is_complete_sentence(next_text):
                sentence_end_idx = find_sentence_end(next_text)
                subs[i].text += " " + next_text[:sentence_end_idx].strip()
                subs[i + 1].text = next_text[sentence_end_idx:].strip()

                proportion_added = sentence_end_idx / len(next_text)
                time_adjustment = int(proportion_added * (subs[i + 1].end - subs[i + 1].start))
                subs[i].end += time_adjustment
                subs[i + 1].start += time_adjustment

    # Handle multiple sentences in the last line
    last_line_text = subs[-1].text.strip()
    if is_complete_sentence(last_line_text):
        new_lines = split_sentences(last_line_text, subs[-1].start, subs[-1].end)
        subs.pop()  # Remove the original last line
        for sentence, start_time, end_time in new_lines:
            new_line = pysubs2.SSAEvent(start=start_time, end=end_time, text=sentence)
            subs.append(new_line)

    # Remove any empty lines and create a new SSAFile object
    filtered_subs = pysubs2.SSAFile()
    for sub in subs:
        if sub.text.strip():
            filtered_subs.append(sub)

    return filtered_subs

# subs = pysubs2.load('Temp_files/norm_subs_wwww2.srt')
# processed_subs = process_subtitles(subs)
# processed_subs.save('Temp_files/norm_subs_wwww3.srt')