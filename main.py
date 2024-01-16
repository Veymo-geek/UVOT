from split_audio import split_audio, convert_to_2_channels, split_6ch_audio
from normalize_subs import normalize_subs
from separate_video_audio_subs import separate_video_audio_subs
from tts import generate_audio_fragments, combine_audio_fragments, speed_up_audio_in_folder
from combine_all import combine_all, combine_6ch_audio, combine_2ch_audio, make_3ch
from adjust_audio_volume import adjust_audio_volume
from translate_text import translate_text
from pydub import AudioSegment
from delete_files import delete_temp_files
from find_files import find_file
from transcribe_audio import transcribe_audio
import time
import gradio as gr

def main(input_video):
    print(input_video)
    separate_video_audio_subs(input_video)

    if find_file("ENG_Subs") is None:
        transcribe_audio("splited_video/ENG_Audio.wav")

    normalize_subs(find_file("ENG_Subs"))
    translate_text("Temp_files/norm_subs.srt")

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

    generate_audio_fragments("Temp_files/subs_uk.srt")
    speed_up_audio_in_folder("audios", 15)
    combine_audio_fragments("Temp_files/subs_uk.srt")
    adjust_audio_volume("Temp_files/combined_audio.wav", "Temp_files/Vocal.wav")

    if num_channels == 6:
        make_3ch("Temp_files/vocals_adjusted.wav", "Temp_files/combined_audio.wav", "Temp_files/result_audio.wav")
        combine_6ch_audio("splited_video/ENG_Audio.wav", "Temp_files/3_channel.wav", "Temp_files/result_audio.wav")
    else:
        combine_2ch_audio()

    combine_all(input_video, "Output/result.mkv")
    return "Output/result.mkv"

# Create a Gradio interface
iface = gr.Interface(
    fn=main,
    inputs=gr.inputs.File(label="Select Video"),
    outputs="video",
    live=False,
    title="UVOT - Ukrainian Voice Over Tool",
    description="Для перекладу завантажте відео",
    show_flag=False
)

iface.launch(share=True)

# delete_temp_files()


# переклад з Deepl
# відео з різних джерел get_video()
# перевірити формати при рендері
# побажання: Синтез голосами оригіналу
# Для цього що треба субтитри всюди на ass змінити