# from subsai import SubsAI, Tools

# def transcribe_audio(audio_file):
#     subs_ai = SubsAI()
#     model = subs_ai.create_model('openai/whisper', {'model_type': 'large-v2'})
#     subs = subs_ai.transcribe(audio_file, model)
#     subs.save('splited_video/ENG_Subs.srt')

from faster_whisper import WhisperModel
import torch
import pysubs2

def transcribe_audio(audio_file):
    model_size = "Systran/faster-whisper-large-v2"
    model = WhisperModel(model_size)
    def check_device():
        if torch.cuda.is_available():
            model = WhisperModel(model_size, device="cuda", compute_type="float16")
        else:
            model = WhisperModel(model_size, device="cpu", compute_type="int8")

    segments, info = model.transcribe(audio_file, beam_size=5)

    results= []
    for s in segments:
        segment_dict = {'start':s.start,'end':s.end,'text':s.text}
        results.append(segment_dict)

    pysubs2.load_from_whisper(results).save('splited_video/ENG_Subs.srt')
