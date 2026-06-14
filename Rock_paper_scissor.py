import random
item_list=["Rock","Paper","Scissor"]

#.capitalize() lagaya taaki agar user 'rock' likhe toh wo apne aap 'Rock' ban jaye
user_choise= input("Enter ur move= [Rock, Paper, Scissor]:- ").capitalize()
comp_choice= random.choice(item_list)

print(f"User choice = {user_choise}, Computer choice= {comp_choice}")

if user_choise == comp_choice:
    print("Both are Tie")

elif user_choise == "Rock":
    if comp_choice== "Paper":
        print("Computer wins! Paper covers the Rock")

    else:
        print("You Win!! Rock crash the Scissor")

elif user_choise== "Paper":
    if comp_choice== "Rock":
        print("You Win!! Paper cover the Rock")
    else:
        print("Computer wins! Scissors cut the Paper")
    
elif user_choise== "Scissor":
    if comp_choice== "Rock":
        print("Computer wins! Rock crushes the Scissors")
    else:
        print("You Win!! Scissor can cut the paper")

else:
    print("iNVALID OPTION")