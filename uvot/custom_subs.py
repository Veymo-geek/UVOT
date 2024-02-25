import os
import pysubs2

def move_subtitles(input_subs, output_subs):
    try:
        if not os.path.isfile(input_subs):
            print(f"Файл {input_subs} не існує.")
            return
        # Завантажуємо субтитри за допомогою pysubs2
        subs = pysubs2.load(input_subs)
        
        # Зберігаємо субтитри у вказаний файл output_subs
        subs.save(output_subs)
        
        print(f"Субтитри збережено у файлі {output_subs}.")
    except Exception as e:
        print(f"Помилка при обробці субтитрів: {e}")

