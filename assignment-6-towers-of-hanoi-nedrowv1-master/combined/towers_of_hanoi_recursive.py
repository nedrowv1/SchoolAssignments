def towers_of_hanoi(tower1, tower3, tower2, num_disks, tot_disks):
    """for each disk in n- 1 disks, move disks from pillar 1 to pillar 2, 
    and then from pillar 2 to pillar3"""
    if num_disks > 0:
        new_height = num_disks - 1
        towers_of_hanoi(tower1, tower2, tower3, new_height, tot_disks)
        move_towers(tower1, tower3, tot_disks, " " * tot_disks)
        towers_of_hanoi(tower2, tower3, tower1, new_height, tot_disks)
