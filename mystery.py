import random

class Game:
    def __init__(self):
        self.player = Player("Brandon")


    def choose_word(self):
        with open('words.txt', 'r') as file:
            data = file.read()
        print("")
        print ("Welcome to Word Fuckery, a word guessing game full of fuckery!")
        word_list = [word for word in data.split()] #Makes a list of all words
        game_word = random.choice(word_list) #Picks a random list item
        game_word = str(game_word)
        game_word_len = len(game_word)
        game_word_letters = list(game_word)
        underscore_list = ["_"] * game_word_len
        print ("")
        print ("Your word has " f'{game_word_len}' " letters:")
        print (str(underscore_list))
        print("")
        Game().play_game()
        
    
    def play_game(self):
        playing = True
        while playing:
            choice = input("What is your first guess? ")
            choice.lower()
            if choice.isalpha():
                break
            else:
                print("Please enter characters A-Z only")
            if len(choice)<=1:
                break
            else: 
                print("Please enter 1 letter at a time.")
        print ("Hello world")
        playing = False
   


class Player:
    def __init__(self, name):
        self.name = name
        self.number_of_turns_remaining = 8


game = Game()
Game().choose_word()


        #In the game class allows you to redo it every time you instantiate a new game. 
        #Working with files in Jupyter notebooks. (Same for looping through the data.)
        #.readline and or tokenize them?

# .join should help with the character problem later on