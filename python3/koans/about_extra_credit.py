#!/usr/bin/env python
# -*- coding: utf-8 -*-

# EXTRA CREDIT:
#
# Create a program that will play the Greed Game.
# Rules for the game are in GREED_RULES.TXT.
#
# You already have a DiceSet class and score function you can use.
# Write a player class and a Game class to complete the project.  This
# is a free form assignment, so approach it however you desire.

from runner.koan import *
import random

class AboutExtraCredit(Koan):
    # Write tests here. If you need extra test classes add them to the
    # test suite in runner/path_to_enlightenment.py
    def test_extra_credit_task(self):
        pass

class DiceSet:
    def __init__(self):
        self._values = None

    @property
    def values(self):
        return self._values

    def roll(self, n):
        self._values = [random.randint(1,6) for i in range(n)]
        return self._values
        
def score(dice):

    score = 0
    for number in set(dice):
        if number != 1 and number != 5 and dice.count(number)<3:
            continue

        elif number == 1:
            if dice.count(number) < 3:
                score += 100 * dice.count(number)
            else:
                score += 1000 + 100 * (dice.count(number) - 3)

        elif number == 5:
            if dice.count(number) < 3:
                score += 50 * dice.count(number)
            else:
                score += 500 + 50 * (dice.count(number) - 3)
                
        elif dice.count(number)>=3:
            score += number * 100
    return score

class Player(object):

    def __init__(self, name):
        self.score = 0
        self.name = name

    def roll_dice(self):
        dice = DiceSet()
        roll = dice.roll(5)
        self.score += score(roll)
        return self.score

class Game(object):
    
    players = []
    name_samples = ['kolya', 'petya', 'vasya']
    def start_game(self, no_of_players):
        for player in range(no_of_players):
            player_name = random.choice(self.name_samples) + str(random.randint(1,10))
            player_name = Player(player_name)
            self.players.append(player_name)
        
    def run(self):
        
        running = True
        while running:
            for player in self.players:
                player.roll_dice()
                if player.score >= 3000:
                    running = False
        self.final_tally(self.players)

    def final_tally(self, players):
        for player in players:
            print(f"Player {player.name} has a final score of {player.score}")
        
game = Game()
game.start_game(2)
game.run()

    


    

