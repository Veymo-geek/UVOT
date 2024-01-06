import pysubs2
import re

def normalize_subs(subs_file):
    subs = pysubs2.load(subs_file)
    for line in subs:
        line.text = re.sub(r'\\N', ' ', line.text)
        line.text = re.sub(r'{.*?}', '', line.text)
        line.text = re.sub(r'\[.*?\]', '', line.text)
        line.text = line.text.strip()
    subs.remove_miscellaneous_events()
    subs.save("Temp_files/norm_subs.srt")