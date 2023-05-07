import turtle
import random
import time
import copy
from math import sqrt

# initialize layout turtle
puzzle = turtle.Turtle()

puzzle.speed(0)

# intialize screen
Turtle_screen = turtle.Screen()

Turtle_screen.setup(1000, 1000)

# assign backsplash
splash_back = 'Resources/splash_screen.gif'

# add back splash to shape list
Turtle_screen.addshape(splash_back)

# assign back splash to turtle
puzzle.shape(splash_back)

# initialize load button
button_loader = turtle.Turtle()

# hide load button
button_loader.hideturtle()

Turtle_screen.addshape('Resources/loadbutton.gif')

button_loader.shape('Resources/loadbutton.gif')

button_loader.speed(0)

# initialize reset button
button_reset = turtle.Turtle()

# hide reset button
button_reset.hideturtle()

Turtle_screen.addshape('Resources/resetbutton.gif')

button_reset.shape('Resources/resetbutton.gif')

button_reset.speed(0)

# initialize quit button
button_quit = turtle.Turtle()

# hide quit button
button_quit.hideturtle()

Turtle_screen.addshape('Resources/quitbutton.gif')

button_quit.shape('Resources/quitbutton.gif')

button_quit.speed(0)

# intial turtle to count moves
move_counter = turtle.Turtle()

move_counter.speed(0)

move_counter.hideturtle()

move_counter.penup()

# set count position
move_counter.setposition(-377.0, -289.0)

# dict to hold turtles
dictionary_turtles = {}

# dict to hold thumbnails
dictionary_thumb = {}


def splash_screen():
    """ function that display background splash for 4 seconds"""

    game_state = 'splash'

    # back splash time limit
    time_limit = 4

    # game start time
    start_time = time.time()

    while game_state == 'splash':

        # back splash countdown timer
        elapsed = time.time() - start_time

        # timer ends
        if elapsed > time_limit:
            # hide turtle
            puzzle.hideturtle()

            game_state = 'playing'


def rectangle(l, w):
    """
        function that takes integer values
        for length and width to draw a rectangle
    """

    # for each side in the rectangle
    for i in range(4):

        if i % 2 == 0:
            # draw even side length
            puzzle.forward(w)
            puzzle.left(90)

        else:
            # draw odd side length
            puzzle.forward(l)
            puzzle.left(90)


def player_input():
    """
        Function that prompt user for player_name and number of
        desired Number of player_moves and return data in a list
    """

    # record player_name
    player_name = Turtle_screen.textinput('Name', 'Enter Player Name:')

    # set number of player_moves
    player_moves = Turtle_screen.numinput('Moves', 'Enter Desired Number of Moves (5 - 200):', minval=5, maxval=200)

    with open('Text/players.txt', 'a') as players, open('Text/moves.txt', 'w') as count:
        # add player_name and player_moves to players file
        players.write(f'{int(player_moves)} : {player_name}\n')

        # add number of player_moves to counter file
        count.write(f'{int(player_moves)}')


def draw_board():
    """
        Function that create boarder of game board
    """

    # Create Game Area
    puzzle.penup()
    puzzle.goto(-480, -150)
    puzzle.pensize(10)
    puzzle.pendown()
    rectangle(500, 550)

    # Create Leader Board
    puzzle.penup()
    puzzle.goto(95, -150)
    puzzle.pensize(8)
    puzzle.color('blue')
    puzzle.pendown()
    rectangle(500, 375)

    # Create Status Bar
    puzzle.penup()
    puzzle.goto(-480, -360)
    puzzle.pensize(8)
    puzzle.color('black')
    puzzle.pendown()
    rectangle(150, 950)


