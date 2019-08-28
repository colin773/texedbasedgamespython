import random
import time
import os
import sys


class Player:

    def __init__(self):
        self.name = ' '
        self.health = 0
        self.difficulty = ' '
        self.location = 'e'
        self.gameover = False


myPlayer = Player()


def title_screen_selection():
    option = input("> ")
    if option.lower() == "play":
        start_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "return":
        title_screen()
    elif option.lower() == "quit":
        quit()
        while option.lower() not in ['play', 'help', 'quit', 'return']:
            print("please enter a valid command (play, help, quit)")
            option = input("> ")
            if option.lower() == "play":
                start_game()
            elif option.lower() == "help":
                help_menu()
            elif option.lower() == "quit":
                quit()
            elif option.lower() == "return":
                title_screen()


def title_screen():
    os.system('clear')
    print("""

     ▄████▄  ▄▄▄   ██▒   █▓█████    ▓█████  ██████ ▄████▄  ▄▄▄      ██▓███ ▓█████ 
    ▒██▀ ▀█ ▒████▄▓██░   █▓█   ▀    ▓█   ▀▒██    ▒▒██▀ ▀█ ▒████▄   ▓██░  ██▓█   ▀ 
    ▒▓█    ▄▒██  ▀█▓██  █▒▒███      ▒███  ░ ▓██▄  ▒▓█    ▄▒██  ▀█▄ ▓██░ ██▓▒███   
    ▒▓▓▄ ▄██░██▄▄▄▄█▒██ █░▒▓█  ▄    ▒▓█  ▄  ▒   ██▒▓▓▄ ▄██░██▄▄▄▄██▒██▄█▓▒ ▒▓█  ▄ 
    ▒ ▓███▀ ░▓█   ▓██▒▀█░ ░▒████▒   ░▒████▒██████▒▒ ▓███▀ ░▓█   ▓██▒██▒ ░  ░▒████▒
    ░ ░▒ ▒  ░▒▒   ▓▒█░ ▐░ ░░ ▒░ ░   ░░ ▒░ ▒ ▒▓▒ ▒ ░ ░▒ ▒  ░▒▒   ▓▒█▒▓▒░ ░  ░░ ▒░ ░
      ░  ▒    ▒   ▒▒ ░ ░░  ░ ░  ░    ░ ░  ░ ░▒  ░ ░ ░  ▒    ▒   ▒▒ ░▒ ░     ░ ░  ░
    ░         ░   ▒    ░░    ░         ░  ░  ░  ░ ░         ░   ▒  ░░         ░   
    ░ ░           ░  ░  ░    ░  ░      ░  ░     ░ ░ ░           ░  ░          ░  ░
    ░                  ░                          ░                               
                                    made by colin773
                                         >play
                                         >help
                                         >quit
    """)
    title_screen_selection()


def help_menu():
    os.system('clear')
    print("""

     ▄████▄  ▄▄▄   ██▒   █▓█████    ▓█████  ██████ ▄████▄  ▄▄▄      ██▓███ ▓█████ 
    ▒██▀ ▀█ ▒████▄▓██░   █▓█   ▀    ▓█   ▀▒██    ▒▒██▀ ▀█ ▒████▄   ▓██░  ██▓█   ▀ 
    ▒▓█    ▄▒██  ▀█▓██  █▒▒███      ▒███  ░ ▓██▄  ▒▓█    ▄▒██  ▀█▄ ▓██░ ██▓▒███   
    ▒▓▓▄ ▄██░██▄▄▄▄█▒██ █░▒▓█  ▄    ▒▓█  ▄  ▒   ██▒▓▓▄ ▄██░██▄▄▄▄██▒██▄█▓▒ ▒▓█  ▄ 
    ▒ ▓███▀ ░▓█   ▓██▒▀█░ ░▒████▒   ░▒████▒██████▒▒ ▓███▀ ░▓█   ▓██▒██▒ ░  ░▒████▒
    ░ ░▒ ▒  ░▒▒   ▓▒█░ ▐░ ░░ ▒░ ░   ░░ ▒░ ▒ ▒▓▒ ▒ ░ ░▒ ▒  ░▒▒   ▓▒█▒▓▒░ ░  ░░ ▒░ ░
      ░  ▒    ▒   ▒▒ ░ ░░  ░ ░  ░    ░ ░  ░ ░▒  ░ ░ ░  ▒    ▒   ▒▒ ░▒ ░     ░ ░  ░
    ░         ░   ▒    ░░    ░         ░  ░  ░  ░ ░         ░   ▒  ░░         ░   
    ░ ░           ░  ░  ░    ░  ░      ░  ░     ░ ░ ░           ░  ░          ░  ░
    ░                  ░                          ░                               

                       type move to move and up/down to chose where
                                  type your commands
                      there are 4 rooms you must pass through to win
                              type return for title screen
    """)
    title_screen_selection()


