import ffmpeg
import subprocess
from pydub import AudioSegment


def get_first_audio_format(input_video):
    # Use ffprobe to get the format of the first audio stream in the input video
    probe = ffmpeg.probe(input_video, v='quiet', select_streams='a:0')
    return probe['streams'][0]['codec_name']

def combine_all(input_video, result_name):
    # Get the format of the first audio stream in the input video
    input_audio_format = get_first_audio_format(input_video)

    # Convert the WAV audio to the same format as the first audio stream
    audio_conversion_command = [
        'ffmpeg', '-y', '-i', 'Temp_files/result_audio.wav',
        '-c:a', input_audio_format,
        'Temp_files/result_audio.' + input_audio_format
    ]
    subprocess.run(audio_conversion_command, check=True)

    # Combine video and new audio
    combine_command = [
        'ffmpeg', '-y', '-i', input_video,
        '-i', 'Temp_files/result_audio.' + input_audio_format, '-map', '0:v', '-map', '1:a',
        '-c:v', 'copy', '-c:a', input_audio_format, result_name
    ]
    subprocess.run(combine_command, check=True)

def combine_2ch_audio():
    # Combine audio files
    command = [
        'ffmpeg', '-y', '-i', 'Temp_files/combined_audio.wav',
        '-i', 'Temp_files/Instrumental.wav',
        '-i', 'Temp_files/vocals_adjusted.wav',
        '-filter_complex', '[0:a][1:a][2:a]amix=inputs=3:duration=longest',
        'Temp_files/result_audio.wav'
    ]
    subprocess.run(command, check=True)

def make_3ch(vocals_adjusted, combined_audio):
    # Combine audio files
    command = [
        'ffmpeg', '-y', '-i', vocals_adjusted,
        '-i', combined_audio,
        '-filter_complex', '[0:a][1:a]amix=inputs=2:duration=longest',
        'Temp_files/3_channel.wav'
    ]
    subprocess.run(command, check=True)

def combine_6ch_audio(ch6_audio, ch1_audio, output):
    audio6 = AudioSegment.from_file(ch6_audio, channels=6)
    audio1 = AudioSegment.from_file(ch1_audio, channels=1)
    channels = audio6.split_to_mono()
    target_length = len(channels[2])

    # Перевірка на однакову довжину
    if len(audio1) > target_length:
        audio1 = audio1[:target_length]
    elif len(audio1) < target_length:
        silence = AudioSegment.silent(duration=target_length - len(audio1))
        audio1 += silence

    channels[2] = audio1
    combined = AudioSegment.from_mono_audiosegments(*channels)
    combined.export(output, format='wav')  
    print(f"Combined audio saved to {output}")


# combine_all("Input/Naruto.mkv", "Output/result.mkv")