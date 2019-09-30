# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:52:10 2019

@author: vnedrow
"""
from towers_of_hanoi_joint import move_towers

def towers_of_hanoi(tower1, tower3, tower2, num_disks, tot_disks, START, MID, END):
    """for each disk in n- 1 disks, move disks from pillar 1 to pillar 2, 
    and then from pillar 2 to pillar3"""
    if num_disks > 0:
        new_height = num_disks - 1
        towers_of_hanoi(tower1, tower2, tower3, new_height, tot_disks, START, MID, END)
        move_towers(tower1, tower3, tot_disks, " " * tot_disks, START, MID, END)
        towers_of_hanoi(tower2, tower3, tower1, new_height, tot_disks, START, MID, END)
