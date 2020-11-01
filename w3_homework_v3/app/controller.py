from flask import render_template, request, redirect
from app import app
from app.models.game import Game
from app.models.player import Player

@app.route('/')

def index():
    return render_template('index.html')
    
@app.route('/get_result', methods=['POST'])    
def return_winner():
    username_1 = request.form['username1']
    username_2 = request.form['username2']
    selection_1 = request.form['selection1']
    selection_2 = request.form['selection2']
    player_1 = Player(player_1=username_1, choice_1=selection_1)
    player_2 = Player(player_2=username_2, choice_2=selection_2)
    gameresult = Game(player_1, player_2)
    result = gameresult.reveal_winner(player_1, player_2)
    return render_template('/', result=result)