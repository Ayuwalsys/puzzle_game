import turtle

from slide_puzzle_functions import *

puzzle.speed(0)

# initialize errror file
init_errorfile()

# open backsplash
splash_screen()

# get player information
player = player_input()

# display leaderboard error
leaderboard_error()

# creat game layout
draw_board()

# create buttons
create_buttons()

# read leaderboard file
read_leader_board()

# load puzzle files
puzzle_images = load_images(load())

# create puzzle
puzzle_pieces = set_board(puzzle_images)

with open('Text/answers.txt', 'w') as key:
    # generate answer key
    answer = answer_key(puzzle_pieces, puzzle_images)

    for each in answer:

        # write answers to file
        key.write(f'{each[1]} {each[0]}\n')

# shuffle puzzle
shuffle_puzzle = shuffle_tiles(puzzle_pieces, answer)

Turtle_screen.onclick(get_feedback)



    
       
    
    

