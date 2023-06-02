import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower().strip()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print( 'It\'s a tie')

    # r > s, s > p, p > r
    elif is_win(user, computer):
        print( 'You won!')

    else:
        print('You lost!')
    
    rerun=input("Do you want to try it again???? write 'y' for yes Or 'n' for no : ").lower().strip()
    
    if rerun == 'y':
        play()
    else:
        print("Bye, Come again later...")
        exit()

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

play()