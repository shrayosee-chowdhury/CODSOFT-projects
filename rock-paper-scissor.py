# Rock-Paper-Scissors Game
# User Input: Prompt the user to choose rock, paper, or scissors.
# Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
# Game Logic: Determine the winner based on the user's choice and the computer's choice.
# Rock beats scissors, scissors beat paper, and paper beats rock.
# Display Result: Show the user's choice and the computer's choice.
# Display the result, whether the user wins, loses, or it's a tie.
# Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
# Play Again: Ask the user if they want to play another round.
# User Interface: Design a user-friendly interface with clear instructions and feedback.

from random import randint

t = ["ROCK", "PAPER", "SCISSOR"]

player = False

while player == False:
   
 # Randomizing computer's choice each round
    computer = t[randint(0, 2)]
    
    player = input("Choose ROCK, PAPER, or SCISSOR: ").upper()
    
    if player not in t:
        print("Invalid choice! Please choose ROCK, PAPER, or SCISSOR.")
        player = False  
        continue

    # Check for a tie
    if player == computer:
        print(f"It's a tie! Both choose {player}")
    
    # Check for ROCK logic
    elif player == "ROCK":
        if computer == "PAPER":
            print(f"You lose! {computer} covers {player}")
        else:
            print(f"You win! {player} smashes {computer}")
    
    # Check for PAPER logic
    elif player == "PAPER":
        if computer == "SCISSOR":
            print(f"You lose! {computer} cuts {player}")
        else:
            print(f"You win! {player} covers {computer}")
    
    # Check for SCISSOR logic
    elif player == "SCISSOR":
        if computer == "ROCK":
            print(f"You lose! {computer} smashes {player}")
        else:
            print(f"You win! {player} cuts {computer}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        player = False  
    else:
        print("Thanks for playing!")
        break



