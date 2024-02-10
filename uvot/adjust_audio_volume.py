from pydub import AudioSegment

def adjust_audio_volume(audio_path, vocals_path):
    audio = AudioSegment.from_wav(audio_path)
    vocals_audio = AudioSegment.from_wav(vocals_path)

    # Зменшення гучності на 12 дБ в аудіофайлі vocals.wav
    reduction_in_db = -8
    vocals_audio = vocals_audio.apply_gain(reduction_in_db)

    # Поріг для визначення тиші (в мілісекундах)
    silence_threshold = -50  # Ви можете змінити це значення в залежності від амплітуди вашого аудіофайлу

    # Мінімальна тривалість тиші, щоб враховувати її (в мілісекундах)
    min_silence_duration = 1000

    # Знаходження проміжків тиші з кроком 0,001 секунди
    silent_ranges = []
    start_silence = None
    step = 1  # Крок в мілісекундах (0,001 секунди)

    for i in range(0, len(audio), step):
        chunk = audio[i:i + step]

        if chunk.dBFS < silence_threshold:
            if start_silence is None:
                start_silence = i
        else:
            if start_silence is not None:
                end_silence = i
                duration = end_silence - start_silence
                if duration >= min_silence_duration:  # Якщо тиша триває 1 секунду або довше
                    silent_ranges.append((start_silence, end_silence))
                start_silence = None

    # Збільшення гучності на 12 ДБ у проміжках тиші зі зміщенням на 200 мілісекунд
    increase_in_db = 12
    offset = 200  # зміщення в мілісекундах

    for start, end in silent_ranges:
        start_time = start / 1000 + offset / 1000
        end_time = end / 1000 - offset / 1000
        if start_time < 0:
            start_time = 0
        if end_time > len(vocals_audio) / 1000:
            end_time = len(vocals_audio) / 1000
        vocals_audio = vocals_audio.overlay(vocals_audio[start_time * 1000:end_time * 1000].apply_gain(increase_in_db), position=start_time * 1000)

    # Збереження зміненого аудіофайлу зі збільшеною гучністю у проміжках тиші
    output_path = "Temp_files/vocals_adjusted.wav"
    vocals_audio.export(output_path, format="wav")



