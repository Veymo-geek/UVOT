from ukrainian_tts.tts import TTS, Voices, Stress
import IPython.display as ipd
from pydub import AudioSegment
from pydub import silence
import os
import re

tts = TTS(device="cpu") # can try gpu, mps
# subtitles_file = "Temp_files/ukr_orig.srt" #@param {type:"string"}


def synthesize_audio(text, output_filename):
    with open(output_filename, mode="wb") as file:
        _, _ = tts.tts(text, Voices.Dmytro.value, Stress.Dictionary.value, file)

def read_subtitles_file(subtitles_file):
    with open(subtitles_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return lines

def split_subtitles_into_phrases(subtitles_lines):
    phrases = []
    current_phrase = []
    for line in subtitles_lines:
        if line.strip().isdigit():
            if current_phrase:
                phrases.append(current_phrase)
                current_phrase = []
        else:
            current_phrase.append(line.strip())
    if current_phrase:
        phrases.append(current_phrase)
    return phrases

def combine_audio_files(phrases):
    output_folder = "audios"
    combined_audio = AudioSegment.empty()

    for idx, phrase in enumerate(phrases, 1):
        phrase_start_time = extract_time(phrase[0].strip().split(" --> ")[0])
        audio_filename = os.path.join(output_folder, f"{idx}.wav")
        audio_segment = AudioSegment.from_file(audio_filename, format="wav")
        silence_duration = phrase_start_time - len(combined_audio)
        if silence_duration > 0:
            silence_segment = AudioSegment.silent(duration=silence_duration)
            combined_audio += silence_segment
        combined_audio += audio_segment

    return combined_audio

def extract_time(time_string):
    hours, minutes, seconds, milliseconds = map(int, re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", time_string)[0])
    total_milliseconds = hours * 60 * 60 * 1000 + minutes * 60 * 1000 + seconds * 1000 + milliseconds
    return total_milliseconds

def generate_audio_fragments(subtitles_file):
    phrases = split_subtitles_into_phrases(read_subtitles_file(subtitles_file))

    output_folder = "audios"
    os.makedirs(output_folder, exist_ok=True)  # Create the "audios" folder if it doesn't exist

    for idx, phrase in enumerate(phrases, 1):
        phrase_text = " ".join(phrase[1:])
        audio_filename = os.path.join(output_folder, f"{idx}.wav")
        synthesize_audio(phrase_text, audio_filename)

def combine_audio_fragments(subtitles_file):
    phrases = split_subtitles_into_phrases(read_subtitles_file(subtitles_file))

    combined_audio = combine_audio_files(phrases)
    combined_audio.export("Temp_files/combined_audio.wav", format="wav")

# def main():
#     phrases = split_subtitles_into_phrases(read_subtitles_file(subtitles_file))

#     # output_folder = "audios"
#     # os.makedirs(output_folder, exist_ok=True)  # Create the "audios" folder if it doesn't exist

#     # for idx, phrase in enumerate(phrases, 1):
#     #     phrase_text = " ".join(phrase[1:])
#     #     audio_filename = os.path.join(output_folder, f"{idx}.wav")
#     #     synthesize_audio(phrase_text, audio_filename)

#     combined_audio = combine_audio_files(phrases)
#     combined_audio.export("Temp_files/combined_audio.wav", format="wav")

# if __name__ == "__main__":
#     main()