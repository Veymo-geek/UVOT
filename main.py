from split_audio import split_audio
from normalize_subs import normalize_subs
from separate_video_audio_subs import separate_video_audio_subs
from tts import generate_audio_fragments, combine_audio_fragments
from combine_all import combine_all
from combine_audio import combine_audio
from translate_text import translate_text

#separate_video_audio_subs("Input/Video-to-Translate.mkv")
#normalize_subs("splited_video/ENG_Subs.srt")
#translate_text("Temp_files/norm_subs.srt")
split_audio("splited_video/ENG_Audio.wav")
generate_audio_fragments("Temp_files/subs_uk.srt")
combine_audio_fragments("Temp_files/subs_uk.srt")
combine_audio("Temp_files/combined_audio.wav","Temp_files/Vocal.wav")
combine_all("Output/result.mkv")



# get_video()
# transcribe_audio()

