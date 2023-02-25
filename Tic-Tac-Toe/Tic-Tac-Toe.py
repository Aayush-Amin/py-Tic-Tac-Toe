from PlayerVsPlayer import PlayerVsPlayer
from PlayerVsBot import PlayerVsBot

def main():
    i=True
    while i:
        mode=input("\nEnter 1 to play against another player or enter 2 to play against a bot: ")
        if mode=="1":
            i=False
        elif mode=="2":
            i=False
        

    if mode=="1":
        PlayerVsPlayer()
    if mode=="2":
        PlayerVsBot()
main()