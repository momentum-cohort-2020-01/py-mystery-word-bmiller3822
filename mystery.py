import random

class Game:
    def __init__(self):
        self.player = Player("Brandon")


    def play_game(self):
        with open('words.txt', 'r') as file:
            data = file.read()
        print("")
        print ("Welcome to Word Fuckery, a word guessing game full of fuckery!")
        print ("")
        print ("Guess one fucking letter at a time until you've guessed the whole fucking word. You have 8 fucking turns.")
        word_list = [word for word in data.split()] 
        game_word = random.choice(word_list) 
        game_word = str(game_word)
        game_word = game_word.lower()
        game_word_len = len(game_word)
        game_word_letters = list(game_word)
        underscore_list = ["_"] * game_word_len
        guess_list = []
        print ("")
        print ("Your word has " f'{game_word_len}' " fucking letters:")
        print ("")
        print (self.list_to_string(underscore_list))
        print("")
        while "_" in underscore_list:
            playing = True       
            while playing:
                choice = input("Please guess a fucking letter: ")
                choice.lower()
                if choice.isalpha() and len(choice)==1:
                    #function to add all choices a third list to check if they've guessed it period.
                    if choice in guess_list:
                        print ("You have already guessed that fucking letter.")
                    elif choice in game_word_letters:
                        index_position_list = self.get_index_positions(game_word_letters,choice)
                        choice_list = len(index_position_list)*[choice,]
                        for (index, choice) in zip(index_position_list, choice_list):
                            underscore_list[index] = choice
                        print (self.list_to_string(underscore_list))
                        print ("YOU FUCKING GENIUS")
                        guess_list.append(choice)
                    else:
                        self.player.number_of_turns_remaining -=1    
                        print ("That's incorrect.  You have " f'{self.player.number_of_turns_remaining}' " fucking turns remaining.")
                        print ("")
                        guess_list.append(choice)
                else:
                    print("Please enter characters A-Z, and only one letter at a time.")
                if self.player.number_of_turns_remaining == 0:
                    self.start_over(game_word)
                break
        playing = False
        self.start_over_win()
                
    
    def get_index_positions(self, game_word_letters, choice):    
        index_pos_list = []
        index_pos = 0
        while True:
            try:
                index_pos = game_word_letters.index(choice, index_pos)
                index_pos_list.append(index_pos)
                index_pos += 1
            except:
                break
        return index_pos_list


    def list_to_string(self, underscore_list):  
        str1 = " "  
        return (str1.join(underscore_list)) 


    def start_over(self, game_word):
        print ("You are out of fucking guesses.  The correct word was: " f'{game_word}')
        play_again = input ("Press R to (R)estart.  Press anything else to exit. ")
        play_again.lower()
        if play_again == "r":
            Game().play_game()
        else:
            exit() 

    def start_over_win(self):
        print ("You fucking won you awesome mother fucker!")
        play_again = input ("Press R to (R)estart.  Press fucking anything else to exit. ")
        play_again.lower()
        if play_again == "r":
            Game().play_game()
        else:
            exit() 


class Player:
    def __init__(self, name):
        self.name = name
        self.number_of_turns_remaining = 8


game = Game()
Game().play_game()


        #In the game class allows you to redo it every time you instantiate a new game. 
        #Working with files in Jupyter notebooks. (Same for looping through the data.)
        #.readline and or tokenize them?

# .join should help with the character problem later on

# Game().play_game()
        # return (game_word_letters)

# if len(choice)<=1:
#                 break
#             else: 
#                 print("Please enter 1 letter at a time.")


# def getIndexPositions(listOfElements, element):
#     ''' Returns the indexes of all occurrences of give element in
#     the list- listOfElements '''
#     indexPosList = []
#     indexPos = 0
#     while True:
#         try:
#             # Search for item in list from indexPos to the end of list
#             indexPos = listOfElements.index(element, indexPos)
#             # Add the index position in list
#             indexPosList.append(indexPos)
#             indexPos += 1
#         except ValueError as e:
#             break
 
#     return indexPosList

# choice = [index_position_list.replace(choice, "_") for index_position_list in underscore_list]



# import random

# class Game:
#     def __init__(self):
#         self.player = Player("Brandon")


#     def play_game(self):
#         with open('words.txt', 'r') as file:
#             data = file.read()
#         print("")
#         print ("Welcome to Word Fuckery, a word guessing game full of fuckery!")
#         word_list = [word for word in data.split()] #Makes a list of all words
#         game_word = random.choice(word_list) #Picks a random list item
#         game_word = str(game_word)
#         game_word.lower()
#         game_word_len = len(game_word)
#         game_word_letters = list(game_word)
#         print("Will be hidden eventually:")
#         print (game_word_letters) #This is a list still
#         underscore_list = ["_"] * game_word_len
#         print ("")
#         print ("Your word has " f'{game_word_len}' " letters:")
#         print (str(underscore_list))
#         print("")
#         playing = True
#         while playing:
#             choice = input("Please guess a letter: ")
#             choice.lower()
#             if choice.isalpha() and len(choice)==1:
#                 if choice in underscore_list:
#                     print ("You have already chosen that letter.")
#                 elif choice in game_word_letters:
#                     #print ("Correct!") This works
#                     def get_index_positions(game_word_letters, choice):    
#                         index_pos_list = []
#                         index_pos = 0
#                         while True:
#                             try:
#                                 index_pos = game_word_letters.index(choice, index_pos)
#                                 index_pos_list.append(index_pos)
#                                 index_pos += 1
#                             except:
#                                 break
#                         return index_pos_list
#                     self.get_index_positions(game_word_letters,choice)   
#                     print (index_position_list)
                            
#             else:
#                 print("Please enter characters A-Z, and only one letter at a time.")
            
#         #     exit()
#         #Here is where I expect it to loop through again.     
# #    words = [w.replace('[br]', '<br />') for w in words]


# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.number_of_turns_remaining = 8


# game = Game()
# Game().play_game()



# index_position_list_two = index_position_list   
#                     for index in index_position_list_two:
#                         underscore_list[index_position_list_two[index]] = choice[index]
#                         print(underscore_list)


# for i in range(game_word_len):
#                         new += underscore_list[index_position_list]
#                     underscore_list = new


# index_position_list = int(str(index_position_list))
                    # new = []
                    # i=0  

                    # for index in index_position_list:
                    #     underscore_list[index_position_list[index-1]] = choice_list[index-1]
                    # print(underscore_list)

# print("Will be hidden eventually:")
#         print (game_word_letters) #This is a list still and will be deleted