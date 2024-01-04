import subprocess

def combine_all(result_name):
    # Combine audio files
    command = [
        'ffmpeg', '-i', 'Temp_files/combined_audio.wav',
        '-i', 'Temp_files/Instrumental.wav',
        '-i', 'Temp_files/vocals_adjusted.wav',
        '-filter_complex', '[0:a][1:a][2:a]amix=inputs=3:duration=longest',
        'Temp_files/result_audio.wav'
    ]
    subprocess.run(command, check=True)

    # Convert to AAC format
    command = [
        'ffmpeg', '-i', 'Temp_files/result_audio.wav',
        '-c:a', 'aac', '-strict', '-2',
        'Temp_files/result_audio.aac'
    ]
    subprocess.run(command, check=True)

    # Combine video and new audio
    command = [
        'ffmpeg', '-i', 'Input/Video.mkv',
        '-i', 'Temp_files/result_audio.aac', '-map', '0:v', '-map', '1:a',
        '-c:v', 'copy', '-c:a', 'aac', 'Output/result.mkv'
    ]
    subprocess.run(command, check=True)

    # Rename and move the final video file
    # final_path = f"Output/{result_name}.mp4"
    # command = ['mv', 'Output/result.mkv', final_path]
    # subprocess.run(command, check=True)

    # print(f"Output video saved as {final_path}")

