
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
                break
            else:
                print("no")
                player += random.randint(1,6)

        while house < player:
            house += random.randint(1,6)

            if house > 13:
                print("house has over 13, you win")
                isRunning = False
                break

        print(f"House has {house}, house wins")
        isRunning = False

    
if __name__ == "__main__":
    main()