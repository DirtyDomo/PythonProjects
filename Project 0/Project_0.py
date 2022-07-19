from Videogames2 import video_game

print("*** WELCOME TO VIDEO GAME JOURNAL! INPUT GAME: NAME, GENRE, SYSTEM, AND YOUR SCORE***")
def ___main___():
    while(True):
        game = input()
        vg = input()
        vgs = input()
        mscore = int(input())
        file = open("all_videogames.csv", "a")
        file.write(f"{game},{vg},{vgs},{mscore} \n")
        file.close()
___main___()