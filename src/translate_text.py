import subprocess

def translate_text(subs):
    command = [
        'translatesubs', subs, 'Temp_files/subs_uk.srt', '--to_lang', 'uk', '--translator', 'google_trans_new'
    ]
    subprocess.run(command, check=True)
# translate_text("Temp_files/norm_subs_wwww3.srt")
