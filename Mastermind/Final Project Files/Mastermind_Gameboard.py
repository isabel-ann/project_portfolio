'''
CS 5001 
Isabel Cuddihy
Final Project - Mastermind Gameboard
12-08-2023
'''
import random
import turtle
import Constants
from Marble import Marble
from Point import Point
from Row import Row
import datetime

def error_file(error_type:str, description:str):
    '''
    Function creates error file to keep track of errors occuring during
    mastermind gameplay
    Input - error_type - specific error type if possible, or general name 
    description - brief description of the error and what likely happened
    Additional - Includes Date and Time of error in the log
    '''
    current_time = datetime.datetime.now()
    timestamp = current_time.timestamp()
    date_and_time = datetime.datetime.fromtimestamp(timestamp)
    with open("mastermind_errors.err", "a") as error_file:
        error_file.writelines(f"Type of Error {error_type} : TimeStamp: \
                              {date_and_time} : {description} \n")

def leaderboard_file():
    '''
    Function updates leaderboard file and creates leaderboard file 
    if one does not exist
    '''
    try:
        with open("leaderboard.txt", 'r') as leaderboard_file:
            player_info = {} # dictionary of player and current score
            player_reader = leaderboard_file.readlines()
            for player in player_reader:
                player_list = player.split()
                for i in range(len(player_list)):
                    player_name, player_score = player_list[i].split(",")
                    player_info[player_name] = int(player_score)
        current_player = []
        current_player_name = turtle.textinput(
            "Player Name", "What is your name? ").title() #player inputs name
        # if player already exists in leaderboard file
        if current_player_name in player_info:
            current_player = [current_player_name, 
                              player_info[current_player_name]]
        # adds new player to leaderboard with default score of 0
        else:
            player_info[current_player_name] = 0
            current_player = [current_player_name, 0] # info for current player
        leaderboard = []
        names = []
        for item in player_info:
            names.append(item)
        names.sort()
        for i in range(len(player_info)):
            leaderboard.append([player_info[names[i]], names[i] ])
        leaderboard.sort()
        # draw leaderboard on screen
        leaderboard_screen(leaderboard, 150, 300, current_player)
        
        return current_player

    except (FileNotFoundError):
        leaderboard_not_found_message()
        error_file("FileNotFoundError", "Leaderboard file was not found, a \
                   new file has been created")
        player_results = ""
        # adds new player name
        player_name = turtle.textinput(
            "Player Name", "What is your name? ").title() 
        player_results = player_name + "," + str(0)
        
        # creates leaderboard file and adds player name to file
        with open("leaderboard.txt", "w") as leaderboard_file:
            leaderboard_file.write(player_results)
        leaderboard = []
        current_player = [player_name, 0]
        leaderboard.append(current_player)
        # draws leaderboard on screen with current player and default score 0
        leaderboard_screen(leaderboard, 150, 300, current_player)
        return current_player

def confirmation_button(x:int, y:int):
    '''
    Function places confirmation button on to screen.
    '''
    turtle.addshape("checkbutton.gif")
    turtle.shape("checkbutton.gif")
    turtle.penup()
    turtle.goto(x, y)
    turtle.stamp()

def clear_button(x:int, y:int):
    '''
    Function places clear selection button on to screen.
    '''
    turtle.addshape("xbutton.gif")
    turtle.shape("xbutton.gif")
    turtle.goto(x, y)
    turtle.stamp()

def quit_button(x:int, y:int):
    '''
    Function places quit button on to screen.
    '''
    turtle.addshape("quit.gif")
    turtle.shape("quit.gif")
    turtle.goto(x, y)
    turtle.stamp()

def win_message():
    '''
    Function displays win message on screen and exits game
    '''
    turtle.home()
    turtle.addshape("winner.gif")
    turtle.shape("winner.gif")
    turtle.penup()
    turtle.stamp()
    turtle.exitonclick()

def game_over_message():
    '''
    Function displays game over message on screen and exits game
    '''
    turtle.home()
    turtle.addshape("lose.gif")
    turtle.shape("lose.gif")
    turtle.penup()
    turtle.stamp()
    turtle.exitonclick()

def leaderboard_not_found_message():
    '''
    function displays leaderboard file not found message on screen
    '''
    turtle.penup()
    turtle.goto(0, Constants.MESSAGE_Y)
    turtle.addshape("leaderboard_error.gif")
    turtle.shape("leaderboard_error.gif")

def player_force_quit():
    '''
    Function adds a mesage on error file stating the player quit the game early
    '''
    error_file("Player Force Quit Game", "Player has quit the game before" +
               " finishing, reason unknown" )
    turtle.penup()
    turtle.goto(0, Constants.MESSAGE_Y)
    turtle.addshape("quitmsg.gif")
    turtle.shape("quitmsg.gif")
    