def read_leader_board():
    """
        function that read leaderboard txt file to display in game
    """

    puzzle.penup()
    puzzle.setpos(-450, -290)
    puzzle.pendown()
    puzzle.write('Moves:', align='left', font=('Arial', 20, 'normal'))

    puzzle.penup()
    puzzle.goto(110, 295)

    try:
        # read leaderboard file
        with open('Text/Leaderboard.txt', 'r') as leaderboard:

            # hold position_y
            position_y = 295

            for each in leaderboard:
                # write each score to leader board
                puzzle.write(each, align='left', font=('Arial', 20, 'normal'))

                # increment entry lines
                position_y -= 30

                # set new position of entry
                puzzle.goto(110, position_y)

    except FileNotFoundError:

        # write leaderboard file
        with open('Text/Leaderboard.txt', 'w') as new_file:

            # write title to leader board file
            new_file.write('Leader board:')

            # hold position_y
            position_y = 295

        # read leaderboard file
        with open('Text/Leaderboard.txt', 'r') as leaderboard:

            for each in leaderboard:
                # write each score to leader board
                puzzle.write(each, align='left', font=('Arial', 20, 'normal'))

                # increment entry lines
                position_y -= 30

                # set new position of entry
                puzzle.goto(100, position_y)

    # count moves
    with open('Text/moves.txt', 'r') as initial:

        # retrieve moves
        counter = initial.read()
        counter = int(counter)

        # write number of moves        
        move_counter.write(f'{counter}', align='left', font=('Arial', 20, 'normal'))


def leaderboard_error():
    try:

        # check if leaderboard file exists
        with open('Text/Leaderboard.txt', 'r') as leaderboard:

            pass

    except FileNotFoundError:

        game_state = 'error'

        # store leaderboard error
        image = 'Resources/leaderboard_error.gif'

        # error time limit
        time_limit = 4

        # record error start time
        start_time = time.time()

        # add leaderboard error 
        Turtle_screen.addshape(image)

        # set turtle as leaderboard error
        puzzle.shape(image)

        while game_state == 'error':

            # show error
            puzzle.st()

            # error countdown timer
            elapsed = time.time() - start_time

            # timer ends
            if elapsed > time_limit:
                # hide turtle
                puzzle.ht()

                game_state = 'playing'

        # append to error file        
        with open('Text/5001_puzzle.err', 'a') as error:
            error.write('leaderboard error, file not found. \n')


def write_leader_board():
    """
        function that takes a list containing player stats and writes
        to leader board txt file to display in game
    """
    # holds top ten leaders
    leaders = []

    # holds all scores
    scores = []

    with open('Text/players.txt', 'r') as players, open('Text/moves.txt', 'r') as count:

        for each in players:
            # seperate moves from name
            each = each.split(' : ')

            each[1] = each[1].strip('\n')

            each[0] = int(each[0])

            # append all scores to list
            scores.append(each)

        # store moves
        moves = int(count.read())

        # update current players score
        scores[-1][0] = int(scores[-1][0]) - moves

        # sort scores by lowest moves
        scores.sort()

    i = 0

    with open('Text/Leaderboard.txt', 'w') as leaderboard:
        # write title to leader board file
        leaderboard.write('Leader board:\n')

        while i < 10 and i < len(scores):
            # write top 10 to leader board file
            leaderboard.write(f'{scores[i][0]} : {scores[i][1]}\n')
            i += 1


def init_errorfile():
    """
        function that creates a txt
        file to record game errors

    """

    with open('Text/5001_puzzle.err', 'a') as error:
        pass


def load_images(puzzle='mario'):
    """
           Function that append puzzle pieces to a list and return
           a list of images
       """

    # holds puzzle metadata
    puzzle_data = {}

    with open(puzzle + '.puz', 'r') as puz:

        for each in puz:
            # split puzzle data
            each = each.split(': ')

            # strip spaces
            each[1] = each[1].strip('\n')

            # append metadata to dictionary
            puzzle_data[each[0]] = each[1]

    # create list to store images
    images = []

    # append puzzle dimensions
    images.append(int(puzzle_data['number']))

    # append pixel size
    images.append(int(puzzle_data['size']))

    # append thumbnail
    images.append(f'Images/{puzzle}/{puzzle}_thumbnail.gif')

    # append blank tile
    images.append(f'Images/{puzzle}/blank.gif')

    for i in range(int(puzzle_data['number']) - 1):
        # append images
        images.append(f'Images/{puzzle}/{i + 2}.gif')

    return images