def game_over_win():
    os.system('clear')
    print("""

             ▄████ ▄▄▄      ███▄ ▄███▓█████     ▒█████  ██▒   █▓█████ ██▀███  
            ██▒ ▀█▒████▄   ▓██▒▀█▀ ██▓█   ▀    ▒██▒  ██▓██░   █▓█   ▀▓██ ▒ ██▒
           ▒██░▄▄▄▒██  ▀█▄ ▓██    ▓██▒███      ▒██░  ██▒▓██  █▒▒███  ▓██ ░▄█ ▒
           ░▓█  ██░██▄▄▄▄██▒██    ▒██▒▓█  ▄    ▒██   ██░ ▒██ █░▒▓█  ▄▒██▀▀█▄  
           ░▒▓███▀▒▓█   ▓██▒██▒   ░██░▒████▒   ░ ████▓▒░  ▒▀█░ ░▒████░██▓ ▒██▒
            ░▒   ▒ ▒▒   ▓▒█░ ▒░   ░  ░░ ▒░ ░   ░ ▒░▒░▒░   ░ ▐░ ░░ ▒░ ░ ▒▓ ░▒▓░
             ░   ░  ▒   ▒▒ ░  ░      ░░ ░  ░     ░ ▒ ▒░   ░ ░░  ░ ░  ░ ░▒ ░ ▒░
           ░ ░   ░  ░   ▒  ░      ░     ░      ░ ░ ░ ▒      ░░    ░    ░░   ░ 
                 ░      ░  ░      ░     ░  ░       ░ ░       ░    ░  ░  ░     
                                                            ░                 
                                         YOU WIN!!
                                >restart (restart the game)
                                  >credits (credit screen)
                                   >quit (quit the game)

    """)
    game_over_selection()


def credit_screen():
    os.system('clear')
    print("""

             ▄████ ▄▄▄      ███▄ ▄███▓█████     ▒█████  ██▒   █▓█████ ██▀███  
            ██▒ ▀█▒████▄   ▓██▒▀█▀ ██▓█   ▀    ▒██▒  ██▓██░   █▓█   ▀▓██ ▒ ██▒
           ▒██░▄▄▄▒██  ▀█▄ ▓██    ▓██▒███      ▒██░  ██▒▓██  █▒▒███  ▓██ ░▄█ ▒
           ░▓█  ██░██▄▄▄▄██▒██    ▒██▒▓█  ▄    ▒██   ██░ ▒██ █░▒▓█  ▄▒██▀▀█▄  
           ░▒▓███▀▒▓█   ▓██▒██▒   ░██░▒████▒   ░ ████▓▒░  ▒▀█░ ░▒████░██▓ ▒██▒
            ░▒   ▒ ▒▒   ▓▒█░ ▒░   ░  ░░ ▒░ ░   ░ ▒░▒░▒░   ░ ▐░ ░░ ▒░ ░ ▒▓ ░▒▓░
             ░   ░  ▒   ▒▒ ░  ░      ░░ ░  ░     ░ ▒ ▒░   ░ ░░  ░ ░  ░ ░▒ ░ ▒░
           ░ ░   ░  ░   ▒  ░      ░     ░      ░ ░ ░ ▒      ░░    ░    ░░   ░ 
                 ░      ░  ░      ░     ░  ░       ░ ░       ░    ░  ░  ░     
                                                            ░                 
                 credits: 2019 colin773,  this is my first python game 
                  big text from: http://www.patorjk.com/software/taag/
                                   Thanks for playing
                                  >return for previous

    """)
    game_over_selection()


