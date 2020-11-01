import unittest
from game import Game

class TestGame(unittest.TestCase):
    def setUp(self):        

        self.game_1 = Game("John", "Sue", "rock", "scissors", "John")
        self.game_2 = Game("John", "Pat", "rock", "paper", "Pat")
        self.game_3 = Game("Pat", "Sue", "paper", "scissors", "Sue")
        self.game_4 = Game("Pat", "John", "paper", "rock", "Pat")
        self.game_5 = Game("Sue", "John", "scissors", "rock", "John")
        self.game_6 = Game("Sue", "Pat", "scissors", "paper", "Sue")

    def test_game_has_choice(self):
        self.assertEqual("rock", self.game_1.choice_1)