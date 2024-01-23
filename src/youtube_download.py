import os
import subprocess
import pysubs2

def download_youtube_video(url):
    # Create directory for split video if it doesn't exist
    if not os.path.exists('splited_video'):
        os.makedirs('splited_video')

    # Download the video in the best quality
    subprocess.run(['yt-dlp', '-f', 'bestvideo+bestaudio', '--merge-output-format', 'mp4', '-o', 'Input/YT_Video.mp4', url])

    # Download the English audio in the best quality
    subprocess.run(['yt-dlp', '-f', 'bestaudio', '--extract-audio', '--audio-format', 'wav', '--audio-quality', '0', '-o', 'splited_video/ENG_Audio.wav', url])

    # Download English subtitles in SRT format if they are not automatically generated
    subprocess.run(['yt-dlp', '--write-sub', '--sub-langs', 'en', '--skip-download', '--sub-format', 'srt', '-o', 'splited_video/ENG_Subs.srt', url])

    # Download Ukrainian subtitles in SRT format if they are not automatically generated
    subprocess.run(['yt-dlp', '--write-sub', '--sub-langs', 'uk', '--skip-download', '--sub-format', 'srt', '-o', 'splited_video/UKR_Subs.srt', url])

    eng_subs_path = "splited_video/ENG_Subs.srt.en.vtt"
    ukr_subs_path = "splited_video/UKR_Subs.srt.en.vtt"

    # Convert English subtitles
    if os.path.exists(eng_subs_path):
        subs = pysubs2.load(eng_subs_path, encoding="utf-8")
        subs.save("splited_video/ENG_Subs.srt")

    # Convert Ukrainian subtitles
    if os.path.exists(ukr_subs_path):
        subs1 = pysubs2.load(ukr_subs_path, encoding="utf-8")
        subs1.save("splited_video/UKR_Subs.srt")


# Example usage
# download_youtube_video('https://www.youtube.com/watch?v=BiuCP0QFg5k&ab_channel=TED')