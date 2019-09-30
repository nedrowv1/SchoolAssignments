"""
Created October 02 2018

Author: Nedrow, Vanessa
"""
from time import sleep
from textwrap import wrap


def define_pillar_row(pillar, disk_index, ttl_disks, endchar):
    """calculate the amount of white space needed to keep rows aligned"""
    if len(pillar) > disk_index:
        buffer = " " * (ttl_disks - len(pillar[disk_index]))
        print_disk = pillar[disk_index] + buffer
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


def move_towers(key_1, key_2, strt_disks):
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
        raise ValueError("The value passed in key_1 was improperly defined")

    if key_2 == 1:
        drop_tower = START
    elif key_2 == 2:
        drop_tower = MID
    elif key_2 == 3:
        drop_tower = END
    else:
        raise ValueError("The value passed in key_2 was improperly defined")
    # move first item from move from tower and put in first place of drop to tower
    drop_tower.insert(0, move_tower.pop(0))
    print_pillar(strt_disks, START, MID, END)


def towers_of_hanoi(tower1, tower3, tower2, num_disks, tot_disks):
    """for each disk in n- 1 disks, move disks from pillar 1 to pillar 2, 
    and then from pillar 2 to pillar3"""
    if num_disks > 0:
        new_height = num_disks - 1
        towers_of_hanoi(tower1, tower2, tower3, new_height, tot_disks)
        move_towers(tower1, tower3, tot_disks)
        towers_of_hanoi(tower2, tower3, tower1, new_height, tot_disks)


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
      r"                              --programmed recursively"
      "\n")
sleep(2)

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
sleep(10)
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
sleep(6)
INTRO = wrap("I don't suggest you try 64 disks here.  It'll take three times "
             "as long.  But try out a smaller number, and see if you can "
             "guess the next move!")
for line in INTRO:
    print(line)
sleep(2)
START_HEIGHT = int(input("Enter the height of your tower\n>>>"))
if START_HEIGHT == 64:
    print("Don't say I didn't warn you!")
START = []
MID = []
END = []
STOP_TIME=((2**START_HEIGHT)-1)*3
STOP_VALUE = "seconds"
if STOP_TIME >= 60:
    STOP_TIME = STOP_TIME//60
    STOP_VALUE="minutes"
if STOP_VALUE == "minutes" and STOP_TIME >= 60:
    STOP_TIME = STOP_TIME//60
    STOP_VALUE = "hours"
if STOP_VALUE == "hours" and STOP_TIME >= 24:
    STOP_VALUE = "days"
    STOP_TIME=STOP_TIME//24
if STOP_VALUE == "days" and STOP_TIME >= 365:
    STOP_TIME = STOP_TIME//365
    STOP_VALUE = "years"

print("This will take {:,} moves and "
      "about {:,} {:<7s}".format((2**START_HEIGHT)-1, STOP_TIME, STOP_VALUE))

sleep(3)
print("Starting in 3...")
sleep(3)
print("2...")
sleep(2)
print("1...")
sleep(1)

# populate first list with discs
for CREATE_DISK in range(START_HEIGHT):
    START.append((CREATE_DISK + 1) * '-')

# print starting sequence to screen
for DISK in range(START_HEIGHT):
    FILLER = " " * (START_HEIGHT - len(START[DISK]))
    print(START[DISK] + FILLER + "|" + " " * START_HEIGHT + "|")
print("_" * START_HEIGHT * 3)
sleep(3)


towers_of_hanoi(1, 3, 2, START_HEIGHT, START_HEIGHT)
