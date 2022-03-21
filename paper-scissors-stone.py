import random

# STONE
choose1_even = '''
YOU _______                _______ PC 
---'   ____)              (____   '---
      (_____)            (_____)
      (_____)            (_____)
      (____)              (____)
---.__(___)                (___)__.---

                EVEN!!

'''
choose1_lose = '''
YOU _______                _____ PC
---'   ____)          ____(____   '---
      (_____)        (_______
      (_____)       (________
      (____)         (_______
---.__(___)           (__________.---

        YOU LOSE HAHAHA! 。(  ﾟ∀ﾟ)☞ 

'''
choose1_win = '''
YOU _______                 ______ PC
---'   ____)         ______(____   '---
      (_____)       (______
      (_____)      (________
      (____)             (____)
---.__(___)               (___)__.---
             
             YOU WIN!!
             
'''
# PAPER
choose2_even = '''
YOU _______                _______ PC
---'   ____)____      ____(____   '---
          ______)    (______
          _______)  (_______
         _______)    (_______
---.__________)         (_________.---

                EVEN!!

'''
choose2_lose = '''
YOU _______                ______ PC
---'   ____)____      ____(____   '---
          ______)    (______
          _______)  (_______
         _______)        (____)
---.__________)           (___)__.---

        YOU LOSE HAHAHA! 。(  ﾟ∀ﾟ)☞ 
        
'''
choose2_win = '''
YOU _______                ______ PC
---'   ____)____      ____(____   '---
          ______)    (______
          _______)  (_______
         _______)        (____)
---.__________)           (___)__.---

            YOU WIN!!
            
'''
# SCISSORS
choose3_even = '''
YOU _______                _______ PC
---'   ____)____      ____(____
          ______)    (______
       __________)  (__________
      (____)              (____)
---.__(___)                (___)__.---

                EVEN!!
                
'''
choose3_lose = '''
YOU _______                _______ PC
---'   ____)____          (____
          ______)        (____
       __________)       (_____
      (____)              (_____
---.__(___)                (______.---

                EVEN!!
                
'''
choose3_win = '''
YOU _______                _______ PC
---'   ____)____      ____(____
          ______)    (______
       __________)  (__________
      (____)         (______
---.__(___)            (__________.---

            YOU WIN!!

'''

choose1 = [choose1_even,choose1_lose,choose1_win]
choose2 = [choose2_even,choose2_lose,choose2_win]
choose3 = [choose3_even,choose3_lose,choose3_win]

GameMode = 1
GameQuestion = "\n\t\tPlease choose your guessing \n\n\t\t\t1 : stone\n\t\t\t2 : paper\n\t\t\t3 : scissors\n\t\t\t  : "
AgainGame = "\n\t\tDo you want to play again? \n\n\t\t\t0 : exit\n\t\t\t1 : again\n\t\t\t  : "
ErrorInput = "Input Error!!!"

def Game(guessing):
    result = random.randint(0, 2)
    if(guessing==1):
        print(choose1[result])
    elif(guessing==2):
        print(choose2[result])
    elif(guessing==3):
        print(choose3[result])
    else:
        print(ErrorInput)

while(GameMode):
    choose = int(input(GameQuestion))
    Game(choose)
    GameMode = int(input(AgainGame))
