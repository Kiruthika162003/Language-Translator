from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated = translator.translate(text, dest=target_language)
    return translated.text

# Example usage
text_to_translate = "Hello, how are you?"
target_language = "es"  # Spanish
translated_text = translate_text(text_to_translate, target_language)
print(f"Translated text: {translated_text}")
