'''
   CS5001
   Isabel Cuddihy
   12-08-2023
   Final Project - Mastermind Game
'''
import random
import turtle
import Constants
from Marble import Marble
from Point import Point
from Row import Row
import Mastermind_Gameboard

class Game:
    """
    Class Game contains the full process for Mastermind.
    Require import of Classes (Marble, Row, Point, PositionService) Constant 
    file and turtle."""
    def __init__(self, player_color_choice: list, secret_color_code: list,
                 hint_colors: list,  marble_color, current_player: list,
                 starting_y = Constants.TURN_START_Y, 
                 starting_x = Constants.TURN_START_X, 
                 turn_number = 0, marble_number = 1):
        """
        Constructor initializes a Game creates recyclable variables for use 
        throughout the running of the game. 
        """
        self.player_color_choice = player_color_choice
        self.secret_color_code = secret_color_code
        self.hint_colors = hint_colors
        self.marble_color = marble_color
        self.current_player = current_player
        self.starting_y = starting_y
        self.starting_x = starting_x
        self.turn_number = turn_number # increases after a turn is completed
        self.marble_number = marble_number
    
    def secret_color_code_creator (self):
        """
        Function creates the secret color code for each game.
        Output secret_color_code (list)
        Randomize a 4 color sequence for gameplay
        """
        colors = ["red", "blue", "green", "yellow", "purple", "black"]
        x = 1
        while x <= Constants.ROW_LENGTH:
            i = random.randint(0,len(colors) - 1)
            dot_color = colors[i]
            if dot_color in self.secret_color_code:
                continue
            else:
                self.secret_color_code.append(dot_color)
            x += 1
        return self.secret_color_code

    def color_choice_results(self, player_color_choice:list, 
                             secret_color_code:list) -> list:
        """
        Function check's players color choices again the secret color code and
        outputs red, black or white dots to show if the play was correct, close
        or totally wrong.
        Input - secret_color_code (list) and players_color_code (list)
        Output - None (updates the self.hint_colors attribute of
        the Game instance or if the player's choice matches the secret code,
        the game ends)
        Requirements - player_color_choice and secret_color_code - both len 4
        """
        x = 0
        while x < Constants.ROW_LENGTH:
            if self.player_color_choice[x] == self.secret_color_code[x]:
                self.hint_colors.append("black")
            elif self.player_color_choice[x] in self.secret_color_code:
                self.hint_colors.append("red")
            else:
                self.hint_colors.append("white")
            x += 1
        return self.hint_colors        

    def turn_row(self, choice_color, row_type, starting_x, starting_y):
        """
        Function draws turn choices based on player's color choices each turn
        Input - choice_color (updates with each click on selection marble),
        row_type ("selection"), starting_x (starts at marble 1 and increases to
        fill in next marble as color selections are made), starting_y
        (decreases after every turn to move down to next row).
        Output - None - """
        turn_row = Row(row_type, starting_y)
        turn_row.row_marble(starting_x, starting_y, choice_color)

    def hint_row(self,choice_color,row_type, starting_y, marble_number):
        """
        Function draws hint results based on player's choices compared to
        the secret color code. Red = correct, but in the wrong spot,
        Black = correct, White = not in secret code
        """
        turn_row = Row(row_type, starting_y)
        turn_row.draw_hint_marbles(choice_color, marble_number, starting_y)

    def gameboard_setup(self):
        """
        Function sets up the Mastermind gameboard.
        Requires Turtle_Gameboard.py file for helper functions
        and provided gifs
        """
        turtle.Screen()
        turtle.bgcolor("white")
        turtle.hideturtle()
        position_y = Constants.TURN_START_Y
        position_x = Constants.TURN_START_X
        for i in range(Constants.TOTAL_TURNS):
            for x in range(Constants.ROW_LENGTH):
                self.turn_row( "white", "selection", position_x ,position_y)
                position_x += Constants.MOVE_TURN_Y
            position_x = Constants.TURN_START_X
            position_y -= Constants.MOVE_TURN_Y
            
        position_y = Constants.TURN_START_Y

        for i in range(Constants.TOTAL_TURNS):
            for x in range(Constants.ROW_LENGTH):
                marble_number = self.marble_number
                self.hint_row("white", "hint", position_y, marble_number) 
        # position_y changes to hint_row_y to separate the changing y values
                self.marble_number += 1
            position_y -= Constants.MOVE_TURN_Y
            self.marble_number = 1
        self.secret_color_code_creator()
        Mastermind_Gameboard.draw_selection_marble()
        Mastermind_Gameboard.confirmation_button(Constants.CONFIRM_BUTTON_X, 
                                             Constants.CONFIRM_BUTTON_Y)
        Mastermind_Gameboard.clear_button(Constants.CLEAR_BUTTON_X, 
                                      Constants.CLEAR_BUTTON_Y)
        Mastermind_Gameboard.quit_button(Constants.QUIT_BUTTON_X, 
                                     Constants.QUIT_BUTTON_Y) 

    def clicker(self,x:int,y:int):
        """Function checks click area for location relative to radius of
        current drawn circle, or button
        Input - x,y value of mouse click
        Output - various - selects player colors, confirms color choices,
        resets player color choices, or quits game"""
        
        #player clicks Red
        if Constants.RED_X + Constants.SELECTION_MARBLE_RADIUS > x and \
            Constants.RED_X - Constants.SELECTION_MARBLE_RADIUS * 2 < x and \
                Constants.RED_Y + Constants.SELECTION_MARBLE_RADIUS * 2 > y \
                    and Constants.RED_Y <= y:
            if len(self.player_color_choice) < Constants.ROW_LENGTH:
                if "red" not in self.player_color_choice:
                    self.player_color_choice.append('red')
                    self.marble_color = "red"
                    self.drawing_players_choices()
        
        # player clicks Blue
        elif Constants.BLUE_X + Constants.SELECTION_MARBLE_RADIUS  > x and \
            Constants.BLUE_X - Constants.SELECTION_MARBLE_RADIUS * 2 < x and \
                Constants.BLUE_Y + Constants.SELECTION_MARBLE_RADIUS * 2 > y \
                    and Constants.BLUE_Y <= y:
            if len(self.player_color_choice) < Constants.ROW_LENGTH:
                if "blue" not in self.player_color_choice:
                    self.player_color_choice.append('blue')
                    self.marble_color = "blue"
                    self.drawing_players_choices()
        
        # player clicks Green
        elif Constants.GREEN_X + Constants.SELECTION_MARBLE_RADIUS > x and \
                Constants.GREEN_X - Constants.SELECTION_MARBLE_RADIUS * 2 < x \
                    and Constants.GREEN_Y + Constants.SELECTION_MARBLE_RADIUS \
                        * 2 > y and Constants.GREEN_Y  <= y:  
            if len(self.player_color_choice) < Constants.ROW_LENGTH:
                if "green" not in self.player_color_choice:
                    self.player_color_choice.append('green')
                    self.marble_color = "green"
                    self.drawing_players_choices()

        # player clicks Yellow
        elif Constants.YELLOW_X + Constants.SELECTION_MARBLE_RADIUS > x and \
                Constants.YELLOW_X - Constants.SELECTION_MARBLE_RADIUS \
                    * 2 < x and Constants.YELLOW_Y + \
                        Constants.SELECTION_MARBLE_RADIUS * 2 > y and \
                            Constants.YELLOW_Y <= y:  
            if len(self.player_color_choice) < Constants.ROW_LENGTH:
                if "yellow" not in self.player_color_choice:
                    self.player_color_choice.append('yellow')
                    self.marble_color = "yellow"
                    self.drawing_players_choices()

        # player clicks Purple
        elif Constants.PURPLE_X + Constants.SELECTION_MARBLE_RADIUS > x and \
                Constants.PURPLE_X - Constants.SELECTION_MARBLE_RADIUS \
                    * 2 < x and Constants.PURPLE_Y + \
                        Constants.SELECTION_MARBLE_RADIUS * 2 > y and \
                            Constants.PURPLE_Y <= y:  
            if len(self.player_color_choice) < Constants.ROW_LENGTH:
                if "purple" not in self.player_color_choice:
                    self.player_color_choice.append('purple')
                    self.marble_color = "purple"
                    self.drawing_players_choices()

        # player clicks Black
        elif Constants.BLACK_X + Constants.SELECTION_MARBLE_RADIUS > x and \
                Constants.BLACK_X - Constants.SELECTION_MARBLE_RADIUS \
                    * 2 < x and Constants.BLACK_Y + \
                        Constants.SELECTION_MARBLE_RADIUS * 2 > y and \
                            Constants.BLACK_Y <= y:  
            if len(self.player_color_choice) < Constants.ROW_LENGTH:
                if "black" not in self.player_color_choice:
                    self.player_color_choice.append("black")
                    self.marble_color = "black"
                    self.drawing_players_choices()

        # QUIT BUTTON - quits game and closes turtle window 
        # sends error to log that player quit before finishing the game
        elif Constants.QUIT_BUTTON_X + Constants.BUTTON_WIDTH > x and \
                Constants.QUIT_BUTTON_X - Constants.BUTTON_WIDTH < x and \
                    Constants.QUIT_BUTTON_Y + Constants.BUTTON_WIDTH > y and \
                        Constants.QUIT_BUTTON_Y - Constants.BUTTON_WIDTH <= y:
            Mastermind_Gameboard.player_force_quit()
            turtle.exitonclick() 

        # player clears selection choices
        elif Constants.CLEAR_BUTTON_X + Constants.BUTTON_WIDTH > x and \
                Constants.CLEAR_BUTTON_X - Constants.BUTTON_WIDTH < x and \
                    Constants.CLEAR_BUTTON_Y + Constants.BUTTON_WIDTH > y and \
                        Constants.CLEAR_BUTTON_Y - Constants.BUTTON_WIDTH <= y:
            self.player_color_choice = []
            for i in range(1, 5):
                self.marble_number = i
                self.marble_color = "white"
                self.drawing_players_choices()
            self.marble_number = 1
        
        # player confirms color choices
        elif Constants.CONFIRM_BUTTON_X + Constants.BUTTON_WIDTH > x and \
                Constants.CONFIRM_BUTTON_X - Constants.BUTTON_WIDTH < x and \
                    Constants.CONFIRM_BUTTON_Y + Constants.BUTTON_WIDTH > y \
                        and Constants.CONFIRM_BUTTON_Y - \
                            Constants.BUTTON_WIDTH <= y:
            self.player_turn() # continue turn - check choices/return results         

    def drawing_players_choices(self):
        """
        Function draws player's color choices to the current turn row
        """
        starting_y = Constants.TURN_START_Y - (Constants.MOVE_TURN_Y * 
                                                self.turn_number)
        starting_x = Constants.TURN_START_X + (Constants.MOVE_TURN_Y * 
                                                (self.marble_number - 1))
        self.turn_row(self.marble_color, "selection", 
                        starting_x, starting_y)
        self.marble_number += 1
    
    def check_for_win(self):
        """
        Function checks if player's color selction matches the secret color
        code.
        If True - save game info, display win message and exit game
        If Not a match - game continues in "player_turn" function
        """
        if self.player_color_choice == self.secret_color_code:
            if self.current_player[1] == 0 or self.current_player[1] > \
                self.turn_number:
                self.current_player[1] = (self.turn_number + 1)
                Mastermind_Gameboard.save_leaderboard_file(self.current_player)
                Mastermind_Gameboard.win_message()

            else:
                Mastermind_Gameboard.save_leaderboard_file(self.current_player)
                Mastermind_Gameboard.win_message()
        else:
            return

    def player_turn(self):
        """
        Function keeps track of number of turns a player has played and
        adjusts the y coordinate for the turn row to show the player's marble
        color choices and returns results of the player's turn to the board
        """
        # player's color choices vs secret color code
        self.color_choice_results(self.player_color_choice, 
                                  self.secret_color_code)
        self.marble_number = 1
        hint_row_y = self.starting_y
        # return results of player's color choices via hint color system
        for hint in self.hint_colors:
            self.hint_row( hint, "hint", hint_row_y, self.marble_number)
            self.marble_number += 1
        
        # check if player's selection was a win
        self.check_for_win()
        
        # continue to next turn
        self.turn_number += 1 # move to next turn / update inner attributes
        if self.turn_number < Constants.TOTAL_TURNS:
            self.starting_y = Constants.TURN_START_Y - (Constants.MOVE_TURN_Y * 
                                                        (self.turn_number))
            self.player_color_choice = []
            self.marble_number = 1
            self.hint_colors = []
            
        # if game is over, save results and exit game
        elif self.turn_number >=Constants.TOTAL_TURNS:
            if self.current_player[1] == 0:
                self.current_player[1] = Constants.TOTAL_TURNS
                Mastermind_Gameboard.save_leaderboard_file(self.current_player)
                Mastermind_Gameboard.game_over_message()
            else:
                self.current_player[1] == Constants.TOTAL_TURNS
                Mastermind_Gameboard.save_leaderboard_file(self.current_player)
                Mastermind_Gameboard.game_over_message()

def main():
    current_game = Game(
        [], [], [], "white", 
        current_player = Mastermind_Gameboard.leaderboard_file(), 
        starting_y = Constants.TURN_START_Y, 
        starting_x = Constants.TURN_START_X, 
        turn_number = 0, marble_number = 1)
    
    current_game.gameboard_setup() #setup gameboard
    turtle.onscreenclick(current_game.clicker) #launch game via clicks
    
if __name__ == "__main__":
    main()
# keeps turtle open while game is running/waiting for clicks or other input
    turtle.done() 