def load():
    """
            Function that load new type_puzzle, append type_puzzle tiles to a
            list and return the list of images

        """

    # holds all type_puzzle dimensions
    dim = [4, 9, 16]

    # holds type_puzzle metadata
    puzzle_data = {}

    # type_puzzle options
    m = 'mario'
    l = 'luigi'
    s = 'smiley'
    y = 'yoshi'
    f = 'fifteen'

    # user chooses type_puzzle
    type_puzzle = Turtle_screen.textinput('Choose a Puzzle:', f'{m}\n {l}\n {s}\n {y}\n {f}\n')

    # check if type_puzzle exists
    try:
        with  open('Text/reset_file.txt', 'w') as reset, open(type_puzzle + '.puz', 'r') as puz:

            for each in puz:
                # split type_puzzle data
                each = each.split(': ')

                # strip spaces
                each[1] = each[1].strip('\n')

                # append metadata to dictionary
                puzzle_data[each[0]] = each[1]

            # check for valid images
            image_checker = turtle.Turtle()

            image_checker.ht()

            # check thumbnail
            Turtle_screen.addshape(puzzle_data['thumbnail'])

            image_checker.shape(puzzle_data['thumbnail'])

            for i in range(len(puzzle_data) - 4):
                # add image to screen
                Turtle_screen.addshape(puzzle_data[f'{i + 1}'])

                # check gifs
                image_checker.shape(puzzle_data[f'{i + 1}'])

            # write type_puzzle name to reset file
            reset.write(type_puzzle)
            print(type_puzzle)

        return type_puzzle


    # if type_puzzle does not exist
    except:

        state = 'no type_puzzle'

        while state == 'no type_puzzle':

            # change state to error
            game_state = 'error'

            # error time limit
            time_limit = 2.5

            # record error start time
            start_time = time.time()

            # init turlte for file error
            puz_error = turtle.Turtle()

            # add type_puzzle file error
            Turtle_screen.addshape('Resources/file_error.gif')

            # make turtle file error image
            puz_error.shape('Resources/file_error.gif')

            while game_state == 'error':

                # error countdown timer
                elapsed = time.time() - start_time

                # timer ends
                if elapsed > time_limit:
                    # hide error message
                    puz_error.hideturtle()

                    game_state = 'playing'

            # append to error file        
            with open('Text/5001_puzzle.err', 'a') as error:
                error.write('type_puzzle file error, file not found. \n')

            # user chooses type_puzzle
            type_puzzle = Turtle_screen.textinput('Choose a Puzzle:', f'{m}\n {l}\n {s}\n {y}\n {f}\n')

            try:
                with open('Text/reset_file.txt', 'w') as reset, open(f'{type_puzzle}.puz', 'r') as puz:

                    for each in puz:
                        # split type_puzzle data
                        each = each.split(': ')

                        # strip spaces
                        each[1] = each[1].strip('\n')

                        # append metadata to dictionary
                        puzzle_data[each[0]] = each[1]

                    if int(puzzle_data['number']) in dim:
                        # declares a type_puzzle has been loaded
                        state = 'type_puzzle!'

                        # write type_puzzle name to reset file
                        reset.write(type_puzzle)
            except:

                state = 'no type_puzzle'

    return type_puzzle


def set_board(lst):
    """
        function that takes a list of puzzle images and generates
        a completed puzzle
    """

    # add thumbnail to dict
    dictionary_thumb['thumbnail'] = turtle.Turtle()

    # add shape to screen
    Turtle_screen.addshape(lst[2])

    # set position of thumbnail
    dictionary_thumb['thumbnail'].ht()
    dictionary_thumb['thumbnail'].pu()
    dictionary_thumb['thumbnail'].setpos(390, 285)
    dictionary_thumb['thumbnail'].pd()
    dictionary_thumb['thumbnail'].st()

    # add thumbnail to turtle
    dictionary_thumb['thumbnail'].shape(lst[2])

    for i in range(len(lst) - 3):
        # create turtles
        dictionary_turtles[f'{i + 1}'] = turtle.Turtle()

        dictionary_turtles[f'{i + 1}'].speed(0)

        dictionary_turtles[f'{i + 1}'].ht()

        # add gif
        Turtle_screen.addshape(lst[i + 3])

        # give turtle gif shape
        dictionary_turtles[f'{i + 1}'].shape(lst[i + 3])

    # set puzzle size
    dim = lst[0]

    # set puzzle dimensions
    size = lst[1]

    # set puzzle start positon 
    x = -120

    y = -10

    counter = 1

    # places turtles based on dimensions
    for i in range(1, int(sqrt(dim) + 1)):

        for j in range(1, int(sqrt(dim) + 1)):
            dictionary_turtles[f'{counter}'].pu()

            dictionary_turtles[f'{counter}'].setpos(x, y)

            dictionary_turtles[f'{counter}'].pd()

            dictionary_turtles[f'{counter}'].st()

            # set next piece location in row
            x -= size

            counter += 1

        # set location of next row
        y += size

        x = -120

    return dictionary_turtles


