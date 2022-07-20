from Videogames2 import video_game

print("*** WELCOME TO VIDEO GAME JOURNAL! INPUT GAME: NAME, GENRE, SYSTEM, AND YOUR SCORE***")
def ___main___():
    while(True):
        print("***Input Game Name***")
        game = input()
        print("***Input Game Genre***")
        vg = input()
        print("*** Input Game System***")
        vgs = input()
        print("*** What Do You Rate Game?***")
        mscore = int(input())
        file = open("all_videogames.csv", "a")
        file.write(f"{game},{vg},{vgs},{mscore} \n")
        file.close()
        if mscore > 10:
            print("invalid Selection, choose number bet 1-10")
        elif mscore <= 0:
            print("invalid Selection, choose number bet 1-10")
            continue
        elif input() == "exit" or "Exit" or "EXIT":
            break
___main___()