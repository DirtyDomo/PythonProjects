class video_game:
    def __init__(self, name, genre, system, score):
        self.name = str(name)
        self.genre = str(genre)
        self.system = str(system)
        self.score = int(score)
    
    def getname(self): #Name of Game
        print("*** What is the name of the game?***")
        input("\n>>>")
    # getname()
    
    def getgenre(self): #genre of Game
        print("*** What is Genre of Video Game?***")
        input("\n>>>")
    # get_genre()
    
    def gamesystem(self): #game system
        print("*** What is the name of the system?***" )
        input("\n>>>")
    # game_system()
    
    def rating(score): #game rating
        print("***What do you rate this game 1-10?***")
        o = int(input()) 
        if o > 10:
            print("invalid Selection, choose number bet 1-10")
        elif o <= 0:
            print("invalid Selection, choose number bet 1-10")
    # rating()