def answer_key(turtles, lst):
    """
        Function that takes a dictionary
        of puzzle pieces in complete form and
        returns their positions as a list

    """

    # hold turtle positions
    answer_key = []

    for i in range(len(lst) - 3):
        # turtle x position
        x = turtles[f'{i + 1}'].xcor()

        # turtle y position
        y = turtles[f'{i + 1}'].ycor()

        # append turtle position
        answer_key.append([x, y])

    return answer_key


def shuffle_tiles(turtles, answer_key):
    """
        function that takes a dictionary of
        puzzle pieces and shuffles the puzzle pieces
    """
    # copy puzzle piece positions
    shuffle = copy.deepcopy(answer_key)

    # shuffle puzzle piece positions
    random.shuffle(shuffle)

    for i in range(len(shuffle)):
        # set piece position
        x = shuffle[i][0]

        y = shuffle[i][1]

        turtles[f'{i + 1}'].penup()

        turtles[f'{i + 1}'].setposition(x, y)

        turtles[f'{i + 1}'].pendown()

    return shuffle


def create_buttons():
    """
        function that enable game buttons
    """


    # show load button
    button_loader.penup()
    button_loader.setposition(110, -290)
    button_loader.showturtle()

    # show reset button
    button_reset.penup()
    button_reset.setposition(255, -290)
    button_reset.showturtle()

    # show quit button
    button_quit.penup()
    button_quit.setposition(400, -290)
    button_quit.showturtle()


def get_feedback(x, y):
    """
        function that takes x,y input and handles click events
        for game buttons and tile moves
    """

    if swap_tiles(x, y):

        # count moves
        with open('Text/moves.txt', 'r') as count:
            # retrieve moves
            counter = count.read()
            counter = int(counter)

        if counter > 0:

            with open('Text/moves.txt', 'w') as countdown:

                # substract move
                counter -= 1

                # clear move counter
                move_counter.clear()

                # write to screen
                move_counter.write(f'{counter}', align='left', font=('Arial', 20, 'normal'))

                # update move counter file
                countdown.write(f'{counter}')

            # if puzzle is complete
            if winner(x, y):
                # write score to leaderboard
                write_leader_board()

                # win pop-up
                win = turtle.Turtle()

                # add pop-up image
                Turtle_screen.addshape('Resources/winner.gif')

                # display winner pop-up
                win.shape('Resources/winner.gif')

                time.sleep(3)

                # close game
                Turtle_screen.bye()
        else:

            # win pop-up
            lose = turtle.Turtle()

            # add pop-up image
            Turtle_screen.addshape('Resources/lose.gif')

            # display winner pop-up
            lose.shape('Resources/lose.gif')

            time.sleep(3)

            # close game
            Turtle_screen.bye()

    # load new puzzle
    load_button(x, y)

    # show completed puzzle
    if reset_button(x, y):

        # load file with name and original number of moves
        with open('Text/players.txt', 'r') as players, open('Text/moves.txt', 'w') as countdown:
            for each in players:
                # seperate moves from name
                each = each.split(' : ')

                each[1] = each[1].strip('\n')

                # store original number of moves
                each[0] = int(each[0])

            # set original as count
            counter = int(each[0])

            # clear move counter
            move_counter.clear()

            # write to screen
            move_counter.write(f'{counter}', align='left', font=('Arial', 20, 'normal'))

            # update move counter file
            countdown.write(f'{counter}')

    # quit game
    quit_button(x, y)

    print(x, y)


