def turn_right():
    turn_left()
    turn_left()
    turn_left()
cikl = 0    
while not at_goal() :
    if right_is_clear() and cikl < 4:
        turn_right()
        move()
        cikl += 1
    elif front_is_clear():
        move()
        cikl = 0
    else:
        turn_left()
        cikl = 0