def leaderboard_rectangle():
    '''
    Function draws leaderboard border rectangle
    '''
    turtle.goto(100, 100)
    leaderboard_poly = (Constants.LEADERBOARD_POLY_1, 
                        Constants.LEADERBOARD_POLY_2, 
                        Constants.LEADERBOARD_POLY_3, 
                        Constants.LEADERBOARD_POLY_4)
    leaderboard_rectangle = turtle.Shape("compound")     
    leaderboard_rectangle.addcomponent(leaderboard_poly, "white", "blue" )  
    turtle.register_shape("leaderboard_rectangle", leaderboard_rectangle)
    turtle.shape("leaderboard_rectangle")
    turtle.stamp()

def turn_row_rectangle():
    '''
    Function draws turn row border rectangle
    '''
    turtle.goto(-100, 100)
    turn_row_poly = (Constants.TURN_ROW_POLY_1, Constants.TURN_ROW_POLY_2, 
                     Constants.TURN_ROW_POLY_3, Constants.TURN_ROW_POLY_4)
    turn_row_rectangle = turtle.Shape("compound")     
    turn_row_rectangle.addcomponent(turn_row_poly, "white", "blue" )  
    turtle.register_shape("turn_row_rectangle", turn_row_rectangle)
    turtle.shape("turn_row_rectangle")
    turtle.stamp()

def selection_row_rectangle():
    '''
    Function draws selection border rectangle
    '''
    turtle.goto(-100, -200)
    selection_row_poly = (Constants.SELECTION_ROW_POLY_1, 
                          Constants.SELECTION_ROW_POLY_2, 
                          Constants.SELECTION_ROW_POLY_3, 
                          Constants.SELECTION_ROW_POLY_4)
    selection_row_rectangle = turtle.Shape("compound")     
    selection_row_rectangle.addcomponent(selection_row_poly, "white", "blue" )  
    turtle.register_shape("selection_row_rectangle", selection_row_rectangle)
    turtle.shape("selection_row_rectangle")
    turtle.stamp()

def leaderboard_screen(leaderboard:list, position_x:int, position_y:int,
                       current_player:list):
    '''
    Function populates the leaderboard screen based on input from the 
    leaderboard file (if available)
    '''
    # draw leaderboard
    turtle.penup()
    leaderboard_rectangle()
    turn_row_rectangle()
    selection_row_rectangle()
    turtle.hideturtle()
    turtle.goto(150,300)
    turtle.pendown()
    turtle.color("red")
    turtle.write("LEADERBOARD", font = ("Arial", 30, "bold"))
    turtle.penup()
    turtle.color("black")
    position_x = 175
    position_y = 270
    turtle.goto(position_x, position_y)

    # populate leaderboard entries
    for entry in leaderboard:
        player_listing = f"{str(entry[0])} : {entry[1]}"
        turtle.pendown()
        turtle.write(player_listing, font= ("Arial", 15, "normal"))
        turtle.penup()
        position_y -= 25
        turtle.goto(position_x, position_y)
    return current_player

def save_leaderboard_file(current_player:list):
    '''
    Function saves new game results to leaderboard file (if better than 
    previous score) or update leaderboard file with new player's info
    '''
    with open("leaderboard.txt", 'r') as leaderboard_file:
            player_info = {} # dictionary of player and current score
            player_reader = leaderboard_file.readlines()
            for player in player_reader:
                player_list = player.split()
                for i in range(len(player_list)):
                    player_name,player_score = player_list[i].split(",")
                    player_info[player_name] = int(player_score)
    if current_player[0] in player_info: 
        player_info[current_player[0]]= current_player[1]
    else:
        player_info[current_player[0]] = current_player[1]
    game_results = ""
    for item in player_info:
        game_results  += item + "," + str(player_info[item]) + "\n"
        
    with open("leaderboard.txt", "w") as leaderboard_file:
            leaderboard_file.write(game_results)

def draw_selection_marble():
    '''
    Function draws selection marbles to gameboard.
    '''
    select_red = Marble(Point(Constants.RED_X, Constants.RED_Y), "red", 
                        Constants.SELECTION_MARBLE_RADIUS)
    select_blue = Marble(Point(Constants.BLUE_X, Constants.BLUE_Y), "blue", 
                        Constants.SELECTION_MARBLE_RADIUS)
    select_green = Marble(Point(Constants.GREEN_X, Constants.GREEN_Y), "green",
                        Constants.SELECTION_MARBLE_RADIUS)
    select_yellow = Marble(Point(Constants.YELLOW_X, Constants.YELLOW_Y), 
                        "yellow", Constants.SELECTION_MARBLE_RADIUS)
    select_purple = Marble(Point(Constants.PURPLE_X, Constants.PURPLE_Y), 
                        "purple", Constants.SELECTION_MARBLE_RADIUS)
    select_black = Marble(Point(Constants.BLACK_X, Constants.BLACK_Y), 
                        "black", Constants.SELECTION_MARBLE_RADIUS)
    select_red.draw()
    select_blue.draw()
    select_green.draw()
    select_yellow.draw()
    select_purple.draw()
    select_black.draw()