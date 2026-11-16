from player import Player
import os

def cls():
    os.system("clear||cls")

def line():
    print("+"+"—"*30+"+")

def create_player():
    paths = [
    # name / status / type of damage or skill that it domains
        ["Purger",20,0,0,5,-5,2,5,5,["Fisical","Weapon"]], # strong fisical attacks but weak spiritual defense/attacks
        ["Summoner",-20,20,0,-5,5,2,0,5,["Summon","Effect"]], # weak on defense/damage/rituals but can summon spirits to fight for it
        ["Manifester",-20,-20,-20,-5,-5,5,0,0,["Manifest","Ritual"]], # gains power when it loses its sanity, rituals can improve its sanity decrease
        ["Ritualist",0,20,20,0,0,0,0,0,["Ritual","Effect"]] # can uses rituals for apply effects on itself or on others of its group
    ]# paths are the players classes
    sex = ["Man","Woman","Other"]
    
    stage = 0

    while stage < 3:
        match stage:
            case 0:
                cls()
                line()
                print("* What's your name? (f/l name)")
                line()
                name = str(input("> "))
                try:
                    if name != None:
                        stage += 1
                except:
                    pass
                    
            case 1:
                cls()
                line()
                print("* What's your sex?")
                line()
                for number,item in enumerate(sex,start=1):
                    print(f"[{number}]. {item}")
                line()
                choice = int(input("> "))
                try:
                    if choice >= 1 and choice <= len(sex):
                        sex = sex[choice-1]
                        stage += 1
                except:
                    pass
                    
            case 2:
                cls()
                line()
                print("* What's your class? ")
                line()
                for number,path in enumerate(paths,start=1):
                    print(f"[{number}]. {path[0]}")
                line()
                path = int(input("> "))
                try:
                    if path >= 1 and path <= len(paths):
                        path = paths[path]
                        stage += 1
                except:
                    pass

    player = Player(name,sex,path)

    cls()
    line()
    print("* SUCESS!")
    line()
    input("...")

create_player()
