from src.split_audio import split_audio, convert_to_2_channels, split_6ch_audio
from src.normalize_subs import normalize_subs
from src.separate_video_audio_subs import separate_video_audio_subs
from src.tts import generate_audio_fragments, combine_audio_fragments, speed_up_audio_in_folder
from src.combine_all import combine_all, combine_6ch_audio, combine_2ch_audio, make_3ch
from src.adjust_audio_volume import adjust_audio_volume
from src.translate_text import translate_text
from src.delete_files import delete_temp_files
from src.find_files import find_file
from src.transcribe_audio import transcribe_audio
from src.youtube_download import download_youtube_video

from pydub import AudioSegment
import time
import os
import re

input_video = "Input/Video-noSubs.mkv"

start_time = time.time()
start_time_full = time.time()

if os.path.isfile(input_video) and input_video.endswith(('.mp4', '.mkv')):
    separate_video_audio_subs(input_video)
else:
    download_youtube_video(input_video)

if find_file("ENG_Subs") == None :
    transcribe_audio("splited_video/ENG_Audio.wav")

normalize_subs(find_file("ENG_Subs"))
translate_text("Temp_files/norm_subs.srt")

elapsed_time_1 = time.time() - start_time


# Check the number of audio channels
audio = AudioSegment.from_file("splited_video/ENG_Audio.wav")
num_channels = audio.channels
start_time = time.time()

if num_channels == 6:
    split_6ch_audio("splited_video/ENG_Audio.wav")
elif num_channels == 2:
    split_audio("splited_video/ENG_Audio.wav")
else:
    convert_to_2_channels("splited_video/ENG_Audio.wav", "splited_video/ENG_Audio_stereo.wav")
    split_audio("splited_video/ENG_Audio_stereo.wav") 

elapsed_time_2 = time.time() - start_time
start_time = time.time()

generate_audio_fragments("Temp_files/subs_uk.srt")
speed_up_audio_in_folder("audios", 15)
combine_audio_fragments("Temp_files/subs_uk.srt")
adjust_audio_volume("Temp_files/combined_audio.wav","Temp_files/Vocal.wav")

elapsed_time_3 = time.time() - start_time
start_time = time.time()

if num_channels == 6:
    make_3ch("Temp_files/vocals_adjusted.wav", "Temp_files/combined_audio.wav")
    combine_6ch_audio("splited_video/ENG_Audio.wav", "Temp_files/3_channel.wav", "Temp_files/result_audio.wav")
else:
    combine_2ch_audio()

if os.path.isfile(input_video) and input_video.endswith(('.mp4', '.mkv')):
    combine_all(input_video, "Output/result.mkv")
else:
    combine_all("Input/YT_Video.mp4", "Output/result.mp4")
  
elapsed_time_4 = time.time() - start_time
elapsed_time_full = time.time() - start_time_full

print(f"1 stage time: {elapsed_time_1} seconds")
print(f"split audio time: {elapsed_time_2} seconds")
print(f"speech creation time: {elapsed_time_3} seconds")
print(f"Final stage time: {elapsed_time_4} seconds")
print(f"Full time: {elapsed_time_full} seconds")

# delete_temp_files()

# запуск у colab
# переклад з Deepl

# побажання: Синтез голосами оригіналу
# Для цього що треба субтитри всюди на ass змінити