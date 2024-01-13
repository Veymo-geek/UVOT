import ffmpeg

def separate_video_audio_subs(input_file):
    # Analyze the input file
    try:
        probe = ffmpeg.probe(input_file)
    except ffmpeg.Error as e:
        print('Error:', e.stderr)
        return

    largest_eng_sub = None
    largest_ukr_sub = None

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
                    # Add more mappings as needed
                }.get(sub_format, 'ass')

                output_filename = f"splited_video/{lang.upper()}_Subs.{sub_extension}"

                # Check if it's the largest subtitle so far
                if lang == 'eng':
                    if largest_eng_sub is None or stream.get('NUMBER_OF_FRAMES', 0) > largest_eng_sub.get('NUMBER_OF_FRAMES', 0):
                        largest_eng_sub = stream
                elif lang == 'ukr':
                    if largest_ukr_sub is None or stream.get('NUMBER_OF_FRAMES', 0) > largest_ukr_sub.get('NUMBER_OF_FRAMES', 0):
                        largest_ukr_sub = stream

    # After processing all streams, save the largest English subtitle file
    if largest_eng_sub:
        output_filename = f"splited_video/ENG_Subs.{sub_extension}"
        ffmpeg.input(input_file).output(output_filename, map=f"0:{largest_eng_sub['index']}").run(overwrite_output=True)

    # After processing all streams, save the largest Ukrainian subtitle file
    if largest_ukr_sub:
        output_filename = f"splited_video/UKR_Subs.{sub_extension}"
        ffmpeg.input(input_file).output(output_filename, map=f"0:{largest_ukr_sub['index']}").run(overwrite_output=True)


separate_video_audio_subs('Input/[JySzE] Naruto Shippuden - 001 [v2] - ukr.mkv')
