from split_audio import split_audio
from separate_video_audio_subs import separate_video_audio_subs
from tts import generate_audio_fragments, combine_audio_fragments
from combine_all import combine_all
from combine_audio import combine_audio

# separate_video_audio_subs("Input/Fragment_eng.mkv")


split_audio("Audio.mp3")
# generate_audio_fragments("Temp_files/ukr_orig.srt")
# combine_audio_fragments("Temp_files/ukr_orig.srt")
combine_audio("Temp_files/combined_audio.wav","Temp_files/Vocal.wav")
combine_all("name34")



# get_video()
# normaliaze_subs()
# translate_text()

