import ffmpeg

def separate_video_audio_subs(input_file):
    # Analyze the input file
    try:
        probe = ffmpeg.probe(input_file)
    except ffmpeg.Error as e:
        print('Error:', e.stderr)
        return

    for stream in probe['streams']:
        # Check if the stream is audio and in English
        if stream['codec_type'] == 'audio' and stream['tags'].get('language') == 'eng':
            ffmpeg.input(input_file).output('splited_video/ENG_Audio.wav', map=f"0:{stream['index']}").run(overwrite_output=True)

        # Check if the stream is audio and in Ukrainian
        elif stream['codec_type'] == 'audio' and stream['tags'].get('language') == 'ukr':
            ffmpeg.input(input_file).output('splited_video/UKR_Audio.wav', map=f"0:{stream['index']}").run(overwrite_output=True)

        # Check if the stream is a subtitle and in English or Ukrainian
        elif stream['codec_type'] == 'subtitle':
            lang = stream['tags'].get('language')
            if lang in ['eng', 'ukr']:
                # Determine subtitle format
                sub_format = stream.get('codec_name', 'srt')
                sub_extension = {
                    'subrip': 'srt', 
                    'ass': 'ass', 
                    'ssa': 'ssa', 
                    'vobsub': 'sub', 
                    'mov_text': 'txt', 
                    # Add more mappings as needed
                }.get(sub_format, 'srt')

                output_filename = f"splited_video/{lang.upper()}_Subs.{sub_extension}"
                ffmpeg.input(input_file).output(output_filename, map=f"0:{stream['index']}").run(overwrite_output=True)

# Example usage

# separate_video_audio_subs('Input/Video-to-Translate.mkv')


# Example usage
# separate_video_audio_subs("Input/Fragment_eng.mkv")
