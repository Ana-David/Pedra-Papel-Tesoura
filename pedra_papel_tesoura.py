import random

user_wins = 0
computer_wins = 0

options = ["pedra", "papel", "tesoura"]


while True:
    user_input = input("Pedra, Papel ou Tesoura ou D para desistir?:  ").lower()
    if user_input =="d":
       break

    if user_input not in options:
       continue

    random_number = random.randint(0,2)
    # Pedra:0, Papel:1, tesoura:2
    computer_pick = options[random_number]
    print("O computador escolheu", computer_pick + ".")

    if user_input == "pedra" and computer_pick == "tesoura":
       print("Ganhaste!")
       user_wins += 1
       

    elif user_input == "papel" and computer_pick == "pedra":
       print("Ganhaste!")
       user_wins += 1
       

    elif user_input == "tesoura" and computer_pick == "papel":
       print("Ganhaste!")
       user_wins += 1

    else:
       print("Perdeste!!")
       computer_wins += 1
      

print("Ganhaste", user_wins,) 
print ("O computador ganhou",computer_wins)  

print("Adeus!")



       
       