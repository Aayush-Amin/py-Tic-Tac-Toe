import random
def init():
    q="1";w="2";e="3";r="4";t="5";y="6";u="7";i="8";o="9"

    player="1"
    count=0
    print("\nThis is the Tic Tac Toe table.\nYou will be asked the position you would like to mark. \nEnter the number at that position.\nPlayer 1 will be X and bot will be O\n")
    
    while True:
        first=input("Enter 1 to go first or 2 to have the bot go first: ")
        if first=="1" or first=="2":
            break

    if first=="2":
        player="bot"


    table(q,w,e,r,t,y,u,i,o)

    return q,w,e,r,t,y,u,i,o,player,count,first


def table(q,w,e,r,t,y,u,i,o):
    print("| ",q," | ",w," | ",e," |")
    print("-------------------")
    print("| ",r," | ",t," | ",y," |")
    print("-------------------")
    print("| ",u," | ",i," | ",o," |\n")

def positionCheck(pos,player,q,w,e,r,t,y,u,i,o):
    if player=="1":
        player="X"
    else:
        player="O"

    if pos=="1":
        q=player
    elif pos=="2":
        w=player
    elif pos=="3":
        e=player
    elif pos=="4":
        r=player
    elif pos=="5":
        t=player
    elif pos=="6":
        y=player
    elif pos=="7":
        u=player
    elif pos=="8":
        i=player
    else:
        o=player
    
    return q,w,e,r,t,y,u,i,o

def check(q,w,e,r,t,y,u,i,o,count):
    if q==w==e:
        return "game"
    elif r==t==y:
        return "game"
    elif u==i==o:
        return "game"
    elif q==r==u:
        return "game"
    elif w==t==i:
        return "game"
    elif e==y==o:
        return "game"
    elif q==t==o:
        return  "game"
    elif u==t==e:
        return "game"
    else:
        pass
    if count==9:
        return "tie"

def gameDone(player):
    if player=="tie":
        print("The game was a tie and no one won")
    else:
        print("player ",player," has won by getting 3 in a row")


def botDefence(q,w,e,r,t,y,u,i,o):
    if r=="X" and u=="X" and q!="O":
        pos=1
    elif t=="X" and i=="X" and w!="O":
        pos=2
    elif y=="X" and o=="X" and e!="O":
        pos=3
    elif q=="X" and r=="X" and u!="O":
        pos=7
    elif w=="X" and t=="X" and i!="O":
        pos=8
    elif e=="X" and y=="X" and o!="O":
        pos=9
    
    elif q=="X" and w=="X" and e!="O":
        pos=3
    elif r=="X" and t=="X" and y!="O":
        pos=6
    elif u=="X" and i=="X" and o!="O":
        pos=9
    elif w=="X" and e=="X" and q!="O":
        pos=1
    elif t=="X" and y=="X" and r!="O":
        pos=4
    elif i=="X" and o=="X" and u!="O":
        pos=7

    elif q=="X" and t=="X" and o!="O":
        pos=9
    elif t=="X" and o=="X" and q!="O":
        pos=1
    elif q=="X" and o=="X" and t!="O":
        pos=5

    else:
        pos="N/A"
    return pos

def botOffence(q,w,e,r,t,y,u,i,o):
    if r=="O" and u=="O" and q!="X":
        pos=1
    elif t=="O" and i=="O" and w!="X":
        pos=2
    elif y=="O" and o=="O" and e!="X":
        pos=3
    elif q=="O" and r=="O" and u!="X":
        pos=7
    elif w=="O" and t=="O" and i!="X":
        pos=8
    elif e=="O" and y=="O" and o!="X":
        pos=9
    
    elif q=="O" and w=="O" and e!="X":
        pos=3
    elif r=="O" and t=="O" and y!="X":
        pos=6
    elif u=="O" and i=="O" and o!="X":
        pos=9
    elif w=="O" and e=="O" and q!="X":
        pos=1
    elif t=="O" and y=="O" and r!="X":
        pos=4
    elif i=="O" and o=="O" and u!="X":
        pos=7

    elif q=="O" and t=="O" and o!="X":
        pos=9
    elif t=="O" and o=="O" and q!="X":
        pos=1
    elif q=="O" and o=="O" and t!="X":
        pos=5

    else:
        pos="N/A"
    return pos

def botLogic(q,w,e,r,t,y,u,i,o,first):
    table=(q,w,e,r,t,y,u,i,o)
    openspots=[]
    for i in range(len(table)):
        try:
            int(table[i])
            openspots.append(table[i])
        except:
            pass
    
    if first=="1":
        pos=botDefence(q,w,e,r,t,y,u,i,o)
        if pos=="N/A":
            pos=botOffence(q,w,e,r,t,y,u,i,o)
        if pos=="N/A":
            pos=random.choice(openspots)
    else:
        pos=botOffence(q,w,e,r,t,y,u,i,o)
        if pos=="N/A":
            pos=botDefence(q,w,e,r,t,y,u,i,o)
        if pos=="N/A":
            pos=random.choice(openspots)
    

    print("The bot has marked the spot at postion "+str(pos))
    return str(pos)



def PlayerVsBot():
    q,w,e,r,t,y,u,i,o,player,count,first=init()


    while True:

        if first=="1":
            if player=="1":
                pos=input("\nPlayer "+player+" where would you like to place a marker: ")
            else:
                pos=botLogic(q,w,e,r,t,y,u,i,o,first)
        else:
            if player=="bot":
                pos=botLogic(q,w,e,r,t,y,u,i,o,first)
            else:
                pos=input("\nPlayer "+player+" where would you like to place a marker: ")
            

        
        q,w,e,r,t,y,u,i,o=positionCheck(pos,player,q,w,e,r,t,y,u,i,o)        
        table(q,w,e,r,t,y,u,i,o)
        count+=1

        gameState=check(q,w,e,r,t,y,u,i,o,count)
        if gameState=="game":
            gameDone(player)
            break
        elif gameState=="tie":
            gameDone("tie")
        
        
        if player=="1":
            player="bot"
        else:
            player="1"



#PlayerVsBot()