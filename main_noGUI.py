from uvot.split_audio import split_audio, convert_to_2_channels, split_6ch_audio
from uvot.normalize_subs import normalize_subs
from uvot.separate_video_audio_subs import separate_video_audio_subs
from uvot.tts import generate_audio_fragments, combine_audio_fragments, speed_up_audio_in_folder
from uvot.combine_all import combine_all, combine_6ch_audio, combine_2ch_audio, make_3ch
from uvot.adjust_audio_volume import adjust_audio_volume
from uvot.translate_text import translate_text
from uvot.delete_files import delete_temp_files
from uvot.find_files import find_file
from uvot.transcribe_audio import transcribe_audio
from uvot.youtube_download import download_youtube_video
from uvot.custom_subs import move_subtitles

from pydub import AudioSegment
import time
import os
import re

input_video = "Input/Video-to-Translate.mkv"
custom_eng_subs = None
custom_ukr_subs = None

if os.path.isfile(input_video) and input_video.endswith(('.mp4', '.mkv')):
    separate_video_audio_subs(input_video)
else:
    download_youtube_video(input_video)

start_time = time.time()
start_time_full = time.time()
stt_time = 0

move_subtitles(custom_eng_subs, "splited_video/ENG_Subs.srt")
move_subtitles(custom_ukr_subs, "splited_video/UKR_Subs.srt")

if find_file("UKR_Subs") is None:
    if find_file("ENG_Subs") is None:
        transcribe_audio("splited_video/ENG_Audio.wav")
        stt_time = time.time() - start_time
        start_time = time.time()

    normalize_subs(find_file("ENG_Subs"))
    translate_text("Temp_files/norm_subs.srt")
else:
    normalize_subs(find_file("UKR_Subs"))
    move_subtitles("Temp_files/norm_subs.srt", "Temp_files/subs_uk.srt")

elapsed_time_1 = time.time() - start_time
start_time = time.time()

# Check the number of audio channels
audio = AudioSegment.from_file("splited_video/ENG_Audio.wav")
num_channels = audio.channels

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

print(f"stt time: {stt_time} seconds")
print(f"translate time: {elapsed_time_1} seconds")
print(f"split audio time: {elapsed_time_2} seconds")
print(f"speech creation time: {elapsed_time_3} seconds")
print(f"Final stage time: {elapsed_time_4} seconds")
print(f"Full time: {elapsed_time_full} seconds")

delete_temp_files()

# запуск у colab
# переклад з Deepl

# побажання: Синтез голосами оригіналу
# Для цього що треба субтитри всюди на ass змінити