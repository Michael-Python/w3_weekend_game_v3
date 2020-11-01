import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player = Player("Sue", "scissors")
        
    def test_player_has_name(self):
        self.assertEqual("Sue", self.player.player)

    def test_player_has_choice(self):
        self.assertEqual("scissors", self.player.choice)

