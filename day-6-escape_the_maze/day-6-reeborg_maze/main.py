# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while at_goal() != True:
#     if front_is_clear() != True and wall_on_right() != True:
#         turn_right()
#         move()
#     elif front_is_clear() == True and wall_on_right() != True:
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()

#     elif front_is_clear() != True and wall_on_right() == True:
#         turn_left()

## more elegant
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()

# while at_goal() != True:
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move()
#     else:
#         turn_left()