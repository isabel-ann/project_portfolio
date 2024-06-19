'''
CS 5001 
Isabel Cuddihy
Final Project - Mastermind Class (Row)
12-08-2023
'''
import turtle
from Marble import Marble
from Point import Point  
import Constants
         
class Row:
    def __init__(self, row_type, starting_y = Constants.TURN_START_Y): 
        self.row_type = row_type # player's choice or hint marble
        self.starting_y = starting_y

    def row_marble(self, starting_x:int, starting_y:int, choice_color:str):
        '''
        Function draws row marbles to the gameboard screen.
        Input -  starting_x (starting x of marble),
        starting_y (current turn's starting y), choice_color(color of marble)
        Output - None -draws straight to gameboard'''
        choice = Marble(Point(starting_x, starting_y), choice_color, 15)
        choice.draw()

    def draw_hint_marbles(self,  hint_color:str, marble_number:int, 
                          starting_y:int):
        '''
        Function draws results of hint marbles to the gameboard screen.
        Input - hint_color (str) "red" (close), "white" (wrong), "black" 
        (correct), marble_number (marble the color is representing), 
        starting_y (current turn's starting y)
        Output - None -draws straight to gameboard'''
        if marble_number == 1: 
            x = Constants.START_X_HINT
            starting_y = starting_y + Constants.ROW_MARBLE_RADIUS
            hint = Marble(Point(x, starting_y), hint_color, 5)
            hint.draw()
            
        elif marble_number == 2: 
            x = Constants.START_X_HINT_2ND_COLUMN
            starting_y = starting_y + Constants.ROW_MARBLE_RADIUS
            hint = Marble(Point(x, starting_y), hint_color, 5)
            hint.draw()
        elif marble_number == 3: 
            x = Constants.START_X_HINT
            hint = Marble(Point(x, starting_y), hint_color, 5)
            hint.draw()
            
        elif marble_number  == 4: 
            x = Constants.START_X_HINT_2ND_COLUMN
            hint = Marble(Point(x, starting_y), hint_color, 5)
            hint.draw()