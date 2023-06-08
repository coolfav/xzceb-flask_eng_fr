from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    '''
    translates english to french
    '''
    translator = MyMemoryTranslator('en','fr')
    french_text = translator.translate(english_text)
    return french_text


def french_to_english(french_text):
    '''
    translates french to english
    '''
    translator = MyMemoryTranslator('fr','en')
    english_text = translator.translate(french_text)
    return english_text
