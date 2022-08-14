import random

# imie = input("Jak masz na imię?")
# print("Cześć " + imie + ", zagrajmy w grę!")

lista = ["rock", "paper", "scissors"]

def gra(user_input):
    comp_input = random.choice(lista)

    descr = f"Computer chose: {comp_input}, you chose: {user_input}"

    cond =[user_input=="paper" and comp_input=="rock",
    user_input=="rock" and comp_input=="scissors",
    user_input=="scissors" and comp_input=="paper"]
    win = any(cond)

    result = ""
    if user_input==comp_input:
        result = "It's a draw!"
    elif win:
        result = "You win!"
    elif user_input not in lista:
        result = "You entered wrong data :( try again"
        descr = ""
    else:
        result = "You lose :(("
    
    return f"{descr} {result}"

# czygrasz = "y"
# while czygrasz=="y":
#     gra()
#     czygrasz=input("gramy dalej? y/n")
