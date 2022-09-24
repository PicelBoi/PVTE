# modules :)
import pickle
import os.path
import datetime
import random
import platform

# PVTE = PicelBoi Virtual Terminal Environment
# PicelBoi made this

# IMPORTANT VARIABLES RELATING TO CODE BUILD
pvte_name = ("PVTE v1.0a")
pvte_fullname = ("PicelBoi Virtual Terminal Environment")
patch_date = ("2022-9-24")
location = ("New York")
python_version = ("Python 3.10")
author = ("Etan Zheng (PicelBoi)")
message = ("THIS IS A ALPHA BUILD!")
# Important functions.
def newsettings():
    # Makes a setting file.
    birthmonth = 0
    birthday = 0
    birthyear = 0
    name = str(input("What is your name?"))
    print('Please enter your birthday.')

    while 1 > birthmonth or 12 < birthmonth:
        try:
            birthmonth = int(input("Enter your birthmonth. For example: 9 is the birthmonth for September."))
        except ValueError:
            # Make em feel bad!
            print("Please put in your birthmonth, accepted values range from 1 to 12.")
    while 1 > birthday or 31 < birthday:
        try:
            birthday = int(input("Enter your birthday. For example: 23rd."))
        except ValueError:
            # Make em feel bad!
            print("Please put in your birthday, accepted values range from 1 to 31.")
    while 1900 > birthyear or 9000 < birthyear:
        try:
            birthyear = int(input("Enter your birthyear. For example: 2022"))
        except ValueError:
            # Make em feel bad!
            print("Please put in your birthyear, accepted values range from 1900 to 9000.")
    greeting = input("What do you want us to say when you start up PCL?")
    print("That's all the info we need. Wait while we do all the work. (grab a coffee if your computer is extremely "
          "old.")
    with open('settings.pkl', 'wb') as brandnew:
        pickle.dump([name, birthmonth, birthday, birthyear, greeting], brandnew)


def loadsettings():
    # Loads the setting file.
    global name, birthmonth, birthyear, birthday, greeting
    with open('settings.pkl', 'rb') as loader:
        name, birthmonth, birthday, birthyear, greeting = pickle.load(loader)
    print("Loaded!")


def start():
    # Prompt.
    prompt = input(name + "@PCL =")
    try:
        eval(prompt + '()')
    except ValueError:
        print("Unknown command. Type in helpptve to list all commands.")
    except SyntaxError:
        print("Unknown command. Type in helpptve to list all commands.")
    except NameError:
        print("Unknown command. Type in helpptve to list all commands.")
    except OverflowError:
        print("OVERFLOW!!")


def helpptve():
    print("Help not avilable.")


def exit():
    # broken
    infiniteloop = 0


# Commands.
def echo():
    # prints "vecho".
    vecho = input("Type in a sentence.")
    print(vecho)


def rpg():
    MHP = int(40)
    PHP = int(100)
    potions = 3
    while MHP > 0 or PHP > 0:
        print("A Jellbie appeared! Don't try to bite it, or you'll become the jellbie itself.")
        print("Jellbie HP: " + str(MHP))
        print(name + " HP: " + str(PHP))
        print("fight to fight, support to recover, bite to bite the jellbie and die.")
        player = ("COMMAND!")
        if player == ("fight"):
            damage = random.randint(0, 40)
            if damage <= 0:
                print("You tried to attack, but the jellbie dodged!")
            elif damage >= 1:
                print("you hit him! you dealt " + str(damage) + " damage to the jellbie!")
                MHP = MHP - damage
                print("Jellbie's at " + str(PHP) + " hp.")
                print("Jellbie attacks!")
                PHP = PHP - 20
                print("Jellbie did 20 damage!")
        elif player == ("support"):
            health = random.randint(20, 40)
            if potions >= 0:
                print("You drank the health potion!")
                PHP = PHP + health
                print("you recovered " + str(health) + " hp.")
                print("You have " + str(potions) + " potions left.")
            elif potions <= 0:
                print("You have no more potions!")
            print("Jellbie attacks!")
            PHP = PHP - 20
            print("Jellbie did 20 damage!")
        elif player == ("bite"):
            print("You bite the jellbie. The taste is too sweet, you feel sleepy, sleepy, sleepy...")
            PHP = 0
        else:
            print("Wrong command.")
    if PHP <= 0:
        print("You won!")
    else:
        print("you got infected with the jelly virus...")


def about():
    my_system = platform.uname()

    print(f"""
         //(*,,,........,..............,,  {pvte_name}
  ((((((#/,*,,,*,*,,*,,,,,,,,,,,,,,,,,     Patch: {patch_date}
  (#((((#/***&&&&&%%%%%%%#%%%%%%%@%/,,     CPU: {my_system.processor}
 #((((#((/**#*****,,,,,,,,,,***,*&%(,,     System: {my_system.system}
 ,(((((((/,*/******          ****%@(,,     Node Name: {my_system.node}
  ((#(((#/*********..,.,,,...****%@(,,     Release: {my_system.release}
  ##(#(#((/*,,******..*,.  ..****%@/*,     Version: {my_system.version}
  (#####(#/**********************%@(*,     Machine: {my_system.processor}
  #####(##/**(*********,***,,,**,#@/**  
  ########/**,(((/,...,,,,.....,******              {pvte_fullname}
  (#######(****************************                     Made in {location}
  ########/********************/*/##/*/                     ({python_version})
  #######%/***************************/                  By {author}
  ########(**/(******************//*//*                  {message}
  #%######(*******/*/(((((((((((((((#               Owned by: {name}
    &(((###((((##%%#%#%%%%%%%%%%%@%#                Greeting: {greeting}
      &#%#%%%%%%%%%%%%%%%%%%%%&&&&&&%               Birthday: {birthmonth}-{birthday}-{birthyear}
        %%%&@@&&&%#&                                        """)





# Path to settings.
settings = "settings.pkl"

# We make a infinite loop here.
infiniteloop = 1
# Startup sequence
print("Starting PVTE v1.0...")
print("Checking for setting files...")
if os.path.isfile(settings):
    print("Found settings file! Loading it...")
    loadsettings()
else:
    print("No settings file found! Creating one...")
    newsettings()
    name = "Waddle Dee"
    birthday = 23
    birthyear = 2022
    birthmonth = 9
    greeting = "default"
    loadsettings()
print("Settings done.")

print("Hello!, " + name + ".")
print(greeting)
if infiniteloop >= 1:
    while infiniteloop >= 1:
        start()
else:
    about()
    print("Bye!")
