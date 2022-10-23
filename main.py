# modules :)
import importlib
import os
import os.path
import pickle
import platform
import random
import sys
import time

import argon2
from argon2 import PasswordHasher

ph = PasswordHasher()
# PVTE = PicelBoi Virtual Terminal Environment
# PicelBoi made this

# IMPORTANT VARIABLES
# the fact that I made this code spaghetti is bad. DONT REMOVE DESTROYPVTE.

destroypvte = "bad"
root = os.getcwd()
userprofiles = root + "/userprofiles"
pvte_name = ("PVTE v1.0.1a")
pvte_fullname = ("PicelBoi Virtual Terminal Environment v1.0.1")
patch_date = ("2022-10-22")
location = ("New York")
python_version = ("Python 3.10")
author = ("Etan Zheng (PicelBoi)")
message = ("THIS IS A ALPHA BUILD!")
password_correct = 0
ascii_art = ("""
 
             ,,,,,,,,,,,,,,,....
       ,φ▄▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒∩
     ▐▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒H
     ▓▓▓▓▓▓▓▓▓▒▒███████▀▀▀▀▀▀▀▀▀▀▀▀▀██▓▌▒H
     ▓▓▓▓▓▓▓▓╫▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▌▒H
     ▓▓▓▓▓▓▓▓▓▒▒█▒▒▒▒▒ªª²²²"```"▒▒▒▒╫█▌▌▒H
     ▓▓▓▓▓▓▓▓╫▒▒█▒▒▒▒▒  ::¬─.:  ║▒▒▒╫█▌▓▒H
     ╟▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒▒H      ...║▒▒▒╫█▌▓▒▒
     ╫▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▌▓▒▒
     ╟▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▌▓▒▒
     ╫▓▓▓▓▓▓▓▓╫▒╫▄▄▄▄▄▄▄▄▄▓▓▓▓▓▓▓▓▓▓▓▀▒╫▒▒
     ▐▓▓▓▓▓▓▓▓╫▒▒▐▀▀▒▒▒▒▒▒▒▒▒▒▒╦╦▒▒▒▒K▒▒▒▒
     ▐▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
     ▐▓▓▓▓▓▓▓▓▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄▄▓▓▓▒▒▒
     ▐▓▓▓▓▓▓▓▓▌▒▒▒▒▒▒▒▒▒▒▒▒▒Ñ▒▒▒▒KÑÑ▒ÑÑ╫▒▒
     ▐▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ÑÑÑÑÑÑ
     ▐██▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓
      ▀███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓
        ▀███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓█▓██▓▓
          ▀█▓▓█████▓▓██████████▀▀▀▀▀▀╙"`
            ╙▀▀▀▀▀▀▀"╙`
     """)

# Checks if folder exists, if not, then make
exists = os.path.exists(userprofiles)

if exists == True:
    print("Pre-boot check reported that folders are intact.")
else:
    print("Pre-boot check reported that folders are not intact. Making folders...")
    os.mkdir(userprofiles)


