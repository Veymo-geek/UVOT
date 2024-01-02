import subprocess
import os
import re

def separate_video_audio_subs(input_file):
    # Check if the file exists
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        return

    # Create a directory for the split files
    output_dir = "splited_video"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extract the base name for the output files
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_path = os.path.join(output_dir, base_name)

    # Function to extract metadata
    def extract_metadata():
        cmd = f"ffmpeg -i {input_file}"
        result = subprocess.run(cmd, shell=True, text=True, stderr=subprocess.PIPE)
        return result.stderr

    # Parse metadata to find audio and subtitle tracks
    metadata = extract_metadata()
    audio_tracks = re.findall(r"Stream #.*?Audio:.*?([a-z]{2,})", metadata)
    subtitle_tracks = re.findall(r"Stream #.*?Subtitle:.*?([a-z]{2,})", metadata)

    try:
        # Extract audio tracks
        for i, lang in enumerate(audio_tracks):
            audio_command = f"ffmpeg -i {input_file} -map 0:a:{i} -c copy {output_path}_audio_{i}_{lang}.aac"
            subprocess.call(audio_command, shell=True)

        # Extract subtitle tracks
        for i, lang in enumerate(subtitle_tracks):
            subtitle_command = f"ffmpeg -i {input_file} -map 0:s:{i} {output_path}_subtitles_{i}_{lang}.srt"
            subprocess.call(subtitle_command, shell=True)

        print("Extraction completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# separate_video_audio_subs("Input/Fragment_eng.mkv")
