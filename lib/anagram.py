# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word=sorted(word.lower())

    def match(self, list):
        return [word for word in list if sorted(word.lower())== self.word]