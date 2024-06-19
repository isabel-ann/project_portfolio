'''
   CS5001
   Isabel Cuddihy
   12-08-2023
   Final Project - Mastermind Game Test
'''
import Constants
from mastermind_game import Game
import unittest

class Game_Test(unittest.TestCase):

    # Positive Tests

    def test__init__(self):
        '''.
        Function tests constructor of Class Game
        Checks Player Color Choice, Secret Color Choice, Hint Color, 
        Marble Color, Turn Number, Marble Number, Starting Y, 
        Starting X for matching inputs
        '''
        # TEST 1 - Game Initializer
        Game_Test = Game([], [], [],  "white", ["Isabel", 0], 
                         starting_y = Constants.TURN_START_Y, 
                         starting_x = Constants.TURN_START_X, 
                         turn_number = 0, marble_number = 1)
        self.assertEqual(Game_Test.player_color_choice, [], "Wrong Sequence")
        self.assertEqual(Game_Test.secret_color_code, [], "Wrong Sequence")
        self.assertEqual(Game_Test.hint_colors, [], "Wrong Sequence")
        self.assertEqual(Game_Test.marble_color, "white", "Wrong Color")
        self.assertEqual(Game_Test.current_player, ["Isabel", 0], 
                               "Wrong Current Player")
        self.assertEqual(Game_Test.turn_number, 0, 
                               "Wrong Turn Number")
        self.assertEqual(Game_Test.marble_number, 1, 
                               "Wrong Marble Number")
        self.assertEqual(Game_Test.starting_y, 300, 
                               "Wrong Starting Y Number")
        self.assertEqual(Game_Test.starting_x, -360, 
                               "Wrong Starting X Number")
        
        # TEST 2 - Game Initalizer
        Game_Test_2 = Game([], [], [],  "black", ["Isabel", 4], 
                         starting_y = Constants.TURN_START_Y, 
                         starting_x = Constants.TURN_START_X, 
                         turn_number = 0, marble_number = 1)
        self.assertEqual(Game_Test_2.player_color_choice, [], "Wrong Sequence")
        self.assertEqual(Game_Test_2.secret_color_code, [], "Wrong Sequence")
        self.assertEqual(Game_Test_2.hint_colors, [], "Wrong Sequence")
        self.assertEqual(Game_Test_2.marble_color, "black", "Wrong Color")
        self.assertEqual(Game_Test_2.current_player, ["Isabel", 4], 
                               "Wrong Current Player")
        self.assertEqual(Game_Test_2.turn_number, 0, 
                               "Wrong Turn Number")
        self.assertEqual(Game_Test_2.marble_number, 1, 
                               "Wrong Marble Number")
        self.assertEqual(Game_Test_2.starting_y, 300, 
                               "Wrong Starting Y Number")
        self.assertEqual(Game_Test_2.starting_x, -360, 
                               "Wrong Starting X Number")


    def test_color_choice_results(self):
        '''
        Function tests color comparison between secret code and 
        player's color choice
        '''
        # TEST 3 - Mixed Results
        Game_Test_3 = Game(
            secret_color_code= ["yellow", "green", "black","purple"], 
            player_color_choice=["black", "red", "yellow", "purple"],
            hint_colors= [],  marble_color= "white", 
            current_player=["Isabel", 0], starting_y = Constants.TURN_START_Y, 
            starting_x = Constants.TURN_START_X, turn_number = 0)
        self.assertEqual(
            Game_Test_3.color_choice_results(
                Game_Test_3.secret_color_code,
                Game_Test_3.player_color_choice), 
                ["red", "white", "red", "black"], "Incorrect Hints")
        
        # TEST 4 - Mixed Results 2
        Game_Test_4 = Game(
            secret_color_code= ["red", "blue", "yellow", "green"], 
            player_color_choice=["black", "blue", "yellow", "red"],
            hint_colors= [],  marble_color= "white", 
            current_player=["Isabel", 0], starting_y = Constants.TURN_START_Y, 
            starting_x = Constants.TURN_START_X, turn_number = 0)
        self.assertEqual(
            Game_Test_4.color_choice_results(
                Game_Test_4.secret_color_code,
                Game_Test_4.player_color_choice),
                ["white", "black", "black", "red"], "Incorrect Hints")
        
        # TEST 5 - Correct Answers all in wrong place
        Game_Test_5 = Game(
            secret_color_code= ["red", "yellow", "green", "blue"], 
            player_color_choice=["blue", "red", "yellow", "green"],
            hint_colors= [],  marble_color= "white", 
            current_player=["Isabel", 0], starting_y = Constants.TURN_START_Y, 
            starting_x = Constants.TURN_START_X, turn_number = 0)
        self.assertEqual(
            Game_Test_5.color_choice_results(
                Game_Test_5.secret_color_code,
                Game_Test_5.player_color_choice),
                ["red", "red", "red", "red"], "Incorrect Hints")
        
        # TEST 6 - Correct Answer all in correct place
        Game_Test_6 = Game(
            secret_color_code= ["black", "purple", "green", "blue"], 
            player_color_choice=["black", "purple", "green", "blue"],
            hint_colors= [],  marble_color= "white", 
            current_player=["Isabel", 0], starting_y = Constants.TURN_START_Y, 
            starting_x = Constants.TURN_START_X, turn_number = 0)
        self.assertEqual(
            Game_Test_6.color_choice_results(
                Game_Test_6.secret_color_code,
                Game_Test_6.player_color_choice),
                ["black", "black", "black", "black"], "Incorrect Hints")  

def main():
    unittest.main(verbosity = 3)
if __name__ == "__main__":
    main()