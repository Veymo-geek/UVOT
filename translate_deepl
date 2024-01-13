from PyDeepLX import PyDeepLX
import pysubs2
import deepl
import os
from srtranslator import SrtFile
from srtranslator.translators.deepl_scrap import DeeplTranslator

def translate_text_deepl(text):
    return PyDeepLX.translate(text, "auto", "uk", 0, False, 'socks5://103.115.20.52:8199')


example_text = "Два мільйони років тому наша планета була зовсім іншою. ^^^^^ Шаблезубий кіт, смілодон. ^^^^^ Страшний хижак свого часу. ^^^^^ На шляху стоїть велетенський птах-терорист, заввишки два метри. ^^^^^ Обидві сторони озброєні... ^^^^^ і готові до сутички. ^^^^^ Це історія про великі битви за виживання ^^^^^ і династії, які захоплять світ. ^^^^^ Це історія життя."

def get_plain_text(path):
    subs = pysubs2.load(path)
    plain_text = []
    for sub in subs:
        plain_text.append(sub.text)
    return " ^^^^^ ".join(plain_text)

def get_subs_from_text(subs_reference_path, plain_text):
    subs_reference = pysubs2.load(subs_reference_path)
    lines = plain_text.split(" ^^^^^ ")
    subs = pysubs2.SSAFile()
    
    for line, ref_sub in zip(lines, subs_reference):
        sub = pysubs2.SSAEvent()
        sub.text = line
        sub.start = ref_sub.start
        sub.end = ref_sub.end
        subs.append(sub)
    
    return subs

my_text = get_plain_text("Temp_files/norm_subs.srt")
# my_text1 = translate_text_deepl("Hello!")
print(my_text)
# print(get_plain_text("Temp_files/norm_subs.srt"))
# converted_subs = get_subs_from_text("Temp_files/norm_subs.srt", example_text) 
# print("Converted Subtitles:")
# for line in converted_subs:
#     print(line.text)


# auth_key = "XbWajyHQE42mRha3mCEez"  # Replace with your key
# translator = deepl.Translator(auth_key)

# result = translator.translate_text("Hello, world!", target_lang="UK")
# print(result.text)  # "Bonjour, le monde !"

translator = DeeplTranslator() 
filepath = "Temp_files/norm_subs.srt"

# SRT File
sub = SrtFile(filepath)
# ASS File
# sub = AssFile(filepath)

# Translate
sub.translate(translator, "en", "uk")

# Making the result subtitles prettier
sub.wrap_lines()

sub.save(f"{os.path.splitext(filepath)[0]}_translated.srt")