# Important functions.
# Deprecated and useless.
class system:
    def password(self):
        global password_correct, hashe, fullname
        correct = 0
        while correct <= 0:
            print("Hello!")
            ok = input("Please enter your password.")
            if ok == "reset":
                system.resetsettings(destroypvte)
                correct = 1
            else:
                try:
                    time.sleep(5)
                    ph.verify(hashe, ok)
                    correct = 1
                except argon2.exceptions.VerifyMismatchError:
                    time.sleep(5)
                    print("Wrong password. Type in 'reset' to reset this setting file.")

    def loadusers(self):
    # obsolete?
        print("DEBUG: LOADUSERS STARTED")
        for x in os.listdir(userprofiles):
            if x.endswith(".pvteuser"):
                # Loading all users...
                print("Found user: " + x)
            else:
                print("No settings file found! Creating one...")
                system.newsettings(destroypvte)
                name = "Waddle Dee"
                fullname = "Waddler Waddle Dee"
                maile = "Waddle@waddle.com"
                birthday = 23
                birthyear = 2022
                birthmonth = 9
                greeting = "default"
                hashe = "etan"

    def loadfunctions(self):
        sys.path.append("functions/")
        for x in os.listdir(root + "/functions/"):
            if x.endswith(".py"):
                # Loading all functions...
                try:
                    module = (x.replace('.py', ''))
                    importlib.import_module(module)
                except SyntaxError:
                    print("WORK IN PROGRESS")
                    print("loading " + x)


    def reload(self):
        print("useless rn, fixing this l8er")


    def resetsettings(self):
        keeper = 1
        confirm = str.lower((input("D/O YOU WANT TO RESET ALL YOUR DATA?? (y for yes, n for no, case-sensitive)")))
        while keeper <= 1:
            if confirm == "y":
                print("good bye :(")
                os.remove("settings.pvte")
                keeper = 0
                newsettings()
            elif confirm == "n":
                print("reset prevented :)")
            else:
                print("Invalid response.")


    def newsettings(self):
        # Makes a setting file.
        global fullname, name, hashe, maile, greeting, birthday, birthyear, birthmonth
        birthmonth = 0
        birthday = 0
        birthyear = 0
        name = str(str.lower(input("What is your name?")))
        fullname = str(input("What is your full name?"))
        maile = str(input("What is your email?"))
        passwordd = str(input("Please enter a strong password."))
        hashe = ph.hash(passwordd)

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
        with open(userprofiles + '/' + name + '.pvteuser', 'wb') as brandnew:
            pickle.dump([name, birthmonth, birthday, birthyear, greeting, fullname, hashe, maile], brandnew)


    def loadsettings(self):
        # Loads the setting file.
        global name, birthmonth, birthyear, birthday, greeting, maile, hashe, username, userpath, userprofiles
        userconfirm = 0
        username = input("What is your name?")

        while userconfirm >= 1:
            global name, birthmonth, birthyear, birthday, greeting, maile, hashe
            username = str(str.lower(input("What is your name?")))
            userpath = userprofiles + '/' + username + ".pvteuser"

            userexists = os.path.isfile(userpath)
            if userexists == True:
                userconfirm = 1
            else:
                print("User does not exist.")




    def shell(self):
        # Prompt.
        prompt = input(name + "@PVTE = ")
        try:
            eval('app.' + prompt + '(destroypvte)')
        except ValueError:
            print("Unknown command. Type in helpptve to list all commands.")
        except SyntaxError:
            print("Unknown syntax. Check your command.")
        except NameError:
            print("Unknown command. Type in helpptve to list all commands.")
        except OverflowError:
            print("OVERFLOW!!")
        except TypeError:
            print("Unknown type. Check your command.")




    def exit(self):
        # broken
        infiniteloop = 0

    def loginprompt(self):
        command_filled = 1
        global fullname, name, hashe, maile, greeting, birthday, birthyear, birthmonth
        while command_filled >= 1:

            command = str(input(f"Welcome to {pvte_name}! Type in create to create a user account, or login to login to a user file you made."))
            if command == "create":
                system.newsettings(destroypvte)
            elif command == "login":
                system.loadsettings(destroypvte)
                command_filled = 0
            else:
                print("Invalid command.")