def game_over_selection():
    option = input("> ")
    if option.lower() == "credits":
        credit_screen()
    elif option.lower() == "return":
        game_over_win()
    elif option.lower() == "restart":
        quit()
    elif option.lower() == "quit":
        end = "thank you for playing\n"
        for character in end:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.04)
        quit()
        while option.lower() not in ['play', 'help', 'quit', 'return']:
            print("please enter a valid command (play, help, quit)")
            option = input("> ")
            if option.lower() == "credits":
                credit_screen()
            elif option.lower() == "return":
                game_over_win()
            elif option.lower() == "restart":
                quit()
            elif option.lower() == "quit":
                end = "thank you for playing\n"
                for character in end:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.04)

# MAP

# a
# b
# c
# d


ZONENAME = 'zone'
DESCRIPTION = 'description'
EXAMINATION = 'examin'
RIDDLE = 'riddle'
ANSWER = 'answer'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'

solved_places = {'a': False,
                 'b': False,
                 'c': False,
                 'd': False,
                 }


zonemap = {
    'a': {
        ZONENAME: 'Escape',
        DESCRIPTION: 'YOU WIN',
        EXAMINATION: ' ',
        RIDDLE: ' ',
        ANSWER: ' ',
        SOLVED: False,
        UP: '',
        DOWN: 'b',
    },
    'b': {
        ZONENAME: 'Last Room',
        DESCRIPTION: 'This is the last room you need to pass through to escape',
        EXAMINATION: 'clues to riddle or whatever',
        RIDDLE: 'The whiter i am the dirtier i get, what am i?',
        ANSWER: 'white board',
        SOLVED: False,
        UP: 'a',
        DOWN: 'c',
    },
    'c': {
        ZONENAME: 'Third Room',
        DESCRIPTION: 'This is the third room you need to escape \nthe puzzle is a bit harder',
        EXAMINATION: 'you see a butchers shop on the wall',
        RIDDLE: 'Tom’s height is six feet, he is an assistant at a butcher’s shop, \nand wears size 12 shoes. \nWhat does he weigh?',
        ANSWER: 'meat',
        SOLVED: False,
        UP: 'b',
        DOWN: 'd',
    },
    'd': {
        ZONENAME: 'Second Room',
        DESCRIPTION: 'This is the second room you need to escape \nthe puzzle is a bit harder',
        EXAMINATION: 'Theres a panda bear using a blender on the wall',
        RIDDLE: 'Whats black and white and read all over?',
        ANSWER: 'a panda in a blender or a newspaper',
        SOLVED: False,
        UP: 'c',
        DOWN: 'e',
    },
    'e': {
        ZONENAME: 'Start Room',
        DESCRIPTION: 'This is the first room you need to escape',
        EXAMINATION: 'there is a big letter E on the wall, \ni wonder what that means',
        RIDDLE: 'what has 3 legs and stands like a table?',
        ANSWER: 'the letter E',
        SOLVED: False,
        UP: 'd',
        DOWN: 'a',
    },

}


# GAME INTERACTION
def print_location():
    print('\n' + ('%' * (6 + len(zonemap[myPlayer.location][ZONENAME]))))
    print('%' + zonemap[myPlayer.location][ZONENAME] + '%')
    print('\n' + ('%' * (6 + len(zonemap[myPlayer.location][ZONENAME]))))


