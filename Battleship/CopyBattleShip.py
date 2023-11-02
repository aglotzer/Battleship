#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 08:55:12 2021

@author: alexglotzer
"""
import random
import copy

from turtle import *
from tkinter import *
global wn
global t
size = 0
way = None
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
posscordscc = [[0,2], [1,2], [2,2], [3,2], [4,2], [9, 0], [5, 8], [5,7], [5, 6], [5, 5], [0, 8], [1, 8], [7, 2], [7, 3], [7, 4]]
rangesplace = []
rangesguess = []
x = -520
y = 350
i = 0
while i < 10:
    j = 0
    temp=[]
    while j < 10:
        temp.append([[x, x+45], [y, y-45]])
        x += 45
        j += 1
    i += 1
    y -= 45
    x = -520
    rangesplace.append(temp)

x = 120
y = 350
i = 0
while i < 10:
    j = 0
    while j < 10:
        temp = []
        temp.append([[x, x+45], [y, y-45]])
        x += 45
        j += 1
    rangesplace.append(temp)
    i += 1
    y -= 45
    x = 120


player = [[0, 0, 5, 0, 0, 0, 0, 0, 2, 0],
          
          [0, 0, 5, 0, 0, 0, 0, 0, 2, 0],
          
          [0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 5, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 4, 4, 4, 4, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


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
print("Possible:", posscordsc)
userfile = None

def button(x, y):
        if x in range(130, 330) and y in range(-100, 0):
            print("login")
            login()
        elif x in range(-330,-130) and y in range(-100,0):
            print("signup")
            signup()
        elif x in range(-100, 100) and y in range(-200, -100):
            print("guest")
            guest()

def begin():
    global wn
    screen = Screen()
    screen.setup(710, 444)

    wn = Screen()
    wn.bgpic("thumb2-uss-billings-aerial-view-littoral-combat-ships-united-states-navy-lcs-15.gif")
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0, 100)
    turtle.write("Battleship",False,"center",("Phosphate",35,"normal"))
    turtle._tracer(0,0)
    turtle.hideturtle()
    turtle.pu()
    turtle.goto(-330,0)
    turtle.pensize(5)
    turtle.color("black")
    turtle.pd()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.pu()
    turtle.goto(230,-65)
    turtle.color("white")
    turtle.write("Login",False,"center",("oswald",35,"normal"))
    turtle.color("black")
    turtle.goto(330,0)
    turtle.pensize(5)
    turtle.pd()
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle._update()
    turtle.pu()
    turtle.goto(-230,-65)
    turtle.color("white")
    turtle.write("Sign Up",False,"center",("oswald",35,"normal"))
    turtle.color("black")
    turtle.goto(100,-100)
    turtle.pensize(5)
    turtle.pd()
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(100)
    turtle._update()
    turtle.pu()
    turtle.goto(0,-170)
    turtle.color("white")
    turtle.write("Guest",False,"center",("oswald",35,"normal"))
    wn.onclick(button)


def signup():
    global wn
    wn.clear()
    wn = Screen()
    wn.setup(800, 800)
    turtle = Turtle()
    turtle.clear()
    turtle.hideturtle()
    turtle._tracer(0,0)
    turtle.penup()
    username = wn.textinput("Username", "Enter a username")
    password = wn.textinput("Password", "Enter a password")
    conf = wn.textinput("Confirm Password", "Please confirm your password")
    while (not password == conf):
        if (password == conf):
            name = username + ".txt"
            file = open(name, "a")
            file.write(password)
            file.close()
            break
        else:
            conf = screen.textinput("Try Again", "Passwords did not match. Try again.")
    draw_board()
    #player_place_ships()
    return file

def login():
    global wn
    wn.clear()
    wn = Screen()
    wn.setup(800, 800)
    turtle = Turtle()
    turtle.clear()
    turtle.hideturtle()
    turtle._tracer(0,0)
    turtle.penup()
    username = wn.textinput("Username", "Enter your username")
    password = wn.textinput("Password", "Enter your password")
    name = username + ".txt"
    i = 0
    while (i < 5):
        file = open(name, "r")
        if not (password == file.readline()):
            file.close()
            i += 1
            password = screen.textinput("Password", "Password Incorrect. Try Again.")
        else:
            draw_board()
            #player_place_ships()
            return file
    print("You were wrong too many times. Please go back to the beginning and try again.")
    begin()
    
    
def guest():
    global wn
    wn.clear()
    wn = Screen()
    wn.setup(800, 800)
    turtle = Turtle()
    turtle.clear()
    turtle.hideturtle()
    turtle._tracer(0,0)
    draw_board()
    #player_place_ships()
    return  

def draw_board():
    
    wn = Screen()
    wn.setup(1400,1000) #sets resolution to 400x400
    
    #make turtle and stealth it
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    i = 0
    x = 120
    y = 350
    while i < 10:
        j = 0
        while j < 10:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.forward(45) # Forward turtle by s units
            t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
            t.forward(45) # Forward turtle by s units
            t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
            t.forward(45) # Forward turtle by s units
            t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
            t.forward(45) # Forward turtle by s units
            t.left(90)
            x += 45
            j += 1
        y -= 45
        x = 120
        i += 1
    i = 0
    x = -520
    y = 350
    while i < 10:
        j = 0
        while j < 10:
            t.penup()
            t.goto(x, y)
            t.pendown()
            t.forward(45) # Forward turtle by s units
            t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
            t.forward(45) # Forward turtle by s units
            t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
            t.forward(45) # Forward turtle by s units
            t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
            t.forward(45) # Forward turtle by s units
            t.left(90)
            x+= 45
            j += 1
        y -= 45
        x = -520
        i += 1

    
    j = 0
    x = -600
    y = -150
    while j < 5:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
                 
                # drawing second side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
                 
                # drawing third side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
                 
                # drawing fourth side
        t.forward(45) 
        t.left(90)
        x+= 45
        j += 1
        y -= 45
        x = -600


    j = 0
    x = -450
    y = -150
    while j < 5:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
        t.forward(45) # Forward turtle by s units
        t.left(90)
        x += 45
        j += 1
        y -= 45
        y = -150

    j = 0
    x = -450
    y = -300
    while j < 4:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
        t.forward(45) # Forward turtle by s units
        t.left(90)
        x += 45
        j += 1
        y -= 45
        y = -300

    j = 0
    x = -150
    y = -150
    while j < 4:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
        t.forward(45) # Forward turtle by s units
        t.left(90)
        x += 45
        j += 1
        y -= 45
        x = -150
    
    j = 0
    x = -50
    y = -150
    while j < 3:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
        t.forward(45) # Forward turtle by s units
        t.left(90)
        x += 45
        j += 1
        y -= 45
        y = -150

    j = 0
    x = 250
    y = -150
    while j < 3:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
        t.forward(45) # Forward turtle by s units
        t.left(90)
        x += 45
        j += 1
        y -= 45
        x = 250

    j = 0
    x = -50
    y = -275
    while j < 2:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
        t.forward(45) # Forward turtle by s units
        t.left(90)
        x += 45
        j += 1
        y -= 45
        y = -275

    j = 0
    x = 150
    y = -150
    while j < 2:
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
        t.forward(45) # Forward turtle by s units
        t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
        t.forward(45) # Forward turtle by s units
        t.left(90)
        x += 45
        j += 1
        y -= 45
        x = 150

    x = 150
    y = -270
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(45) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
             
            # drawing second side
    t.forward(45) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
             
            # drawing third side
    t.forward(45) # Forward turtle by s units
    t.left(90) # Turn turtle by 90 degree
             
            # drawing fourth side
    t.forward(45) # Forward turtle by s units
    t.left(90)
    player_place_ships()
    
def validvp(x, y, size):
    validity = False
    i = 1
    if (x < 10 and y < 10 and x >= 0 and y >= 0):
        print("Valid if")
        while (i < size):
            print("valid loop")
            if(x + i < 10 and x + i > 0 and player[y][x+i] == 0):
                print("valid loop if")
                i += 1
                print("valid return true")
            else:
                print("valid loop else return")
                return validity
        validity = True
        return validity
    else:
        print("valid else return")
        return validity

def validhp(x, y, size):
    validity = False
    i = 1
    if (x < 10 and y < 10 and x >= 0 and y >= 0):
        print("Valid if")
        while (i < size):
            print("valid loop")
            if(y + i < 10 and y + i > 0 and player[y+i][x] == 0):
                print("valid loop if")
                i += 1
            else:
                print("valid loop else return")
                return validity
        validity = True
        return validity
    else:
        print("valid else return")
        return validity
    
def validvc(x, y, size):
    validity = False
    i = 1
    if (x < 10 and y < 10 and x >= 0 and y >= 0):
        print("Valid if")
        while (i < size):
            print("valid loop")
            if(x + i < 10 and x + i >= 0 and computer[y][x+i] == 0):
                print("valid loop if")
                i += 1
                print("valid return true")
            else:
                print("valid loop else return")
                return validity
        validity = True
        return validity
    else:
        print("valid else return")
        return validity

def validhc(x, y, size):
    validity = False
    i = 1
    if (x < 10 and y < 10 and x >= 0 and y >= 0):
        print("Valid if")
        while (i < size):
            print("valid loop")
            if(y + i < 10 and y + i >= 0 and computer[y+i][x] == 0):
                print("valid loop if")
                i += 1
            else:
                print("valid loop else return")
                return validity
        validity = True
        return validity
    else:
        print("valid else return")
        return validity

def button2(x, y):
    global wn
    print("button 2")
    print("x", x, "y", y)
    print(rangesplace)
    i = 0
    while i < len(rangesplace):
        j = 0
        while j < len(rangesplace[i]):
            if(x in range(rangesplace[i][j][0][0], rangesplace[i][j][0][1]) and y in range(rangesplace[i][j][1][0], rangesplace[i][j][1][1])):
                print("big if")
                if way == "vertical":
                   validpv(j, i, size)
                elif way == "horizontal":
                   validph(j, i, size)
            else:
                j += 1
        i += 1

def button1(x, y):
    global size
    global way
    if x in range(-600, -555) and y in range(-330, -105):
        print("5 vert")
        size = 5
        way = "vertical"
        print("button 2 call")
        wn.onscreenclick(button2)
    elif x in range(-450, -225) and y in range(-150, -105):
        print("5 hor")
        size = 5
        way = "horizontal"
        wn.onscreenclick(button2)
    elif x in range(-150, -105) and y in range(-285, -105):
        print("4 vert")
        size = 4
        way = "vertical"
        wn.onscreenclick(button2)
    elif x in range(-450, -270) and y in range(-300, -255):
        print("4 hor")
        size = 4
        way = "horizontal"
        wn.onscreenclick(button2)
    elif x in range(250, 295) and y in range(-240, -105):
        print("3 vert")
        size = 3
        way = "vertical"
        wn.onscreenclick(button2)
    elif x in range(-50, 85) and y in range(-150, -105):
        print("3 hor")
        size = 3
        way = "horizontal"
        wn.onscreenclick(button2)
    elif x in range(150, 195) and y in range(-195, -105):
        print("2 vert")
        size = 2
        way = "vertical"
        wn.onscreenclick(button2)
    elif x in range(-50, 40) and y in range(-275, -230):
        print("2 hor")
        size = 2
        way = "horizontal"
        wn.onscreenclick(button2)
    elif x in range(150, 195) and y in range(-275, -230):
        print("1 vert")
        size = 1
        way = "vertical"
        wn.onscreenclick(button2)
    print("x", x, "y", y)
def player_place_ships():
    global t
    global wn
    ships = [5, 4, 3, 2, 1]
    #while (len(ships) > 0):
    print("You have", len(ships), "left. They are size", ships)
    wn.onclick(button1)
    """
        while True:
            #placement = input("Please enter the coordinates between [0, 0] and [9, 9] for the front of the ship like this: '5,2' ")
            #way = input("Please enter horizontal or vertical: ")
            x = int(placement[:1])
            print(x)
            y = int(placement[2:])
            print(y)
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
    print(player)
    print(computer)
    computer_place_ships()
    """
  
def computer_place_ships():
    print(computer)
    ships = [5, 4, 3, 2, 1]
    while (len(ships) > 0):
        ways = ["horizontal", "vertical"]
        size = ships[random.randint(0, len(ships)-1)]
        way = ways[random.randint(0, len(ways)-1)]
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if(way.upper() == "HORIZONTAL" and validhc(x, y, size)):
            i = 0
            print(size, "hor")
            while (i < size):
                computer[x][y + i] = size
                i += 1
            ships.remove(size)
            
        elif(way.upper() == "VERTICAL" and validvc(x, y, size)):
            i = 0
            print(size, "vert")
            while (i < size):
                computer[x + i][y] = size
                i += 1
            ships.remove(size)
    print(computer)
    player_turn(sinkDictP)
            
def player_turn(sinkDictP):
    target = input("In the same coordinate form, please enter a target: ")
    x = int(target[:1])
    y = int(target[2:])
    if (not computer[y][x] == 0 and [y, x] in posscordsp):
        posscordsp.remove([y, x])
        sinkDictP[computer[y][x]] += 1
        print("HIT!")
        pbombed = computer[y][x]
        computer[y][x] = 100
        if (sinkDictP[pbombed] == pbombed):
            print("You sunk their Battleship!")
            sinkDictP.pop(sinkDictP[pbombed])
            if len(sinkDictP) == 0 and not len(sinkDictC) == 0:
                player_win()
        player_turn(sinkDictP)
    else:
        print("Miss")
        computer_turn(sinkDictC)
    

def computer_turn(sinkDictC):
    global hotcoords
    global choicecoords
    global comphit
    global miss
    print("Misses:", miss)
    if (not miss == 0 and miss % 5 == 0):
        print("miss if")
        chosen = random.choice(posscordscc)
        print(chosen)
        print(posscordscc)
        y = chosen[0]
        x = chosen[1]
        print("y", y, "x", x)
        posscordscc.remove(chosen)
    else:
        choose = random.choice(posscordsc)
        y = choose[0]
        x = choose[1]
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
    print(posscordsc)
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
        print(choicecoords)
        print("x:", y)
        print("y:", x)
        if (not player[y][x] == 0):
                print("HIT!")
                miss = 0
                print("Player coordinate", player[y][x])
                cbombed = player[y][x]
                print("Bombed:", cbombed)
                print("Bombed if")
                player[y][x] = 100
                sinkDictC[cbombed] += 1
                if sinkDictC[cbombed] == cbombed:
                    print("Bombed")
                    hotcoords = [None, None]
                    compsink(cbombed)
                choose = random.choice(choicecoords)
                print("List:", choicecoords)
                print("Choice:", choose)
                while True:
                    if choose in posscordsc:
                        y = choose[0]
                        x = choose[1]
                        break
                    else:
                        choicecoords.remove(choose)
                        choose = random.choice(choicecoords)
                choicecoords.remove(choose)   
                print(sinkDictC)
                print(player)
    if([y, x] in posscordsc):
        posscordsc.remove([y, x])
    print("Hotcoords if")
    if(len(choicecoords) > 0):
        print("Assignment")
        choose = random.choice(choicecoords)
        print("Choice:", choose)
        hotcoords[0] = choose[0]
        hotcoords[1] = choose[1]
        print("Hot 1", hotcoords[0], "Hot 2", hotcoords[1])
        choicecoords.remove(choose)
        print(choicecoords)
    else:
        hotcoords = [None, None]
    print(hitlistC)
    print("Miss")
    miss += 1
    print(sinkDictC)
    player_turn(sinkDictP)
                
def compsink(cbombed):
    if sinkDictC[cbombed] == cbombed:
        print("They sunk your Battleship!")
        sinkDictC.pop(sinkDictC[cbombed])
        compwin = False
        playwin = False
        i = 0
        while i < 10:
            j = 0
            while j < 10:
                if not computer[i][j] == 0 and not computer[i][j] == 100:
                    compwin = False
                else:
                    compwin = True
        i = 0
        while i < 10:
            j = 0
            while j < 10:
                if not player[i][j] == 0 and not player[i][j] == 100:
                    playwin = False
                else:
                    playwin = True
        if (compwin and not playwin):
            computer_win()
        computer_turn(sinkDictC)
    else:
        return
          
def player_win():
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
    global player
    global computer
    global file
    if not userfile == None:
        userfile.write("You lost")
        userfile.close()
    print("Uh oh! The computer beat you!")
    ans = input("Would you like to play again? ")
    while not (ans.upper() == "YES" and ans.upper() == "NO"):
        if ans.upper() == "YES":
            
            player = [[None, None, None, None, None, None, None, None, None, None],
          
                      [None, None, None, None, None, None, None, None, None, None],
                      
                      [None, None, None, None, None, None, None, None, None, None],
                      
                      [None, None, None, None, None, None, None, None, None, None],
                      
                      [None, None, None, None, None, None, None, None, None, None],
                      
                      [None, None, None, None, None, None, None, None, None, None],
                      
                      [None, None, None, None, None, None, None, None, None, None],
                      
                      [None, None, None, None, None, None, None, None, None, None],
                      
                      [None, None, None, None, None, None, None, None, None, None],
                      
                      [None, None, None, None, None, None, None, None, None, None],
                      
                      [None, None, None, None, None, None, None, None, None, None]]

            computer = [[None, None, None, None, None, None, None, None, None, None],
                  
                        [None, None, None, None, None, None, None, None, None, None],
                  
                        [None, None, None, None, None, None, None, None, None, None],
                  
                        [None, None, None, None, None, None, None, None, None, None],
                  
                        [None, None, None, None, None, None, None, None, None, None],
                  
                        [None, None, None, None, None, None, None, None, None, None],
                  
                        [None, None, None, None, None, None, None, None, None, None],
                  
                        [None, None, None, None, None, None, None, None, None, None],
                  
                        [None, None, None, None, None, None, None, None, None, None],
                  
                        [None, None, None, None, None, None, None, None, None, None],
                      
                        [None, None, None, None, None, None, None, None, None, None]]
            player_place_ships()
        elif ans.upper() == "NO":
            print("Thank you for playing!")
            file.close()
        else:
            ans = input("Your answer was invalid. Please enter 'yes' or 'no' and try again (not case senstitive): ")     

begin()
