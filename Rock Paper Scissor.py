import random

item_list = ["Rock", "Paper", "Scissor"]

while True:
    user_choice = input("Enter your move (Rock, Paper, Scissor or 'quit' to exit): ").capitalize()
    if user_choice == 'Quit':
        print("Thanks for playing!")
        break
    elif user_choice not in item_list:
        print("Invalid choice, please try again.")
        continue

    comp_choice = random.choice(item_list)
    print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

    if user_choice == comp_choice:
        print("Both chose the same: Match Tie")

    elif user_choice == "Rock":
        if comp_choice == "Paper":
            print("Paper covers Rock = Computer Win")
        else:
            print("Rock smashes Scissor = You win")

    elif user_choice == "Paper":
        if comp_choice == "Scissor":
            print("Scissor cuts Paper = Computer Win")
        else:
            print("Paper covers Rock = You win")

    elif user_choice == "Scissor":
        if comp_choice == "Rock":
            print("Rock smashes Scissor = Computer Win")
        else:
            print("Scissor cuts Paper = You win")
