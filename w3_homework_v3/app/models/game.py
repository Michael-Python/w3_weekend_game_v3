class Game:
    
    def __init__(self, player_1, player_2, choice_1, choice_2, winner):
        self.player_1 = player_1
        self.player_2 = player_2
        self.winner = winner

    def add_to_winner_list(self, player):
        self.winner.append(player)

    def reveal_winner(self, player_1, player_2):
        if player_1.choice == "rock" and player_2.choice == "paper":
            self.winner.append(player_2)
            return player_2
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            self.winner.append(player_1)
            return player_1
        elif player_1.choice == "scissors" and player_2.choice == "rock":
            self.winner.append(player_2)
            return player_2
        elif player_1.choice == "paper" and player_2.choice == "rock":
            self.winner.append(player_1)
            return player_1
        elif player_1.choice == "paper" and player_2.choice == "scissors":
            self.winner.append(player_2)
            return player_2
        elif player_1.choice == "rock" and player_2.choice == "scissors":
            self.winner.append(player_1)
            return player_1
        else:
            None