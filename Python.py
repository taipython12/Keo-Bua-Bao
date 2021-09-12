from random import randint
import time

while True:
    computer = randint(0,2)

    if computer == 0:
        computer = "Đấm"
    elif computer == 1:
        computer = "Lá"
    elif computer == 2:
        computer = "Kéo"

    player = input("Mời bạn chọn: ")
    time.sleep(0.75)
    print("-"*5)
    time.sleep(0.75)
    print("Player choose: ",player)
    time.sleep(0.75)
    print("Computer choose: ",computer)
    time.sleep(0.75)
    print("-"*5)
    
    if player == computer:
        print("Draw")
    else:
        if player == "Đấm":
            if computer == "Lá":
                print("Lose")
            else:
                print("Win")
        elif player == "Lá":
            if computer == "Kéo":
                print("Lose")
            else:
                print("Win")
        elif player == "Kéo":
            if computer == "Đấm":
                print("Lose")
            else:
                print("Win")
        else:
            print("Nhập sai! Nhập lại")
    a=input("Muốn tiếp tục không>(Y/N)")
    if a == "n":
        print("Bye")
        break
    