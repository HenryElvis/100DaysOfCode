def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        
        if front_is_clear():
            move()
        else:
            turn_right()
            
    elif not right_is_clear():
        if front_is_clear():
            move()
        else:
            turn_left()