def init():
    q="1";w="2";e="3";r="4";t="5";y="6";u="7";i="8";o="9"

    player1="X"
    player2="O"
    player=1
    count=0
    print("\nThis is the Tic Tac Toe table.\nYou will be asked the position you would like to mark. \nEnter the number at that position.\nPlayer 1 will be X and player 2 will be O\n")
    table(q,w,e,r,t,y,u,i,o)

    return q,w,e,r,t,y,u,i,o,player1,player2,player,count

def table(q,w,e,r,t,y,u,i,o):
    print("| ",q," | ",w," | ",e," |")
    print("-------------------")
    print("| ",r," | ",t," | ",y," |")
    print("-------------------")
    print("| ",u," | ",i," | ",o," |\n")

def positionCheck(pos,player,q,w,e,r,t,y,u,i,o):
    if player==1:
        player="x"
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
        print("player ",player," has wone by getting 3 in a row")



def main():
    q,w,e,r,t,y,u,i,o,player1,player2,player,count=init()

    while True:
        
        pos=input("\nPlayer "+str(player)+" where would you like to place a marker: ")
        q,w,e,r,t,y,u,i,o=positionCheck(pos,player,q,w,e,r,t,y,u,i,o)        
        table(q,w,e,r,t,y,u,i,o)
        count+=15

        gameState=check(q,w,e,r,t,y,u,i,o,count)
        if gameState=="game":
            gameDone(player)
            break
        elif gameState=="tie":
            gameDone("tie")
        
        
        if player==1:
            player=2
        else:
            player=1

main()