def prompt():
    print("\n")
    print("what do you wanna do?")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk',
                          'examine', 'inspect', 'look', 'interact',
                          'riddle', 'solve', 'try', 'answer',
                          'quit']
    while action.lower() not in acceptable_actions:
        print("invalid request/action, try again  (valid actions: move, look, solve) \n")
        action = input("> ")
    if action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move()
    elif action.lower() in ['examine', 'inspect', 'look', 'interact', ]:
        player_examine()
    elif action.lower() in ['riddle', 'solve', 'try', 'answer', ]:
        player_answer()
    elif action.lower() in 'quit':
        print("thanks for playing")
        quit()


def player_move():
    if zonemap[myPlayer.location][SOLVED]:
        ask = "where would you like to move?\n"
        dest = input(ask + "> ")
        if dest in ['up', 'north']:
            destination = zonemap[myPlayer.location][UP]
            movement_handeler(destination)
        if dest in ['down', 'south']:
            destination = zonemap[myPlayer.location][DOWN]
            movement_handeler(destination)
    else:
        print("you cant move until the riddle in this room is solved. \ntry looking around")


def movement_handeler(destination):
    myPlayer.location = destination
    print("\n" + "you have moved to the " +
          zonemap[myPlayer.location][ZONENAME])
    print("\n" + zonemap[myPlayer.location][DESCRIPTION])
    if destination is 'a':
        myPlayer.gameover = True
        print("you have just won the game " + myPlayer.name +
              "!!\ncongragumaations you have escaped the cave")
    # print_location()


def player_examine():
    if zonemap[myPlayer.location][SOLVED]:
        print("\nyou have already solved the riddle and can move up to the next room")
        print("the clue \"" + zonemap[myPlayer.location]
              [EXAMINATION] + "\" really helped you solve the puzzel")
    else:
        print(zonemap[myPlayer.location][EXAMINATION])


def player_answer():
    if zonemap[myPlayer.location][SOLVED]:
        print("\nyou have already solved the riddle and can move up to the next room")
    else:
        print(zonemap[myPlayer.location][RIDDLE])
        print("\nwhat do you think the answer is?")
        desision = input("> ")
        if desision in zonemap[myPlayer.location][ANSWER]:
            print("\ngood job!\nyou may now move up to the next room")
            zonemap[myPlayer.location][SOLVED] = True
        else:
            player_answer()


# GAME FUNCTONALITY + STORY

def main_game_loop():
    while myPlayer.gameover is False:
        prompt()
    input("press enter to continue\n> ")
    game_over_win()


def start_game():
    os.system('clear')

    # NAME SELECT
    question1 = "hello player, what is your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

    # DIFFICULTY SELECT
    question2 = "what difficulty do you pick?\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print("(you can play on easy, medium or hard)\n")
    player_difficulty = input("> ")
    valid_difficulty = ['easy', 'medium', 'hard', ]
    if player_difficulty.lower() in valid_difficulty:
        myPlayer.difficulty = player_difficulty
        print("\nyou are playing on " + player_difficulty + " mode\n")
    while player_difficulty.lower() not in valid_difficulty:
        print("\n invalid setting please try again")
        player_difficulty = input("> ")
        if player_difficulty.lower() in valid_difficulty:
            myPlayer.difficulty = player_difficulty
            print("\nyou are playing on " + player_difficulty + " mode\n")

    ###DIFFICULTY + HEALTH
    if myPlayer.difficulty is 'easy':
        myPlayer.health = 120
    elif myPlayer.difficulty is 'medium':
        myPlayer.health = 100
    elif myPlayer.difficulty is 'hard':
        myPlayer.health = 80

    # INTRODUCTION
    question3 = "welcome, " + player_name + "\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    time.sleep(1)
    os.system('clear')
    story1 = "random storyline that makes it reasonable that you are in a \ncave with 4 locked rooms that you can only escape by \nanswering riddles. i will change this backstory later\n"
    for character in story1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
    story2 = "and then"
    for character in story2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.09)
    story3 = "...\n\n"
    for character in story3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    time.sleep(0.5)
    print("click\n")
    time.sleep(1)
    os.system('clear')
    print("the adventure begins")
    main_game_loop()


title_screen()
