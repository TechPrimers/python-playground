class Word:

    def __init__(self, text):
        self.text = text

    def __eq__(self, new_word):
        return self.text.lower() == new_word.text.lower()
