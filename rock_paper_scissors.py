import random

def play():
    user_points = 0
    comp_points = 0

    while user_points < 3 and comp_points < 3:

        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
        comp = random.choice(['r','p','s'])
        print("Computer's choice:",comp)

        if user==comp:
            pass
        elif is_win(user,comp):
            user_points += 1
        else:
            comp_points += 1

        print("Your points =",user_points,"\nComp points =",comp_points)

    if user_points==3:
        print("You won!")
    elif comp_points==3:
        print("You lost!")

def is_win(player,opponent):
    if (player=='p' and opponent=='r') or (player=='s' and opponent=='p') or (player=='r' and opponent=='s'):
        return True

play()