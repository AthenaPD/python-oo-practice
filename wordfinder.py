from random import randint
import os

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """Object to find random words from a file with many words.

    >>> wf = WordFinder("words.txt")
    235891 words read

    >>> wf.random() in wf.words
    True
    """

    def __init__(self, filename):
        self.words = []
        self.num_words = 0
        self.file_path = os.path.join(os.getcwd(), filename)
        
        self.read_file()
        self.print_length()

    def read_file(self):
        with open(self.file_path, "r") as file:
            for line in file:
                self.words.append(line[:-1])

    def print_length(self):
        self.num_words = len(self.words)
        print(f'{self.num_words} words read')

    def random(self):
        randIdx = randint(0, self.num_words-1)
        return self.words[randIdx]


class SpecialWordFinder(WordFinder):
    """This find random words from a file, in which blank line and comment are allowed.
    
    >>> swf = SpecialWordFinder("words.txt")
    235886 words read

    >>> swf.random() in swf.words
    True
    """

    def __init__(self, filename):
        super().__init__(filename)

    def read_file(self):
        with open(self.file_path, "r") as file:
            for line in file:
                if line != "\n" and not line.startswith("#"):
                    self.words.append(line[:-1])