def load_button(x, y):
    """
        Function that load a new puzzle when the load button is clicked

    """

    # verify if click is in range of load
    load_x = 71 <= x <= 149

    load_y = -326 <= y <= -254

    # load new puzzle 
    if load_x == True and load_y == True:

        # load puzzle files
        puzzle_images = load_images(load())
        print(puzzle_images)

        # remove last puzzle
        for key, value in dictionary_turtles.items():
            dictionary_turtles[key].hideturtle()

        # remove thumbnail  
        dictionary_thumb['thumbnail'].hideturtle()

        # create puzzle
        pieces = set_board(puzzle_images)

        with open('Text/answers.txt', 'w') as key:
            # generate answer key
            answer = answer_key(pieces, puzzle_images)

            for each in answer:
                # write answers to file
                key.write(f'{each[1]} {each[0]}\n')

        # shuffle puzzle
        shuffle = shuffle_tiles(pieces, answer)


def reset_button(x, y):
    '''Function that takes click input and
    shows a completed puzzle'''

    # set x for reset
    a = button_reset.xcor()

    # set y for reset
    b = button_reset.ycor()

    # click space for reset button
    click_zone = (x - a) ** 2 + (y - b) ** 2

    # if reset button is clicked
    if click_zone <= 40 ** 2:

        # retrieve puzzle name
        with open('Text/reset_file.txt', 'r') as puz_name:

            # assign puzzle name
            puzzle = puz_name.read()

            # load puzzle files
            puzzle_images = load_images(puzzle)

            # remove last puzzle
            for key, value in dictionary_turtles.items():
                dictionary_turtles[key].ht()

            # remove thumbnail  
            dictionary_thumb['thumbnail'].ht()

            # create puzzle
            pieces = set_board(puzzle_images)

        return True


def quit_button(x, y):
    """
        function that displays a quit pop-up message
    """

    # verify if click is in range of quit
    quit_x = 362 <= x <= 440

    quit_y = -313 <= y <= -268

    # load new puzzle 
    if quit_x == True and quit_y == True:
        # change state to quit
        game_state = 'quit'

        # init turlte for quit pop-up
        q_pop = turtle.Turtle()

        # add puzzle file quit pop-u[
        Turtle_screen.addshape('Resources/quitmsg.gif')

        # time limit
        stop = 2

        # record quit pop-up start time
        start_time = time.time()

        # make turtle file quit image
        q_pop.shape('Resources/quitmsg.gif')

        while game_state == 'quit':

            # back splash countdown timer
            elapsed = time.time() - start_time

            # timer ends
            if elapsed > stop:
                Turtle_screen.bye()


