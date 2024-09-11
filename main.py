
import random
import os



  



def main():
    player = 0
    house =  0
    isRunning = True

    while isRunning:
        print(isRunning)   
        player += random.randint(1,6)
        house += random.randint(1,6)
        print(f"Player has {player}")
        print(f"House has {house}")


        while True:
            if player>13:
                print("You have over 13, You lose!")
                isRunning = False
                break
                
            print(f"You have {player}, do you want to stay Y/N")
            x = input()
            if x.lower() == "y":
                print("yes")
            else:
                print("no")
                player += random.randint(1,6)


if __name__ == "__main__":
    main()