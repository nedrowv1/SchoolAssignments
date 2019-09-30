from time import sleep
from textwrap import wrap


def define_pillar_row(pillar, disk_index, ttl_disks, endchar):
    """calculate the amount of white space needed to keep rows aligned"""
    if len(pillar) > disk_index:
        buffer = " " * (ttl_disks - len(pillar[disk_index]))
        print_disk = pillar[disk_index]  + buffer
    else:
        print_disk = ' ' * ttl_disks
    print(print_disk, end=endchar)


def print_pillar(disks, pillar_1, pillar_2, pillar_3):
    """print disk movement to screen"""
    for disk in range(disks):
        define_pillar_row(pillar_1, disk, disks, "|")
        define_pillar_row(pillar_2, disk, disks, "|")
        define_pillar_row(pillar_3, disk, disks, "\n")
    print("_" * (disks * 3))
    sleep(3)


def move_towers(key_1, key_2, strt_disks, air):
    """inserts, pops and prints the movement of the top disk of a given pillar
    to the top of another"""
    # global variable used for manipulation of lists - because otherwise
    # very strange things happened :/
    global START
    global MID
    global END

    if key_1 == 1:
        move_tower = START
    elif key_1 == 2:
        move_tower = MID
    elif key_1 == 3:
        move_tower = END
    else:
        raise ValueError("The value passed in key_1 is invalid")

    if key_2 == 1:
        drop_tower = START
    elif key_2 == 2:
        drop_tower = MID
    elif key_2 == 3:
        drop_tower = END
    else:
        raise ValueError("The value passed in key_2 is invalid")
    # move first item from move from tower and put in first place of drop to tower
    for i, value in enumerate(move_tower):
        if value != air:
            move_disk = value
            move_tower[i] = air
            break
    for i, value in enumerate(drop_tower):
        if value != air:
            drop_tower[i-1] = move_disk
            break
        elif i == len(drop_tower) -1:
            drop_tower[i] = move_disk
            break           
                    
    print_pillar(strt_disks, START, MID, END)

