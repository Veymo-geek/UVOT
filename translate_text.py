import subprocess

def translate_text(subs):
    command = [
        'translatesubs', subs, 'Temp_files/subs_uk.srt', '--to_lang', 'uk'
    ]
    subprocess.run(command, check=True)