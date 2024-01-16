import os
from audio_separator.separator.separator import Separator
from pydub import AudioSegment
import ffmpeg
import time


def split_audio(file_name):
    separator = Separator(
        audio_file_path=file_name,
        primary_stem_path="Temp_files/Vocal.wav",
        secondary_stem_path="Temp_files/Instrumental.wav",
        output_format="WAV",
        model_name="UVR_MDXNET_9482"
    )
    output_files = separator.separate()
    print("Output files:", output_files)


def convert_to_2_channels(file_name, output_file_name):
    input_file = ffmpeg.input(file_name)
    output_file = ffmpeg.output(input_file, output_file_name, ac=2)
    ffmpeg.run(output_file, overwrite_output=True)


def split_6ch_audio(file_name):
    ffmpeg.input(file_name).output("Temp_files/Vocal.wav", af=f'pan=1c|c0=c2').run(overwrite_output=True)



def split_models_test(file_name, model_names):
    execution_times = {}
    for model_name in model_names:
        start_time = time.time()
        separator = Separator(
            audio_file_path=file_name,
            primary_stem_path=f"Temp_files/{model_name}_Instrumental.wav",
            secondary_stem_path=f"Temp_files/{model_name}_Vocal.wav",
            output_format="WAV",
            model_name=model_name
        )
        output_files = separator.separate()
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times[model_name] = execution_time

    # Print execution times after all work is done
    for model_name, exec_time in execution_times.items():
        print(f'For "{model_name}" time: {exec_time:.2f} sec')

# Usage
# model_names = ["Kim_Inst", "Kim_Vocal_1", "Kim_Vocal_2", 
# "Reverb_HQ_By_FoxJoy", "UVR-MDX-NET-Inst_1", 
# "UVR-MDX-NET-Inst_2", "UVR-MDX-NET-Inst_3", "UVR-MDX-NET-Inst_HQ_1", 
# "UVR-MDX-NET-Inst_HQ_2", "UVR-MDX-NET-Inst_Main", "UVR_MDXNET_1_9703", 
# "UVR_MDXNET_2_9682", "UVR_MDXNET_3_9662", "UVR_MDXNET_9482",
# "UVR_MDXNET_KARA", "UVR_MDXNET_Main", "UVR-MDX-NET-Voc_FT"]
# split_models_test("Input/30s.wav", model_names)
