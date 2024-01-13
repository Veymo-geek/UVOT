import os

def find_file(file_name):
    folder_path = "splited_video"  # Встановіть шлях до вашої папки
    file_name = file_name  # Назва файлу без розширення

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith(file_name) and os.path.isfile(os.path.join(root, file)):
                eng_subs = os.path.join(root, file)
                return eng_subs  # Повертаємо адресу файлу, якщо знайдено

    return None  # Повертаємо None, якщо файл не було знайдено

eng_subs = find_file("ENG_Subs")
