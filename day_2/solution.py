import numpy as np
import pandas as pd 

with open("input.txt") as input:
    data = input.readlines()

def score(them, me):
    play_points = ord(me)-87
    win_loss_points = 6-3*((ord(them)-ord(me))%3)
    return play_points + win_loss_points
    
    
def part_1(data=data.copy()):
    return sum(score(*d.split()) for d in data)

def score_part_2(them,me):
    wtl_key = (ord(me)-88)
    play_points = (3-(ord(them)-65+wtl_key))%3
    return 3*wtl_key + (3-play_points)
    
def part_2(data=data.copy()):
    return sum(score_part_2(*d.split()) for d in data)
    
print(part_1())
print(part_2())
