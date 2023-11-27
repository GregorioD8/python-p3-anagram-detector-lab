# your code goes here!

class Anagram:
    def __init__(self, word):
        # sort the words letters to compare later
        self.word_letters = sorted([letter for letter in word])

    def match(self, word_list): 
        match_word_list = []
       
        # compare letters in words 
        for word in word_list:
            if sorted([letter for letter in word]) == self.word_letters:
                match_word_list.append(word)
        return match_word_list
    
