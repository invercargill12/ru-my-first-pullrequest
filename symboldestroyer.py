def filter_string(text, char):
    result = ""
    for symbol in text:
        if symbol.lower() != char.lower():
          result = result + symbol

    return result.strip()

# Функция, устраняющая заданные символы в тексте
