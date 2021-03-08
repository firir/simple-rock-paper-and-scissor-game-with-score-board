import random
from IPython.display import clear_output

def user(inputp1):
    while inputp1 not in values:
        clear_output()
        inputp1=input("please select from rock, paper or scissor: ")
    return inputp1

p_score=0
c_score=0
def check_winner(a,b):
    p1_score=0
    c1_score=0
    if a==b:
        print(f" \nDraw \n Both are {player1.title()} \n No Score added")
    elif (a==1 and b==2) or (a==2 and b==1):
        if a==2:
            print(f" \nPaper beats Rock\n Player1 was: {player1.title()}\n Comp1 was: {comp1.title()}\n Player1 Wins")
            p1_score+=1
        else:
            print(f" \nPaper beats Rock \n Player1 was: {player1.title()} \n Comp1 was: {comp1.title()} \n Computer Wins")
            c1_score+=1
    elif (a==1 and b ==3) or (a==3 and b==1):
        if a==1:
            print(f" \nRock beats Scissor \n Player1 was: {player1.title()} \n Comp1 was: {comp1.title()} \n Player1 Wins")
            p1_score+=1
        else:
            print(f" \nRock beats Scissor \n Player1 was: {player1.title()} \n Comp1 was: {comp1.title()} \n Computer Wins")
            c1_score+=1
    elif (a==2 and b ==3) or (a==3 and b==2):
        if a==3:
            print(f" \nScissor beats Paper \n Player1 was: {player1.title()} \n Comp1 was: {comp1.title()} \n Player1 Wins")
            p1_score+=1
        else:
            print(f" \nScissor beats Paper \n Player1 was: {player1.title()} \n Comp1 was: {comp1.title()} \n Computer Wins")
            c1_score+=1
    else:
        pass
    return p1_score,c1_score

# welcome
clear_output()
print("Welcome to Jack En Poy")
print("Your opponent will be the computer ")
print("The Game will be best of 5")

while True:
    # shuffle
    rpslist=["rock","paper","scissor"]
    values={'rock':1,'paper':2,'scissor':3}
    random.shuffle(rpslist)

    #player input and computer input
    inputp1=input("Select rock, paper or scissor:")
    player1=user(inputp1)
    comp1=rpslist[0]

    # convert to int
    p1=values[player1]
    p2=values[comp1]

    # score
    p1_score,c1_score=check_winner(p1,p2)
    p_score+=p1_score
    c_score+=c1_score
 
    print(f"Player 1 Score: {p_score}")
    print(f"Computer Score: {c_score}\n")
      
    if p_score==3 or c_score==3:
        if p_score:
            print("Player 1 is over all Winner")
            # uncomment this if you want to add "Do you want to play again function"
            # p_score=0
            # c_score=0
            break
        else:
            print("Computer is over all Winner")
            # uncomment this if you want to add "Do you want to play again function"
            # p_score=0
            # c_score=0
            break

