import random

options = ["rock", "paper", "scissors"]
enemy_win=0
player_win=0
ties=0
run = True
while run:
    enemy_move = random.choice(options)
    player_move = input("pick: rock (r), paper (p), scissors (s) ")
    if player_move == "r":
        player_move = "rock"
    elif player_move == "p":
        player_move = "paper"
    elif player_move == "s":
        player_move = "scissors"

    if enemy_move == player_move:
        print(enemy_move + " vs " + player_move)
        print("tie")
        ties += 1
    # player won
    elif enemy_move == "rock" and player_move == "paper":
        print("\n"+ enemy_move + " vs " + player_move)
        print("you won")
        player_win += 1
    elif enemy_move == "paper" and player_move == "scissors":
        print("\n"+ enemy_move + " vs " + player_move)
        print("you won")
        player_win += 1
    elif enemy_move == "scissors" and player_move == "rock":
        print("\n"+ enemy_move + " vs " + player_move)
        print("you won")
        player_win += 1
    # enemy won
    elif enemy_move == "paper" and player_move == "rock":
        print("\n"+ enemy_move + " vs " + player_move)
        print("enemy won")
        enemy_win = +1
    elif enemy_move == "scissors" and player_move == "paper":
        print("\n"+ enemy_move + " vs " + player_move)
        print("enemy won")
        enemy_win = +1
    elif enemy_move == "rock" and player_move == "scissors":
        print("\n"+ enemy_move + " vs " + player_move)
        print("enemy won")
        enemy_win = +1

    spelet = input("if you don't want to play type no (n): ")
    if spelet == "yes" or spelet == "y":
        run = False
    else:
        continue

print("enemys won: ", enemy_win)
print("player won: ", player_win)
print("ties: ", ties)
print("\nThanks you for playing!")