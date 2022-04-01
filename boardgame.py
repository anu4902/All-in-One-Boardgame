from random import randint,choice
from time import sleep
import cv2
import turtle

PLAYER=0
COMP=1
playerpos=0
comppos=0
fourpiccnt=0
hist=[] 
funcs=[0,1,2,3,4,5]
def dispimg(img):
    
    img=cv2.imread(img)
    img=cv2.resize(img,(500,500))
    cv2.imshow('',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

def rolldice():
    num=randint(1,3)
    return num

def rps(p):
    l=["ROCK","PAPER","SCISSORS"]
    
    if p==PLAYER:
        print("\n\t\tLET'S PLAY ** ROCK PAPER SCISSORS !!!! **")
        
        ch=input("Choose Rock|Paper|scissors --> ").upper()
       
        while (ch not in l):
            ch=input("INVALID INPUT!!Choose Rock|Paper|Scissors").upper()
            
        print("\nROCK...")
        sleep(2)
        print("PAPER...")
        sleep(2)
        print("SCISSORS...")
        sleep(2)
   
        print("\nYour choice is : ",ch)
   
        compch=randint(1,3)

   
        if (compch==1):
            compchn="ROCK"
        elif (compch==2):
            compchn="PAPER"
        else:
            compchn="SCISSORS"
       
        print("The computer's choice is : ",compchn)
     
        print("\n\n" + ch + "  " + "VS" + "  " + compchn)
     
        if((ch=="ROCK" and compchn=="PAPER") or (ch=="PAPER" and compchn=="ROCK")):
             print("\nPAPER WINS!!",end=" ")
             win="PAPER"
        elif((ch=="ROCK" and compchn=="SCISSORS") or (ch=="SCISSORS" and compchn=="ROCK")):
            print("\nROCK WINS!!",end=" ")
            win="ROCK"
        elif((ch=="PAPER" and compchn=="SCISSORS") or (ch=="SCISSORS" and compchn=="PAPER")):
            print("\nSCISSORS WIN",end=" ")
            win="SCISSORS"
        else:
            print("\nIT'S A TIE!!!")
            return 1
   
        if win==ch:
            print("\n\t\t**--YOU WIN !! --**")
            return 'w'
        else:
            print("\n\t\t**--COMPUTER WINS--**")
            return 'l'
         
    elif p==COMP:
        
        print("\n\t\tCOMPUTER PLAYS ROCK PAPER SCISSORS!\n")
        
        print("ROCK...")
        sleep(2)
        print("PAPER...")
        sleep(2)
        print("SCISSORS...")
        sleep(2)
        
        compch1=l[randint(1,3)-1]
        print("\nThe computer's choice is : ",compch1)
        
        compch2=l[randint(1,3)-1]
        print("The opponent's choice is : ",compch2)
        
        print("\n\n" + compch1 + "  " + "VS" + "  " + compch2)
        
        if compch1==compch2:
            print("IT'S A TIE!!!")
            print("\n\t\t**--COMPUTER LOSES--**")
            return 'l'
        
        if (compch1=="ROCK" and compch2=="PAPER") or (compch1=="PAPER" and compch2=="SCISSORS") or (compch1=="SCISSORS" and compch2=="ROCK"):
            print("\n\t\t**--COMPUTER LOSES--**")
            return 'l'
        
        if (compch2=="ROCK" and compch1=="PAPER") or (compch2=="PAPER" and compch1=="SCISSORS") or (compch2=="SCISSORS" and compch1=="ROCK"):
            print("\n\t\t**--COMPUTER WINS--**")
            return 'w'
       

def oddeven(p):
    
        if p==PLAYER:
            
            print("\nWelcome player!!!")
            print("U made it to the odd-even game")
            print("\nRules are simple :)")
            sleep(2)
            print("\n->U get 3 chances and ur opponent is the computer")
            sleep(2)
            print("\n->Choose odd/even")
            sleep(2)
            print("\n->The sum of the choices of both opponents are calculated in each round and is then checked for odd/even")
            print("Depending on which the winner is decided")
            
            print("\nLets begin!!")
        
            count=0
            compwin=0
        
            for i in range(3):
                
                print("\n\nRound : ",i+1)
                ch=input("Choose ODD/EVEN : ").upper()
            
                val=randint(0,5)
        
                n=int(input("Enter a number: "))
                print("Computer choice : ",val)
        
                sum=val+n
        
                if ch=="ODD":
                    if sum%2!=0:
                        count=count+1
                        print("\nU win this round!")
                    
                    else:
                        print("\nU lost this one..")
                        compwin=compwin+1
                
                elif ch=="EVEN":
                    if sum%2==0:
                        count=count+1
                        print("U win this round")
                
                    else:
                        print("U lost this one")
                        compwin=compwin+1
                
                if count==2:
                    print("")
                    print("\t\t:) U WON THE GAME !!!! :)")
                    return 1
    
                if compwin==2:
                    print("")
                    print("\t\tOOPS... U LOST THE GAME...")
                    return 0
            
        if p==COMP:
            print("\n\t\tComputer plays the *** ODD/EVEN GAME ***")
            pairity=choice(['odd','even'])
            print("\nPairity choice:",pairity)
        
            print('.')
            sleep(1)
            print('.')
            sleep(1)
            print('.')
        
            first=randint(1,5)
            second=randint(1,5)
        
            print("\nComp:",first,"\nOpponent:",second)
        
            if pairity=='odd':
                if (first+second)%2==1:
                    print("\n\t\t**--COMPUTER WINS--**")
                    return 1
                else:
                    print("\n\t\t**--COMPUTER LOSES--**")
                    return 0
        
            if pairity=='even':
                if (first+second)%2==0:
                    print("\n\t\t**--COMPUTER WINS--**")
                    return 1
                else:
                    print("\n\t\t**--COMPUTER LOSES--**")
                    return 0
        

def numguess(p):
    
    if(p==PLAYER):
        
        print("\n\t\tLet's play NUMBGER GUESS !!!\n")
        
        print("\nGuess a number from 1 to 100..\n\n")
        
        n=randint(1,100)
        count=1
        guess_chances=10
        
        while 1<=guess_chances:
            
            num =int(eval(input("\nGuess the Number : ")))
            
            if num >n:
                print("\nYour guess was high : Guess a smaller number.")
            elif num <n:
                print("\nYour guess was low : Guess a higher number.")
            else:
                print("\n\n\t\tYOU WIN!!")
                return 1
            
            guess_chances-=1
            print("\nGuesses Left :",guess_chances)
            count+=1
            
        print("\nGame Over..")
        print("\n\nNumber is",n)
        return 0
    
    elif p==COMP:
        
        start,end=(1,100)
        
        print("\n\t\tComputer plays ***NUMBER GUESS***")
        print('\nComputer gets 10 chances to get the correct num.\n')
        
        n=randint(1,100)
        
        for i in range(10):
            sleep(2)
            guess=randint(start,end)
            print("\nGuess",i+1,end='')
            
            if guess==n:
                print("\nComputer's guess:",guess,"-> CORRECT ")
                print("\n\t\t**--COMPUTER WINS--**")
                return 1
            
            elif guess<n:
                start=guess+1
                print("\nComputer's guess:",guess,"-> WRONG (LOW)")
            
            else:
                end=guess-1
                print("\nComputer's guess:",guess,"-> WRONG (HIGH)")
        
        print("\nGame Over..")
        print("\nNumber is",n)
        print("\n\t\t**--COMPUTER LOSES--**")
       
        return 0       
def error_1(t):
  t.left(90)
  t.forward(200)
  t.right(90)
def error_2(t):
  t.forward(50)
  t.right(90)
def error_3(t) :
  t.forward(50)
  t.right(90)
def error_4(t):
  r=20
  t.circle(r)
  t.penup()
  t.left(90)
  t.forward(40)
def error_5(t):
  t.pendown()
  t.forward(20)
def error_6(t):
  t.right(45)
  t.forward(20)
  t.penup()
  t.backward(20)
  t.left(45)
  t.left(45)
def error_7(t):
  t.pendown()
  t.forward(20)
  t.backward(20)
  t.left(45)
  t.right(90)
def error_8(t):
  t.forward(40)
def error_9(t):
  t.right(45)
  t.forward(20)
  t.penup()
  t.backward(20)
  t.left(45)
  t.left(45)
def error_10(t):
  t.pendown()
  t.forward(20)
  t.backward(20)
  t.left(45)
  t.right(90)    

def hangman(p,t):

    words=["oxygen","microwave",'rainbow','reverse','board','geeks',"cobweb","dentist","director","axiom"]

    if p==PLAYER:
        print("\n\t\tLet's play ** HANGMAN **")
     
        word=choice(words)
        
        print("\nYou totally have 10 chances to guess the correct word.\n")
        
        print("\nGuess the characters:")
        guesses=[]
        turns=10
        
        while turns>0:
            failed=0
            for char in word:
                
                if char in guesses:
                    print(char," ",end='')
                    
                else:
                    print("_ ",end='')
                    failed+=1
        
            if failed==0:
                print("\n\nYESS!! The word is:",word)
                print("\n\t\t\t** YOU WIN THE HANGMAN GAME !! **")
                return 1
            
            print("\n\nUsed characters:",guesses)
            guess=input("\nGuess a character: ")
            
            if guess not in guesses:
                guesses.append(guess)
            else:
                print("\nYou already guessed '",guess,"' !\n")
                
            if guess not in word:
                if turns==10:
                    error_1(t)
                elif turns==9:
                    error_2(t)
                elif turns==8:
                    error_3(t)
                elif turns==7:
                    error_4(t)
                elif turns==6:
                    error_5(t)
                elif turns==5:
                    error_6(t)
                elif turns==4:
                    error_7(t)
                elif turns==3:
                    error_8(t)
                elif turns==2:
                    error_9(t)
                elif turns==1:
                    error_10(t)
                
                turns-=1
                print("Wrong")
                print("\nYou have",turns,"more guesses")
                
                
            if turns==0:
                print("\n\t\t** Hangman Game Over..You Lose **")
                return 0
                
    elif p==COMP:
        
        print("\n\t\t\tComputer plays *** HANGMAN ***")
        hangcomp=rolldice()==rolldice()
        
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        
        print("\nThe word was '",choice(words),"'\n")
        
        if hangcomp:
            print("\n\t\t**--COMPUTER WINS--**")
            return 1
        
        else:
            print("\n\t\t**--COMPUTER LOSES--**")
            return 0

def twodie(p):
    
    if p==PLAYER:
        print("\n\t\tLet's play the *** TWO DIE GAME ***")
        sleep(1)
        print("\nRoll two die | Get same number on both to win!\n")
        sleep(1)
        
        input("Press ENTER to rolldie: ")
        num1=rolldice()
        sleep(1)
        print("Dice 1:",num1)

        input("Press ENTER to rolldie: ")
        num2=rolldice()
        sleep(1)
        print("Dice 2:",num2)
        
        sleep(1)
        if num1==num2:
            print("\n\t\t**--YOU WIN !! --**")
            return 1
        elif num1!=num2:
            print("\n\t\t** You Lose **")
            return 0
    
    elif p==COMP:
        print("\n\t\tComputer plays the *** TWO DIE GAME ***")
        
        num1=rolldice()
        sleep(1)
        print("\nDice 1:",num1)
        num2=rolldice()
        sleep(1)
        print("\nDice 2:",num2)
        
        sleep(1)
        if num1==num2:
            print("\n\t\t**--COMPUTER WINS--**")
            return 1
        elif num1!=num2:
            print("\n\t\t**--COMPUTER LOSES--**")
            return 0
    
def fourpic(p):
     if p==PLAYER:
        
        print("\n\t\tLet's play *** FOUR PIC ONE WORD ***\n\n")
        sleep(2)
        print("->Four pics will be displayed\n->Guess the word which is common in all the four.\n")
        print("->You get two chances to guess...All the best!!\n")
        sleep(5)
        
        ImageAddress = ["C:\\Users\\anura\\Desktop\\Pythonproject\\root.jpg","C:\\Users\\anura\\Desktop\\Pythonproject\\tooth.png"]
        img=ImageAddress[fourpiccnt]
        dispimg(img)

        for i in range(2):
            answer=input("Enter answer: ").upper()
    
            if fourpiccnt==0 and answer=='ROOT':
                print("\n\t\tYESS!! Correct Answer !!\n\t\t** --YOU WIN !! --**")
                return 1

            if fourpiccnt==1 and answer=='TOOTH':
                print("\n\t\tYESS!! Correct Answer !!\n\t\t**--YOU WIN !! --**")
                return 1
    
            else:
                print("\n\t\tWrong Anwer... Try again!\n\n")
            
        print("\n\t\tGAME OVER... ** You Lose **")
        return 0

     elif p==COMP:
    
        print("\n\t\tComputer plays *** FOUR PIC ONE WORD ***\n\n")
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        
        piccomp=rolldice()==rolldice()
        if piccomp:
            print("\n\t\t**--COMPUTER WINS--**")
            return 1
        else:
            print("\nComputer was not able to find the answer..")
            print("\n\t\t**--COMPUTER LOSES--**")
            return 0
def check_repeat(ls):
    
    return     
   
def play(p):
    
    global playerpos
    global comppos
    pos=0
    result=0
   
    dicenum=rolldice()
    print("\nNumber on die:",dicenum,"\n")
    sleep(1)
   
    if p==PLAYER and playerpos+dicenum<=16:
        playerpos+=dicenum
        pos=playerpos
        print("Your current position:",pos)
        
    elif p==PLAYER and playerpos+dicenum>16:
        print("\nOops..U went past sq 16..Better luck next time!\n")
        return result
       
    if p==COMP and comppos+dicenum<=16:
        comppos+=dicenum
        pos=comppos
        print("Computer's current position:",pos)
        
    if p==COMP and comppos+dicenum>16:
        print("\nComputer went past sq 16..So it stays on",comppos,"\n")        
    
    func_temp=funcs[:]
    if p==PLAYER:
        if len(hist)==0:
            func_call_ind=3
        else:
            func_call_ind=choice(func_temp)
        
       
        while func_call_ind in hist:
            func_temp.remove(func_call_ind)
            if len(func_temp)!=0:
                func_call_ind=choice(func_temp)
            else:
                func_temp=funcs[:]
                if len(hist)==6:
                    for i in hist:
                        hist.remove(i)
            
        hist.append(func_call_ind)
        if len(hist)==6:
            for i in hist:
                hist.remove(i)
    else:
        func_call_ind=choice(funcs)
        
    if func_call_ind==0:
        r=rps(p)  
        while(r==1):
            r=rps(p)
        if r=='w':
            result=1
        elif r=='l':
            result=0
    elif func_call_ind==1:
        result=numguess(p)
    elif func_call_ind==2:
        result=oddeven(p)
    elif func_call_ind==3:
        t=turtle.Turtle()
        t.hideturtle()
        result=hangman(p,t)
        t.screen.exitonclick()
    elif func_call_ind==4:
        result=twodie(p)
    elif func_call_ind==5:
        result=fourpic(p)
    
    
    # if pos in rps1:
    #     r=rps(p)  
    #     while(r==1):
    #         r=rps(p)
    #     if r=='w':
    #         result=1
    #     elif r=='l':
    #         result=0  

     
    # elif pos in numguess1:
    #     result=numguess(p)
       
    # elif pos in oddeven1:
    #     result=oddeven(p)
       
    # elif pos in hangman1:
    #     result=hangman(p)
   
    # elif pos in diegame1:
    #     result=twodie(p)
       
    # elif pos in fourpic1:
    #     result=fourpic(p)
   
    return result

def dispwin(p):
    
    winner="C:\\Users\\anura\\Desktop\\Pythonproject\\winner.png"
    loser="C:\\Users\\anura\\Desktop\\Pythonproject\\loser.png"
    
    if p==0:
        
        dispimg(winner)
        print("\n\tCONGRATULATIONS!!!\nYou have won!!!\n\n")
        
    elif p==1:
        dispimg(loser)
        print("\n\tThe computer has won....Better luck next time!\n\n")
        
    return


print("\n\t\t*************************************\n\t\tWELCOME TO THE ALL IN ONE BOARDGAME!!\n")
print("\t\t*************************************")

print("Rules:\n->Roll dice\n->Reach spot\n->Play a game\n\nIf u Win : Move 2 steps forward.\n     Lose: Stay on the same spot.\n\n")
print("\nYou start from SQUARE: 1...Reach SQUARE: 16 to win it!!")
print("\nRemember..Reach 16 before the computer does to win the game !!")
print("\n\nARE U READYYY??\n\n")

c=input("\nEnter YES to begin the game!").upper()

if c=="YES":
    
    while(playerpos!=16 and comppos!=16):
        
        print("\n-----------------------------------------------------------------------------\n")
        
        print("\n It's your turn now !!\n")
        result=play(PLAYER)
    
        if(result and playerpos+2<=16):
            sleep(1)
            print("\nCongrats!! Since you won, u move two more steps forward!!\n")
            playerpos+=2
            print("Your current position:",playerpos)
        
        if(playerpos==16):
            dispwin(PLAYER)
        
        sleep(3)
    
        print("\n It's computer's turn now !!\n")
        result=play(COMP)
    
        if(result and comppos+2<=16):
            comppos+=2
            sleep(1)
            print("\nComputer moves two more steps forward!!\n")
            print("Computer's current position:",comppos)
        
        if(comppos==16):
            dispwin(COMP)
        
        sleep(3)