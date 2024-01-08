import os
from audio_separator.separator.separator import Separator
from pydub import AudioSegment
import ffmpeg

def split_audio(file_name):
    separator = Separator(
        audio_file_path=file_name,
        primary_stem_path="Temp_files/Instrumental.wav",
        secondary_stem_path="Temp_files/Vocal.wav",
        output_format="WAV"
    )
    output_files = separator.separate()
    print("Output files:", output_files)


def convert_to_2_channels(file_name, output_file_name):
    input_file = ffmpeg.input(file_name)
    output_file = ffmpeg.output(input_file, output_file_name, ac=2)
    ffmpeg.run(output_file, overwrite_output=True)


def split_6ch_audio(file_name):
    ffmpeg.input(file_name).output("Temp_files/Vocal.wav", af=f'pan=1c|c0=c2').run(overwrite_output=True)



# Usage
# split_audio("splited_video/ENG_Audio.wav")
