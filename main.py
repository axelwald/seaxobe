
import random
import os

from playsound import playsound



  


player = 0
house =  0
isRunning = True



while isRunning:

        print(isRunning)   
        # playsound("sounds/dice_roll.mp3")
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

        if player <= 13:
            while house < player:
                house += random.randint(1,6)

                if house > 13 :
                            
                    print("house has over 13, you win")
                    playsound("sounds/yippie.mp3")
                    isRunning = False
                    break
            if house <= 13:
                print(f"House has {house}, house wins")
                playsound("sounds/trombone.mp3")

        
        isRunning = False

    
