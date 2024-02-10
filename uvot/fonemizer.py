from ukrainian_word_stress import Stressifier

soft_consonants = {
    "дзі+": "d̪͡z̪´ji",
    "дзя+": "d̪͡z̪´ja",
    "дзю+": "d̪͡z̪´ju",
    "дзє+": "d̪͡z̪´jɛ",
    "джі+": "d͡ʒ´ji",
    "джя+": "d͡ʒ´ja",
    "джю+": "d͡ʒ´ju",
    "джє+": "d͡ʒ´jɛ",
    "ді+": "d̪´ji",
    "дя+": "d̪´ja",
    "дю+": "d̪´ju",
    "дє+": "d̪´jɛ",
    "лі+": "ɫ´ji", #
    "ля+": "ɫ´ja", #
    "лю+": "ɫ´ju", #
    "лє+": "ɫ´jɛ", #
    "ні+": "n̪´ji",
    "ня+": "n̪´ja",
    "ню+": "n̪´ju",
    "нє+": "n̪´jɛ",
    "рі+": "r´ji",
    "ря+": "r´ja", 
    "рю+": "r´ju", 
    "рє+": "r´jɛ", 
    "сі+": "s̪´ji",
    "ся+": "s̪´ja", 
    "сю+": "s̪´ju", 
    "сє+": "s̪´jɛ", 
    "ті+": "t̪´ji",
    "тя+": "t̪´ja", 
    "тю+": "t̪´ju", 
    "тє+": "t̪´jɛ", 
    "ці+": "t̪͡s̪´ji",
    "ця+": "t̪͡s̪´ja",
    "цю+": "t̪͡s̪´ju",
    "цє+": "t̪͡s̪´jɛ",
    "зі+": "z̪´ji",
    "зя+": "z̪´ja",
    "зю+": "z̪´ju",
    "зє+": "z̪´jɛ",
    "дзь": "d̪͡z̪j",
    "дзі": "d̪͡z̪ji",
    "дзя": "d̪͡z̪ja",
    "дзю": "d̪͡z̪ju",
    "дзє": "d̪͡z̪jɛ",
    "джь": "d͡ʒj",
    "джі": "d͡ʒji",
    "джя": "d͡ʒja",
    "джю": "d͡ʒju",
    "джє": "d͡ʒjɛ",
    "ді": "d̪ji",
    "дь": "d̪ʲ",
    "дя": "d̪ja",
    "дю": "d̪ju",
    "дє": "d̪jɛ",
    "лі": "ɫji", #
    "ль": "ɫʲ", #
    "ля": "ɫja", #
    "лю": "ɫju", #
    "лє": "ɫjɛ", #
    "ні": "n̪ji",
    "нь": "n̪ʲ",
    "ня": "n̪ja",
    "ню": "n̪ju",
    "нє": "n̪jɛ",
    "рі": "rji",
    "рь": "rʲ",
    "ря": "rja", 
    "рю": "rju", 
    "рє": "rjɛ", 
    "сі": "s̪ji", #
    "сь": "s̪ʲ",
    "ся": "s̪ja",  #
    "сю": "s̪ju", #
    "сє": "s̪jɛ", #
    "ті": "t̪ji",
    "ть": "t̪ʲ",
    "тя": "t̪ja", 
    "тю": "t̪ju", 
    "тє": "t̪jɛ", 
    "ці": "t̪͡s̪ji",
    "ць": "t̪͡s̪ʲ",
    "ця": "t̪͡s̪ja",
    "цю": "t̪͡s̪ju",
    "цє": "t̪͡s̪jɛ",
    "зі": "z̪ji",
    "зь": "z̪ʲ",
    "зя": "z̪ja",
    "зю": "z̪ju",
    "зє": "z̪jɛ",
    "\'": "" #ˈ
}

exceptions = {
    "дз": "d̪͡z̪",
    "дж": "d͡ʒ",
}

stressed_vowels = {
    "е+": "´ɛ",
    "а+": "´ɑ", #
    "є+": "´jɛ",
    "і+": "´i",
    "и+": "´ɪ",
    "о+": "´ɔ",
    "у+": "´u",
    "я+": "´ja",
    "ї+": "´ji",
    "ю+": "´ju"
}

unstressed_vowels = {
    "а": "ɐ", #
    "е": "e",
    "є": "je", #
    "і": "i", #
    "и": "ɪ",
    "о": "o", #
    "у": "ʊ",
    "я": "ja",
    "ї": "ji",
    "ю": "ju"
}

other_consonants = {
    "б": "b",
    "в": "v", #
    "г": "h",
    "ґ": "ɡ", #
    "д": "d̪",
    "ж": "ʒ",
    "з": "z̪",
    "к": "k",
    "л": "ɫ",
    "м": "m",
    "н": "n̪",
    "п": "p",
    "р": "r", 
    "с": "s̪",
    "т": "t̪",
    "ф": "f",
    "й": "j",
    "х": "x",
    "ц": "t̪͡s̪",
    "ч": "t͡ʃ",
    "ш": "ʃ",
    "щ": "ɕtʂ"
}



def transform_text(input_text):
    stressify = Stressifier(stress_symbol="+", on_ambiguity="all")
    # lines_pre = input_text.split('\n')
    word = stressify(input_text)

    # Apply soft consonant replacements
    for soft_consonant, replacement in soft_consonants.items():
        word = word.replace(soft_consonant, replacement)

    # Apply exceptions
    for exception, replacement in exceptions.items():
        word = word.replace(exception, replacement)

    # Apply stressed vowel replacements
    for stressed_vowel, replacement in stressed_vowels.items():
        word = word.replace(stressed_vowel, replacement)

    # Apply unstressed vowel replacements
    for unstressed_vowel, replacement in unstressed_vowels.items():
        word = word.replace(unstressed_vowel, replacement)

    # Apply other consonant replacements
    for other_consonant, replacement in other_consonants.items():
        word = word.replace(other_consonant, replacement)

    return word

# Get input text from the user
input_text = input("Введіть текст для трансформації: ")

# Call the transform_text function and print the result to the console
transformed_text = transform_text(input_text)
print(transformed_text)
