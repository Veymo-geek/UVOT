import os
from audio_separator.separator.separator import Separator

def split_audio(file_name):
    file_path = file_name
    instrumental_output = "Temp_files/Instrumental.wav"
    vocal_output = "Temp_files/Vocal.wav"

    separator = Separator(
        audio_file_path=file_path,
        primary_stem_path=instrumental_output,
        secondary_stem_path=vocal_output,
        output_format="WAV"
    )

    output_files = separator.separate()
    print("Output files:", output_files)

# Split the specified audio file
#split_audio("Audio.mp3")