def swap_tiles(x, y):
    """
        function that takes x,y and swaps the position of the blank tile
    """

    # track blank gif         
    blank = dictionary_turtles['1']

    # read puzzle name
    with open('Text/reset_file.txt', 'r') as puz_name:

        # assign puzzle name
        puzzle = puz_name.read()

        # load puzzle files
        puzzle_images = load_images(puzzle)

        # set tile size
        size = puzzle_images[1]

        # set blank tile x
        blank_x = blank.xcor()

        # set blank tile x
        blank_y = blank.ycor()

    # if click left of blank
    if (blank_x - (size * 1.5)) < x < (blank_x + size / 2):

        if (blank_y + size / 2) > y > (blank_y - size / 2):

            for i in range(len(puzzle_images) - 3):

                # turtle x position
                swap_x = dictionary_turtles[f'{i + 1}'].xcor()

                # turtle y position
                swap_y = dictionary_turtles[f'{i + 1}'].ycor()

                # check if blank is in range of other tile
                in_x = (swap_x - size / 2) < x < (swap_x + size / 2)

                in_y = (swap_y - size / 2) < y < (swap_y + size / 2)

                # if adjacent tile then swap
                if in_y and in_x:
                    blank.penup()

                    # swap to adjacent
                    blank.setposition(swap_x, swap_y)

                    blank.pendown()

                    dictionary_turtles[f'{i + 1}'].penup()

                    # swap to blank
                    dictionary_turtles[f'{i + 1}'].setposition(blank_x, blank_y)

                    dictionary_turtles[f'{i + 1}'].pendown()

                    return True

    # if i click right of blank tile
    if (blank_x + (size * 1.5)) > x > (blank_x + size // 2):

        if (blank_y + size / 2) > y > (blank_y - size / 2):

            for i in range(len(puzzle_images) - 3):

                # turtle x position
                swap_x = dictionary_turtles[f'{i + 1}'].xcor()

                # turtle y position
                swap_y = dictionary_turtles[f'{i + 1}'].ycor()

                # check if blank is in range of other tile
                in_x = (swap_x - size / 2) < x < (swap_x + size / 2)

                in_y = (swap_y - size / 2) < y < (swap_y + size / 2)

                # if adjacent tile then swap
                if in_y and in_x:
                    blank.penup()

                    # swap to adjacent
                    blank.setpos(swap_x, swap_y)

                    blank.pendown()

                    dictionary_turtles[f'{i + 1}'].penup()

                    # swap to blank
                    dictionary_turtles[f'{i + 1}'].setposition(blank_x, blank_y)

                    dictionary_turtles[f'{i + 1}'].pendown()

                    return True

    # if i click above, same x:
    if (blank_y + (size * 1.5)) > y > (blank_y + size / 2):

        if (blank_x - size / 2) < x < (blank_x + size / 2):

            for i in range(len(puzzle_images) - 3):

                # turtle x position
                swap_x = dictionary_turtles[f'{i + 1}'].xcor()

                # turtle y position
                swap_y = dictionary_turtles[f'{i + 1}'].ycor()

                # check if blank is in range of other tile
                in_x = (swap_x - size / 2) < x < (swap_x + size / 2)

                in_y = (swap_y - size / 2) < y < (swap_y + size / 2)

                # if adjacent tile then swap
                if in_y and in_x:
                    blank.penup()

                    # swap to adjacent
                    blank.setposition(swap_x, swap_y)

                    blank.pendown()

                    dictionary_turtles[f'{i + 1}'].penup()

                    # swap to blank
                    dictionary_turtles[f'{i + 1}'].setposition(blank_x, blank_y)

                    dictionary_turtles[f'{i + 1}'].pendown()

                    return True

    # if i click below, same x:
    if (blank_y - (size * 1.5)) < y < (blank_y - size / 2):

        if (blank_x - size / 2) < x < (blank_x + size / 2):

            for i in range(len(puzzle_images) - 3):

                # turtle x position
                swap_x = dictionary_turtles[f'{i + 1}'].xcor()

                # turtle y position
                swap_y = dictionary_turtles[f'{i + 1}'].ycor()

                # check if blank is in range of other tile
                in_x = (swap_x - size / 2) < x < (swap_x + size / 2)

                in_y = (swap_y - size / 2) < y < (swap_y + size / 2)

                # if adjacent tile then swap
                if in_y and in_x:
                    blank.penup()

                    # swap to adjacent
                    blank.setposition(swap_x, swap_y)

                    blank.pendown()

                    dictionary_turtles[f'{i + 1}'].penup()

                    # swap to blank
                    dictionary_turtles[f'{i + 1}'].setposition(blank_x, blank_y)

                    dictionary_turtles[f'{i + 1}'].pendown()

                    return True


def winner(x, y):
    """
        function that  check if tiles are
        in correct order and declares win
    """

    # list to hold answer key
    answer = []

    with open('Text/reset_file.txt', 'r') as puz_name, open('Text/answers.txt', 'r') as key:

        # assign puzzle name
        puzzle = puz_name.read()

        # load puzzle files
        puzzle_images = load_images(puzzle)

        for each in key:
            # split up x and y
            each = each.split()

            each[0] = int(each[0])

            each[1] = int(each[1])

            # append coordinates to key
            answer.append(each)

    # Loop through turtles 
    for i in range(len(puzzle_images) - 3):

        # Get the current position of the turtle
        current_x = dictionary_turtles[f'{i + 1}'].xcor()

        current_y = dictionary_turtles[f'{i + 1}'].ycor()

        # Get the correct position in finished puzzle
        correct_x = answer[i][1]

        correct_y = answer[i][0]

        # Check if the current position of the turtle matches the "correct" position
        if current_x != correct_x or current_y != correct_y:
            # Return False if the positions do not match
            return False

    # Return True if all of the positions match
    return True
