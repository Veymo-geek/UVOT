import os
from audio_separator.separator.separator import Separator

files_folder = "Temp_files/"

def split_audio(file_name):
    file_path = files_folder + file_name
    instrumental_output = files_folder + "Instrumental.flac"
    vocal_output = files_folder + "Vocal.flac"

    separator = Separator(
        audio_file_path=file_path,
        primary_stem_path=instrumental_output,
        secondary_stem_path=vocal_output,
        output_format="FLAC"
    )

    output_files = separator.separate()
    print("Output files:", output_files)

# Split the specified audio file
split_audio("Audio.mp3")
