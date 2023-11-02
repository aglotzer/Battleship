#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 08:55:12 2021

@author: alexglotzer

Alex Glotzer
COMP-112 Intro to Programming
Final Porject
12/17/2021
"""
import random
import copy
sinkDictP = {5:0, 4:0, 3:0, 2:0, 1:0}
sinkDictC = {5:0, 4:0, 3:0, 2:0, 1:0}
hitlistP = []
hitlistC = []
hotcoords = [None, None]
choicecoords = []
cbombed = 0
pbombed = 0
miss = 0
posscordsc = []
posscordscc = []
playerguess = []


playershots = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

player = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
computershots = copy.deepcopy(player)
computer = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

i = 0
while i < 10:
    j = 0
    while j < 10:
        posscordsc.append([i, j])
        j += 1
    i += 1
    
posscordsp = copy.deepcopy(posscordsc)
userfile = None
def begin():
    """
    Sig: NoneType -> NoneType
    Prompts the user to pick a login method and then open up a file with the information they want
    """
    global userfile
    print("Welcome!")
    option = input("Login, Signup, or Guest: ")
    if (option == "Signup"):
        userfile = signup()
    elif (option == "Login"):
        userfile = login()
    else:
        guest()

def signup():
    """
    Sig: NoneType -> File
    Allows the user to create a new file to store their data and bein playing
    """
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    conf = input("Please confirm your password: ")
    while True:
        if (password == conf):
            name = username + ".txt"
            file = open(name, "a")
            file.write(password)
            break
        else:
            conf = input("Passwords do not match. Please try again: ")
    player_place_ships()
    return file

def login():
    """
    Sig: NoneType -> File
    Allows the user to access the file that they have been using previously
    """
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    name = username + ".txt"
    i = 0
    while (i < 5):
        file = open(name, "r")
        if not (password == file.readline()):
            file.close()
            i += 1
            password = input("Incorrect password. Please try again: ")
        else:
            player_place_ships()
            return file
    print("You were wrong too many times. Please go back to the beginning and try again.")
    begin()
    
    
def guest():
    """
    Sig: NoneType -> NoneType
    Allows the user to cjust start playing without having to worry about data and scores
    """
    player_place_ships()

    
def validvp(x, y, size):
    """
    Sig: Int, Int, Int -> Boolean
    Checks to see if the user can place a boat vertically in a selected space
    """
    validity = False
    i = 1
    if size == 1:
        if computer[x][y] == 0:
            validity = True
            return validity
        else:
            return validity
    if (x < 10 and y < 10 and x >= 0 and y >= 0):
        while (i < size):
            if(x + i < 10 and x + i > 0 and player[x+i][y] == 0):
                i += 1
            else:
                return validity
        validity = True
        return validity
    else:
        return validity

def validhp(x, y, size):
    """
    Sig: Int, Int, Int -> Boolean
    Checks to see if the user can place a boat horizontally in a selected space
    """
    validity = False
    i = 1
    if size == 1:
        if computer[x][y] == 0:
            validity = True
            return validity
        else:
            return validity
    if (x < 10 and y < 10 and x >= 0 and y >= 0):
        while (i < size):
            if(y + i < 10 and y + i > 0 and player[x][y+i] == 0):
                i += 1
            else:
                return validity
        validity = True
        return validity
    else:
 
        return validity
    
def validvc(x, y, size):
    """
    Sig: Int, Int, Int -> Boolean
    Checks to see if the computer can place a boat vertically in a selected space
    """
    validity = False
    i = 1
    if size == 1:
        if computer[x][y] == 0:
            validity = True
            return validity
        else:
            return validity
    if (x < 10 and y < 10 and x >= 0 and y >= 0):
        while (i < size):
            if(x + i < 10 and x + i > 0 and computer[x+i][y] == 0):
                i += 1
            else:
                return validity
        validity = True
        return validity
    else:
        return validity

def validhc(x, y, size):
    """
    Sig: Int, Int, Int -> Boolean
    Checks to see if the computer can place a boat horizontally in a selected space
    """
    global computershots
    validity = False
    i = 1
    if size == 1:
        if computer[x][y] == 0:
            validity = True
            return validity
        else:
            return validity
    if (x < 10 and y < 10 and x >= 0 and y >= 0):
        while (i < size):
            if(y + i < 10 and y + i > 0 and computer[x][y+i] == 0):
                i += 1
            else:
                return validity
        validity = True
        return validity
    else:
        return validity
    
def player_place_ships():
    """
    Sig: NoneType -> NoneType
    Prompts the user to place their boats on the gameboard and makes sure the user is placing the boats in legal spaces
    """
    global computershots
    ships = [5, 4, 3, 2, 1]
    while (len(ships) > 0):
        print("You have", len(ships), "left. They are size", ships)
        while True:
            try:
                size = int(input("Which would you like to place? "))
                break
            except:
                print("Invalid boat size. Please try again.")
        while True:
            if size in ships:
                break
            else:
                print("Invalid boat size. Please try again.")
                size = int(input("Which would you like to place? "))
        while True:
            placement = input("Please enter the coordinates between [0, 0] and [9, 9] for the front of the ship like this: '5,2' ")
            way = input("Please enter horizontal or vertical: ")
            y = int(placement[:1])
            x = int(placement[2:])
            if (way.upper() == "HORIZONTAL" and validhp(x, y, size)):
                i = 0
                while (i < size):
                    player[x][y + i] = size
                    i += 1
                ships.remove(size)
                break
            elif (way.upper() == "VERTICAL" and validvp(x, y, size)):
                i = 0
                while (i < size):
                    player[x + i][y] = size
                    i += 1
                ships.remove(size)
                break
            else:
                print("Invalid entry. Please try again.")
        for i in player:
            print(i)
    i = 0
    while i < 10:
        j = 0
        while j < 10:
            if(not player[i][j] == 0):
                posscordscc.append([i, j])
            j += 1
        i += 1
    computershots = copy.deepcopy(player)
    computer_place_ships()
    

def computer_place_ships():
    """
    Sig: NoneType -> NoneType
    Uses random to strategically place the computer's boats on the board and makes sure the selections are legal
    """
    ships = [5, 4, 3, 2, 1]
    while (len(ships) > 0):
        ways = ["horizontal", "vertical"]
        size = ships[random.randint(0, len(ships)-1)]
        way = ways[random.randint(0, len(ways)-1)]
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if(way.upper() == "HORIZONTAL" and validhc(x, y, size)):
            i = 0
            while (i < size):
                computer[x][y + i] = size
                i += 1
            ships.remove(size)
            
        elif(way.upper() == "VERTICAL" and validvc(x, y, size)):
            i = 0
            while (i < size):
                computer[x + i][y] = size
                i += 1
            ships.remove(size)
    player_turn(sinkDictP)
            
def player_turn(sinkDictP):
    """
    Sig: Dictionary -> NoneType
    Prompts the user to guess coordinates of where they suspect the computer's ships to be
    """
    print("Previous Guesses:", playerguess)
    target = input("In the same coordinate form, please enter a target: ")
    while True:
        try:
            y = int(target[:1])
            x = int(target[2:])
            break
        except:
            print("Invalid coordinates. Please try again.")
            target = input("In the same coordinate form, please enter a target: ")
    playerguess.append([x, y])
    if (not computer[y][x] == 0 and [y, x] in posscordsp):
        posscordsp.remove([y, x])
        sinkDictP[computer[y][x]] += 1
        print("HIT!")
        playershots[y][x] = "!"
        for i in playershots:
            print(i)
        pbombed = computer[y][x]
        computer[y][x] = 100
        if (sinkDictP[pbombed] == pbombed):
            print("You sunk their Battleship!")
            sinkDictP.pop(sinkDictP[pbombed])
            if len(sinkDictP) == 0 and not len(sinkDictC) == 0:
                player_win()
            
        player_turn(sinkDictP)
    else:
        playershots[y][x] = "X"
        print("Miss")
        for i in playershots:
            print(i)
        computer_turn(sinkDictC)
    

def computer_turn(sinkDictC):
    """
    Sig: Dictionary -> NoneType
    Has the computer strategically guess spaces where the user might have ships
    """
    global hotcoords
    global choicecoords
    global miss
    if (not miss == 0 and miss % 5 == 0):
        chosen = random.choice(posscordscc)
        y = chosen[0]
        x = chosen[1]
        posscordscc.remove(chosen)
    else:
        try:
            choose = random.choice(posscordsc)
            y = choose[0]
            x = choose[1]
        except:
            computer_win()
        if not (hotcoords[0] == None and hotcoords[1] == None):
            y = hotcoords[0]
            x = hotcoords[1]
        while True:
            if([y,x] not in posscordsc):
                y = random.randint(0, 9)
                x = random.randint(0, 9)
            else:
                break
    if([y, x] in posscordscc):
        posscordscc.remove([y, x])
    print("x:", y)
    print("y:", x)
    while(not player[y][x] == 0 and [y, x] in posscordsc):
        posscordsc.remove([y, x])
        choicecoords = []
        cbombed = 0
        if(x == 9 and y == 9):
            choicecoords = [[y - 1, x], [y, x - 1]]
        elif(x == 9 and y == 0):
            choicecoords = [[y + 1, x], [y, x - 1]]
        elif(x == 0 and y == 9):
            choicecoords = [[y - 1, x], [y, x + 1]]
        elif(x == 0 and y == 0):
            choicecoords = [[y + 1, x], [y, x - 1]]
        elif(x == 0):
            choicecoords = [[y - 1, x], [y, x + 1], [y + 1, x]]
        elif(x == 9):
            choicecoords = [[y - 1, x], [y, x - 1], [y + 1, x]]
        elif(y == 0):
            choicecoords = [[y + 1, x], [y, x + 1], [y, x - 1]]
        elif(y == 9):
            choicecoords = [[y - 1, x], [y, x + 1], [y, x - 1]]
        else:
            choicecoords = [[y + 1, x], [y, x + 1], [y, x - 1], [y - 1, x]]
        print("x:", y)
        print("y:", x)
        if (not player[y][x] == 0):
                print("HIT!")
                computershots[y][x] = "!"
                for i in computershots:
                    print(i)
                miss = 0
                cbombed = player[y][x]
                player[y][x] = 100
                sinkDictC[cbombed] += 1
                if sinkDictC[cbombed] == cbombed:
                    hotcoords = [None, None]
                    compsink(cbombed)
                choose = random.choice(choicecoords)
                while True:
                    try:
                        if choose in posscordsc:
                            y = choose[0]
                            x = choose[1]
                            break
                        else:
                            choicecoords.remove(choose)
                            choose = random.choice(choicecoords)
                    except:
                        choose = random.choice(posscordsc)
                        y = choose[0]
                        x = choose[1]
                        
    if([y, x] in posscordsc):
        posscordsc.remove([y, x])
    if(len(choicecoords) > 0):
        choose = random.choice(choicecoords)
        hotcoords[0] = choose[0]
        hotcoords[1] = choose[1]
        choicecoords.remove(choose)
        print(choicecoords)
    else:
        hotcoords = [None, None]
    print("Miss")
    computershots[y][x] = "X"
    for i in computershots:
        print(i)
    miss += 1
    player_turn(sinkDictP)
                
def compsink(cbombed):
    """
    Sig: Int -> NoneType
    Checks to see if the computer sank a ship, and then subsequently if the computer won
    """
    if sinkDictC[cbombed] == cbombed:
        print("They sunk your Battleship!")
        sinkDictC.pop(sinkDictC[cbombed])
        if len(sinkDictC) == 0 and not len(sinkDictP) == 0:
            computer_win()
        else:
            computer_turn(sinkDictC)
          
def player_win():
    """
    Sig: NoneType -> NoneType
    Executes special messages to the user to tell them that they won, adds the win to their file, and asks them if they want to play again
    """
    global player
    global computer
    global file
    if not userfile == None:
        userfile.write("You won!")
        userfile.close()
    print("Congratulations! You beat the computer!")
    ans = input("Would you like to play again? ")
    if ans.upper() == "YES":
        player = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],          
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        computer = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],          
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                 
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        player_place_ships()
    elif ans.upper() == "NO":
        print("Thank you for playing!")
        userfile.close()
    else:
        ans = input("Your answer was invalid. Please enter 'yes' or 'no' and try again (not case sensitive): ")     
def computer_win():
    """
    Sig: NoneType -> NoneType
    Executes special messages to the user to tell them that they lost, adds the loss to their file, and asks them if they want to play again
    """
    global player
    global computer
    global file
    if not userfile == None:
        userfile.write("You lost")
        userfile.close()
    print("Uh oh! The computer beat you!")
    ans = input("Would you like to play again? ")
    while True:
        if ans.upper() == "YES":
            player = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],          
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                 
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
            computer = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],          
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                  
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                   
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],                 
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            player_place_ships()
        elif ans.upper() == "NO":
            print("Thank you for playing!")
            exit()
        else:
            ans = input("Your answer was invalid. Please enter 'yes' or 'no' and try again (not case senstitive): ")
begin()
