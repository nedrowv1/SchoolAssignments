"""
Created October 05 2018

Author: Nedrow, Vanessa
"""
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


print(r"______________________________________________________________"
      "\n"
      r"                                                            "
      "\n"
      r" ___________                                   __"
      "\n"
      r"      |                                       /  \ "
      "\n"
      r"      |                                       |"
      "\n"
      r"      |     _          _   __   _        _   _|__"
      "\n"
      r"      |    / \ \    / |_| |    |_       / \   |"
      "\n"
      r"      |    \_/  \/\/  |_  |     _|      \_/   |"
      "\n"
      r"                                    _______    __________"
      "\n"
      r" |    |       /\         |\     |  /       \       |"
      "\n"
      r" |    |      /  \        | \    |  |       |       |"
      "\n"
      r" |____|     /    \       |  \   |  |       |       |"
      "\n"
      r" |    |    /______\      |   \  |  |       |       |"
      "\n"
      r" |    |   /        \     |    \ |  |       |       |"
      "\n"
      r" |    |  /          \    |     \|  \_______/  _____|____"
      "\n"
      r"_______________________________________________________________"
      "\n"
      r"                              --programmed iteratively"
      "\n")
#sleep(2)

QUOTE = wrap("It's been very lonely here at the monastery since the monks all "
             "left. Today, I went to the neglected Tower of Hanoi. I was "
             "about to start playing when I noticed the edge of a panel "
             "sticking out from under one of the towers. I moved the Tower, "
             "uncovering a button and a sign that said, 'In case of "
             "emergency, push to end the world.' 'Wow,' I thought. 'It's "
             "been right there the whole time.'")

for line in QUOTE:
    print(line)
print("\n--Anonymous, Demon Magazine")
#sleep(10)
print()
print()
MOVES_TO_END_OF_WORLD = (2 ** 64) - 1
TIME_TO_END_OF_WORLD = MOVES_TO_END_OF_WORLD//(3.2*(10**7))

INTRO = wrap("Legend says that when the monks in Tibet finish moving 64 "
             "golden disks from one tower to another, never placing a larger "
             "disk atop a smaller, and having only one pillar in reserve, the "
             "world will end.  Thankfully, this takes {:,} moves or just "
             "over {:,} years, at one a second, so we have some "
             "time.".format(MOVES_TO_END_OF_WORLD, TIME_TO_END_OF_WORLD))
for line in INTRO:
    print(line)
print()
#sleep(6)
INTRO = wrap("I don't suggest you try 64 disks here.  It'll take three times "
             "as long.  But try out a smaller number, and see if you can "
             "guess the next move!")
for line in INTRO:
    print(line)
#sleep(2)
START_HEIGHT = int(input("Enter the height of your tower\n>>>"))
if START_HEIGHT == 64:
    print("Don't say I didn't warn you!")
START = []
MID = []
END = []
STOP_TIME = ((2**START_HEIGHT)-1)*3
STOP_VALUE = "seconds"
if STOP_TIME >= 60:
    STOP_TIME = STOP_TIME//60
    STOP_VALUE = "minutes"
if STOP_VALUE == "minutes" and STOP_TIME >= 60:
    STOP_TIME = STOP_TIME//60
    STOP_VALUE = "hours"
if STOP_VALUE == "hours" and STOP_TIME >= 24:
    STOP_VALUE = "days"
    STOP_TIME = STOP_TIME//24
if STOP_VALUE == "days" and STOP_TIME >= 365:
    STOP_TIME = STOP_TIME//365
    STOP_VALUE = "years"

print("This will take {:,} moves and "
      "about {:,} {:<7s}".format((2**START_HEIGHT)-1, STOP_TIME, STOP_VALUE))

#sleep(3)
print("Starting in 3...")
#sleep(3)
print("2...")
#sleep(2)
print("1...")
#sleep(1)

# populate first list with discs
for CREATE_DISK in range(START_HEIGHT):
    START.append((CREATE_DISK + 1) * '-')
    MID.append(START_HEIGHT * ' ')
    END.append(START_HEIGHT * ' ')  
# print starting sequence to screen
for DISK in range(START_HEIGHT):
    FILLER = " " * (START_HEIGHT - len(START[DISK]))
    print(START[DISK] + FILLER + "|" + " " * START_HEIGHT + "|")
print("_" * START_HEIGHT * 3)
sleep(3)

if START_HEIGHT % 2 == 0:  # towers with an even number of disks start on tower 2
    MOD3_1 = 1  # moves with remainder 1 when divided by 3

else:  # towers with an odd number of disks start on tower 3
    MOD3_1 = 2  # see above


towers_of_hanoi(START_HEIGHT, MOD3_1, START, MID, END)

# Great solutions. I'm somewhat surprised you did not have the towers starting
# from the bottom of the grid. Wouldn't be hard to fill a queue with empty
# strings and then pop one as you append a disk. Would you have been able to
# reduce your codebase by importing functions from one file into the other?

