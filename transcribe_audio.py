from subsai import SubsAI, Tools

def transcribe_audio(audio_file):
    subs_ai = SubsAI()
    model = subs_ai.create_model('openai/whisper', {'model_type': 'large-v2'})
    subs = subs_ai.transcribe(audio_file, model)
    sync_subs = Tools.auto_sync(subs, audio_file)
    sync_subs.save('splited_video/ENG_subs.srt')