# Commands.
class app:
    def helpptve(self):
        print("All built-in commands.")
        print("""
        Calculator: (commands are plus, minus, multiply, divide) A simple calculator.
        Jellbie!: (command is rpg.) A simple Role Playing Game.
        System: (command is about) System commands.""")

    def plus(self):
        add1 = input("First number.")
        add2 = input('Second number.')
        add = (float(add1) + float(add2))
        print(str(add))


    def minus(self):
        subtract1 = input("First number.")
        subtract2 = input("Secound number.")
        subtract = (float(subtract1) - float(subtract2))
        print(str(subtract))


    def multiply(self):
        times1 = input("First number.")
        times2 = input("Second number.")
        times = (float(times1) * float(times2))


    def divide():
        divide1 = input("First number.")
        divide2 = input("Second number.")
        divider = (float(divide1) / float(divide2))


    def echo(self):
        # prints "vecho".
        vecho = input("Type in a sentence.")
        print(vecho)


    def rpg(self):
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


    def about(self):
        my_system = platform.uname()
        print(f"""
                   ,,,,,,,,,,,,,,,....      {pvte_name}
       ,φ▄▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒∩  ({pvte_fullname})
     ▐▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒H  -----------------------------
     ▓▓▓▓▓▓▓▓▓▒▒███████▀▀▀▀▀▀▀▀▀▀▀▀▀██▓▌▒H  System Information
     ▓▓▓▓▓▓▓▓╫▒▒▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█▓▌▒H  CPU: {my_system.processor}
     ▓▓▓▓▓▓▓▓▓▒▒█▒▒▒▒▒ªª²²²"```"▒▒▒▒╫█▌▌▒H  OS: {my_system.system}
     ▓▓▓▓▓▓▓▓╫▒▒█▒▒▒▒▒  ::¬─.:  ║▒▒▒╫█▌▓▒H  Node: {my_system.node}
     ╟▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒▒H      ...║▒▒▒╫█▌▓▒▒  Version: {my_system.version}
     ╫▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▌▓▒▒  Machine: {my_system.machine}
     ╟▓▓▓▓▓▓▓▓▒▒▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▌▓▒▒  -----------------------------
     ╫▓▓▓▓▓▓▓▓╫▒╫▄▄▄▄▄▄▄▄▄▓▓▓▓▓▓▓▓▓▓▓▀▒╫▒▒  User Information
     ▐▓▓▓▓▓▓▓▓╫▒▒▐▀▀▒▒▒▒▒▒▒▒▒▒▒╦╦▒▒▒▒K▒▒▒▒  Name: {name}
     ▐▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  
     ▐▓▓▓▓▓▓▓▓▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▄▄▓▓▓▒▒▒  E-Mail: {maile}
     ▐▓▓▓▓▓▓▓▓▌▒▒▒▒▒▒▒▒▒▒▒▒▒Ñ▒▒▒▒KÑÑ▒ÑÑ╫▒▒  Birthday: {birthmonth}-{birthday}-{birthyear}
     ▐▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ÑÑÑÑÑÑ  Greeting: {greeting}
     ▐██▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓  -----------------------------
      ▀███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓    Other Information
        ▀███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓█▓██▓▓    Message: {message}
          ▀█▓▓█████▓▓██████████▀▀▀▀▀▀╙"`    Patch: {patch_date}
            ╙▀▀▀▀▀▀▀"╙`
""")


# Path to settings.
for x in os.listdir(userprofiles):
    global settings
    settings = x.endswith(".pvteuser")


# We make a infinite loop here.
infiniteloop = 1
# Startup sequence
print("Starting PVTE v1.0...")
print("Loading services....")
system.reload(destroypvte)
print("Checking for setting files...")
birthmonth = 0
birthday = 0
birthyear = 0
name = "kirby"
fullname = "kirbykirby"
maile = "e@e.com"
passwordd = "wadl"
hashe = "eat"

command_filled = 1
while command_filled >= 1:

    command = str(input(f"Welcome to {pvte_name}! Type in create to create a user account, or login to login to a user file you made."))
    if command == "create":
        system.newsettings(destroypvte)
    elif command == "login":
        userconfirm = 0
        username = input("What is your name?")
        while userconfirm >= 1:
            username = str(str.lower(input("What is your name?")))
            userpath = userprofiles + '/' + username + ".pvteuser"

            userexists = os.path.isfile(userpath)
            if userexists == True:
                userconfirm = 1
            else:
                print("User does not exist.")
        with open(userprofiles + '/' + username + ".pvteuser", 'rb') as loader:
            name, birthmonth, birthday, birthyear, greeting, maile, hashe, fullname = pickle.load(loader)
        print("Loaded!")

        command_filled = 0
    else:
        print("Invalid command.")

print("Settings done.")
print("Loading all functions from functions folder...")
system.loadfunctions(destroypvte)
system.password(destroypvte)
print("Hello!, " + name + ".")
print(greeting)
if infiniteloop >= 1:
    while infiniteloop >= 1:
        system.shell(destroypvte)
else:
    app.about()
    print("Bye!")
