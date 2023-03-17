# LOGIC TIME! EYY
# Game
###### instance attributes:
### guild_id or whatever (server id?) -- maybe not, it will be stored outside? not sure
### is_game_running : or existence of this Game object proves this
### is_round_running: bool
### challenger: Member
### listing: scraped object -- no need!
### listPrice: float
### guesses: dict[Member, float]
### points: dict[Member, int]
###     or players: dict[key = Member, value= list[score: int, currentGuess: float]]
###     keep it in 2 dicts i think
###
###### methods
### init (start a game)
### start a round
### submit a guess
###     NOT THIS    - players[message.author][currGuess] = players.get(message.author,{score: 0, currGuess: None})[currGuess]
###     players[message.author] = players[message.author] | {currGuess: givenGuess}
### end a roundound
###     - loop through guesses
###         - see who got the closest 
###             - guess could be None or a float
###             - do running tally of distance + members who guessed that
###             - closestGuess: float, bestGuessers: list[Member]
###         - delete the currentGuess as you iterate or make it None
###         - declare winners and say sorry to everyone else...
###         - add +1 to points of winners!
### end the game
###     - loop through players
###         - find highest score and declare winner!
###     - delete the instance (probably will be done in bot.py)
###### game flow
### start a game
### start a round -- give price to guess. designate quizmaster
### in round: players (not quizmaster) submit guesses
### in round: players can re-guess, will replace guess
### end the round: display who got it closest and give them a point
### end game: show highest score and peace out

from discord import Member

class Game():
    def __init__(self):
        # self.is_game_running: bool = True 
        # ^^ not needed, existence of this object implies game is running
        self.points = {}

    def start_round(self, challenger, listPrice):
        self.round = Round(challenger, listPrice)

    def end_round(self):
        winner: list = self.round.get_round_winners()
        self.round = None
        # (so that python cleans it up)
        return winner

    def end_game(self):
        pass
        # nuke this game object from bot.py!!


class Round():
    def __init__(self, challenger, listPrice): #same as starting a round
        self.challenger = challenger #Member obj
        self.listPrice: float = listPrice
        self.guesses = {}
    
    def submit_guess(self, guesser: Member, guess: float):
        pass
        # self.guesses =  {guesser: guess}

    def get_round_winners(self) -> list[Member]:
        pass
        # go through
