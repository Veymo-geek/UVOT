# import os
# import shutil

# def setting_custom_subtitles(input_subs, result_file_name="ENG_Subs"):
#     # Функція переносить вказаний файл субтитрів у потрібний каталог 
#     # і робить потрібну назву, для подальшої роботи з ним.

#     if os.path.exists(input_subs) and (input_subs.endswith('.ass') or input_subs.endswith('.srt')):
#         # Визначення шляху для копіювання файлу
#         output_dir = "splited_video"
#         output_file = os.path.join(output_dir, result_file_name + os.path.splitext(input_subs)[1])
        
#         # Перевірка, чи існує вихідний каталог і створення його, якщо необхідно
#         if not os.path.exists(output_dir):
#             os.makedirs(output_dir)
        
#         # Копіювання файлу
#         shutil.copy(input_subs, output_file)
#         print(f"Файл скопійовано у {output_file}")
#     else:
#         print("Введений файл не існує або має неправильне розширення.")

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

