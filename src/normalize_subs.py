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
