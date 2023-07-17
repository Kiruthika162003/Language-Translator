# Language-Translator


1. Import the `Translator` class from the `googletrans` library: The `googletrans` library provides an interface to the Google Translate API, allowing us to perform language translations.

2. Define the `translate_text` function: This function takes two parameters: `text`, which represents the input text to be translated, and `target_language`, which specifies the desired language for translation.

3. Create an instance of the `Translator` class: Within the `translate_text` function, an instance of the `Translator` class is created using the line `translator = Translator()`. This object provides the necessary methods to interact with the translation functionality.

4. Perform the translation: The `translate` method of the `Translator` class is used to perform the translation. It takes the input text and the target language as parameters. In this example, the input text is translated to the specified target language using `translator.translate(text, dest=target_language)`.

5. Retrieve the translated text: The translated text can be accessed using the `text` attribute of the translated object returned by the `translate` method. In the example, `translated.text` retrieves the translated text.

6. Return the translated text: The translated text is returned as the result of the `translate_text` function.

7. Example usage: In the example usage section, a text to translate and a target language are provided. The `translate_text` function is called with these parameters, and the translated text is stored in the variable `translated_text`.

8. Print the translated text: The translated text is then printed using `print(f"Translated text: {translated_text}")`.

