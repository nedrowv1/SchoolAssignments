from time import sleep
from textwrap import wrap

def move_disk(disk1, disk2, pillar1, pillar2, start_hgt, air):
    """determine if, and in what direction, a disk can move"""
    if (disk1 < disk2 or disk2 == 0) and disk1 != 0:
        move_towers(pillar1, pillar2, start_hgt, air)
    elif (disk2 < disk1 or disk1 == 0) and disk2 != 0:
        move_towers(pillar2, pillar1, start_hgt, air)
        
def towers_of_hanoi(start_hgt, mod1, strt, mid, end):
    """iterative method of moving the towers of hanoi.  won't hit
    recursion max with high numbers....but will still take 500 billion
    years at one second per disk :)"""
    tot_moves = (2 ** start_hgt) - 1  # so big...so fast
    moves = 0
    mod2 = 3 - mod1  # the pillar for the second and all even numbered moves
    disk_a = disk_b = disk_c = 0
    air = start_hgt * " "
    while moves <= tot_moves:
        a = b= c= False
        for disk in strt:
            if disk != air:
                disk_a = len(disk)
                a = True
                break
        if not a: disk_a = 0
        for disk in mid:
            if disk != air:
                disk_b = len(disk)
                b = True
                break
        if not b: disk_b = 0
        for disk in end:
            if disk != air:
                disk_c = len(disk)
                c = True
                break
        if not c: disk_c = 0
        if moves % 3 == mod1:
            move_disk(disk_a, disk_b, 1, 2, start_hgt, air)

        elif moves % 3 == mod2:
            move_disk(disk_a, disk_c, 1, 3, start_hgt, air)

        else:
            move_disk(disk_b, disk_c, 2, 3, start_hgt, air)

        moves += 1
