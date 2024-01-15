"""
Adventure Game
ICS3U Mr. Costello
Karan Chawla
"""

# imports
import os
import time
import random

# functions

def start():
  print ("Welcome to Mario Party!")
  time.sleep(2)
  os.system("clear")
  print ("Your job is to win the game. The fun part is that it's not so simple !")
  time.sleep(4)
  os.system("clear")
  print ("You will get 10 turns to make as much money (and stars) as possible !")
  time.sleep(5)
  os.system("clear")
  print ("Go to different map locations to find stars and explore opportunities of making money!")
  time.sleep(5)
  os.system("clear")
  print ("In between turns, there are minigames against Wario. Beware !")
  time.sleep(5)
  os.system("clear")
  print ("Be careful of the obstacles on the map such as Unlucky Squares and Countdown Mania !")
  time.sleep(5)
  os.system("clear")
  print ("Here is 10 coins to start your game!")
  time.sleep(3)
  os.system("clear")

def chooseCharacter(player):
  
  chosenCharacter = input(f"Choose {player} character from the following:\n\n\t1) Mario (Mario's Block: 1, 1, 4)\n\n\t2) Wario (Wario's Block: 0, 3, 3)\n\n\t3) Luigi (Luigi's Block: 2, 2, 2)\n\n\t4) Waluigi (Waluigi's Block: 0, 2, 4)\n\nInput: ") # displaying character list and their respective blocks
  
  while chosenCharacter != "1" and chosenCharacter != "2" and chosenCharacter != "3" and chosenCharacter != "4": # user validation
    print ("\n(You must input either 1, 2, 3, or 4. Try Again)") # must be 1, 2, 3, or 4
    chosenCharacter = input("\nInput: ") # reinput
    
  characterBlock = { # character to block dictionary for easy translation
    "1": [1,1,4],
    "2": [0,3,3],
    "3": [2,2,2],
    "4": [0,2,4]
  }

  time.sleep(1)
  os.system("clear") # clearing console after selection
  time.sleep(1)
  
  return characterBlock[chosenCharacter] # returning block

def roll(characterBlock, defaultBlock):

  rollInput = input(f"Which block do you want to roll?\n1. {characterBlock}\n2. {defaultBlock}\n\nInput: ")

  while rollInput != "1" and rollInput != "2":
    rollInput = input(f"Invalid input. Which block do you want to roll?\n1. {characterBlock}\n2. {defaultBlock}\n\nInput: ")

  if rollInput == "1":
    rollInput = characterBlock
  else:
    rollInput = defaultBlock

  tempInput = random.randint(0,2)
  tempOutput = "Rolling block."

  os.system("clear")
  
  for x in range (5):
    
    print (f"{tempOutput}")
    time.sleep(0.2)
    os.system("clear")
    print (f"{tempOutput}.")
    time.sleep(0.2)
    os.system("clear")
    print (f"{tempOutput}..")
    time.sleep(0.2)
    os.system("clear")

  print (f"You rolled {rollInput[tempInput]}!")
  return rollInput[tempInput]

def options(startingLocation, roll):

  if startingLocation == "Starting Square":
    optionsLocations = {0:["Starting Square"], 1:["Lakitu Island"], 2:["Unlucky Square 1"], 3:["Unlucky Square 2"], 4:["Countdown Mania"]}

  elif startingLocation == "Lakitu Island":
    optionsLocations = {0:["Lakitu Island"], 1:["Unlucky Square 1"], 2:["Unlucky Square 2"], 3:["Countdown Mania"], 4:["Lucky Square", "Countdown Mania", "Karting Korner"]}

  elif startingLocation == "Unlucky Square 1":
    optionsLocations = {0:["Unlucky Square 1"], 1:["Lakitu Island"], 2:["Countdown Mania"], 3: ["Karting Korner", "Ally Square", "Unlucky Square 2"], 4:["Ally Square", "Special Event", "Countdown Mania"]}

  elif startingLocation == "Karting Korner":
    optionsLocations = {0:["Karting Korner"], 1:["Ally Square"], 2:["Countdown Mania"], 3: ["Unlucky Square 2", "Item Shop"], 4:["Special Event"]}

  elif startingLocation == "Unlucky Square 2":
    optionsLocations = {0:["Unlucky Square 2"], 1:["Countdown Mania"], 2:["Lakitu Island", "Ally Square", "Lucky Square"], 3:["Special Event", "Karting Korner", "Ally Square"], 4:["Lucky Square", "Item Shop"]}

  elif startingLocation == "Countdown Mania":
    optionsLocations = {0:["Countdown Mania"], 1:["Unlucky Square 2", "Ally Square"], 2:["Karting Korner", "Special Event"], 3:["Lucky Square", "Lakitu Island", "Item Shop", "Special Event"], 4:["Special Event", "Unlucky Square 1"]}

  elif startingLocation == "Ally Square":
    optionsLocations = {0:["Ally Square"], 1:["Karting Korner", "Countdown Mania"], 2:["Unlucky Square 2", "Item Shop"], 3:["Special Event"], 4:["Lakitu Island", "Lucky Square", "Special Event"]}

  elif startingLocation == "Lucky Square":
    optionsLocations = {0:["Lucky Square"], 1:["Special Event"], 2:["Unlucky Square 2"], 3:["Countdown Mania"], 4:["Lakitu Island", "Unlucky Square 2", "Countdown Mania", "Ally Square"]}

  elif startingLocation == "Special Event":
    optionsLocations = {0:["Special Event"], 1:["Lucky Square"], 2:["Countdown Mania"], 3:["Unlucky Square", "Countdown Mania", "Ally Square"], 4:["Countdown Mania", "Ally Space", "Karting Korner"]}

  elif startingLocation == "Item Shop":
    optionsLocations = {0:["Item Shop"], 1:["Special Event"], 2:["Lucky Square"], 3:["Countdown Mania"], 4:["Unlucky Square", "Countdown Mania", "Ally Square"]}
  
  return optionsLocations[roll]

def displayOptions (options):

  print ("Please select a location to travel to:\n")
  emptyList = []

  for x in range(len(options)):
    print (f"{x+1}. {options[x]}")
    emptyList.append(str(x+1))

  locationInput = input("\nInput: ")

  while locationInput not in emptyList:
    locationInput = input("Invalid input. Input: ")

  os.system("clear")
  
  return options[int(locationInput)-1]

def locationInformation (startingLocation, coins, stars, ticks, starChance):

  if startingLocation == "Starting Square":
    
    print ("You are currently on the starting location. The starting location was home to Mario, where he enjoyed sharing his pasta with Luigi, before he had to save a certain someone from Bowser...")
    time.sleep(5)
    os.system("clear")
    print ("This is where your adventure begins ! Roll to begin your battle !")
    time.sleep(3)
    os.system("clear")
    
  elif startingLocation == "Lakitu Island":

    print ("Welcome to Lakitu Island. The potential saviour to your conquest... Lakitu has been cursed to forever grace those who confront him. ")
    time.sleep(5)
    os.system("clear")
    print ("This is your opportunity to change the game ! Lakitu island is a once in a game opportunity...")
    time.sleep(3)
    os.system("clear")

    coins, stars = lakituIsland (coins, stars)
    
  elif startingLocation == "Unlucky Square 1":

    print ("Welcome to Unluck Square 1, the first of two. First originated from the downfall of Wario's bathroom...")
    time.sleep(3)
    os.system("clear")
    print ("Unfortunately, your game will hit some obstacles")
    time.sleep(3)
    os.system("clear")

    coins, stars = unluckySquare (coins, stars)
    
  elif startingLocation == "Karting Korner":

    print ("Welcome to Karter Korner. This is where every Mario Kart game takes place. Hundreds of maps all in one. Don't forget to accelerate...")
    time.sleep(5)
    os.system("clear")

    coins, stars = kartingKorner(coins, stars)

  elif startingLocation == "Unlucky Square 2":

    print ("Welcome to Unlucky Square 2, the second of two. First originated from the downfall of Waluigi's height and chin...")
    time.sleep(3)
    print ("Unfortunately, your game will hit some obstacles")
    time.sleep(3)
    os.system("clear")

    coins, stars = unluckySquare (coins, stars)
    
  elif startingLocation == "Countdown Mania":

    print ("Welcome to Countdown Mania, the doom of everyone. When the tick becomes 0, a catastrophe occurs. Don't get Mr. Countdown MAD !")
    time.sleep(5)
    os.system("clear")

    coins, stars, ticks = countdownMania(coins, stars, ticks)
    
  elif startingLocation == "Ally Square":

    print ("Welcome to the Ally Square. This is where all tag-teams are created. Originated from Luigi's moustache, you're sure to get double trouble...")
    time.sleep(5)
    os.system("clear")

    coins, stars, starChance = allySquare(coins, stars, starChance)

  elif startingLocation == "Lucky Square":

    print ("Welcome to the Lucky Square. Unlike Unlucky Squares, everything lucky happens here. This is a defining point in the game and it stems from Donkey Kong's muscles...")
    time.sleep(5)
    os.system("clear")

    coins, stars = luckySquare(coins, stars)
    
  elif startingLocation == "Special Event":
    
    print ("Welcome to the Special Event square ! Originating from Yoshi's greeness, it celebrates all events that are unique... be careful of what you trigger...")
    time.sleep(5)
    os.system("clear")

    coins, stars, ticks, starChance = specialEvent(coins, stars, ticks, starChance)
    
  elif startingLocation == "Item Shop":

    print ("Welcome to the Item Shop ! Here's where you can buy important items that can alter the course of the game. All items were harvested from Mario's plumber...")
    time.sleep(5)
    os.system("clear")

    coins, stars, ticks, starChance = itemShop(coins, stars, ticks, starChance)


  return coins, stars, ticks, starChance
  
def lakituIsland (coins, stars):

  print ("Here at Lakitu Island you have options...Either to get a star or to get more coins !")
  time.sleep(4)
  os.system("clear")

  userSelection = input("Would you like to...\n\t1. Buy a star (20 coins required)\nOR\n\t2. Get coins (10 coins)\n\ninput: ")

  if userSelection == "1" and coins < 20:
    print ("\nUnfortunately you don't have enough money to buy a star...")
    userSelection = "2"

  if userSelection == "1":
    stars += 1
    print (f"\nYou now have {stars} stars !")
    
  if userSelection == "2":
    coins += 10
    print (f"\nYou now have {coins} coins !")

  time.sleep(3)
  os.system("clear")
  
  return coins, stars

def unluckySquare(coins, stars):

  print ("Here at unlucky squares you have 0 options...everything is decided for you !")
  time.sleep(4)
  os.system("clear")

  print ("\t1. Lose 5 coins\n\t2. Lose 10 coins\n\t3. Lose 3 coins\n\t4. Lose a star")
  time.sleep(4)
  randomNumber = random.randint(1, 4)

  if randomNumber == 1:
    coins -= 5
    print (f"\n1 was selected ! You now have {coins} coins...")
  elif randomNumber == 2:
    coins -= 10
    print (f"\n2 was selected ! You now have {coins} coins...")
  elif randomNumber == 3:
    coins -= 3
    print (f"\n3 was selected ! You now have {coins} coins...")
  else:
    if stars > 0:
      stars -= 1
  
    print (f"\n4 was selected ! You now have {stars} stars ")

  time.sleep(3)
  os.system("clear")
  return coins, stars

def kartingKorner (coins, stars):
  
  print ("This is a reaction test ! The better you do, the more you coins you recieve ! You will see a direction on the screen, and you will need to input a respective letter.")
  time.sleep(5)
  os.system("clear")

  print ("Direction to letter chart:\n\tForward = 'w'\n\tBackward = 's'\n\tLeft = 'a'\n\tRight = 'd'")
  time.sleep(5)
  os.system("clear")

  Directions = ["Forward", "Backward", "Left", "Right"]
  Answers = ["w", "s", "a", "d"]

  Correct = 0
  for x in range(10):
    randomIndex = random.randint(0,3)

    print (Directions[randomIndex])
    userAnswer = input("\ninput: ")

    if userAnswer == Answers[randomIndex]:
      print ("\nCorrect!")
      Correct += 1

    else:
      print ("\nIncorrect")

    time.sleep(3)
    os.system("clear")
    
  print (f"You got {Correct} answers correct !")

  coins += Correct

  print (f"You now have {coins} coins !")

  time.sleep(3)
  os.system("clear")
  
  return coins, stars

def countdownMania (coins, stars, ticks):

  print ("You've arrived at COUNTDOWN MANIA !")
  ticks -= 1
  print (f"Mr. Countdown is now at {ticks} ticks...")

  time.sleep(5)
  os.system("clear")
  
  if ticks <= 0:
    ticks = 3
    
    print ("You've erupted Mr. Countdown !")
    print ("You will now lose half your money and half your stars!")

    coins = int(coins/2)
    stars = int(stars/2)

    print (f"You now have {coins} coins and {stars} stars")

  return coins, stars, ticks

def allySquare (coins, stars, starChance):

  if starChance != 4:
    print ("This is your chance to get an ally on your team !")
    time.sleep(3)
    os.system("clear")
  
    print ("Joining your team is Daisy ! She doubles your chances of recieving a star !")
  
    starChance = 2

  else:
    print ("You've already recieved your ally this game !")

  return coins, stars, starChance

def luckySquare(coins, stars):

  print ("Here at lucky square you have an opportunity to win BIG ! A random generator will select your reward...")
  time.sleep(4)
  os.system("clear")

  print ("\t1. Win 5 coins\n\t2. Win 10 coins\n\t3. Win 3 coins\n\t4. Win a star")
  
  time.sleep(4)
  randomNumber = random.randint(1, 4)

  if randomNumber == 1:
    coins += 5
    print (f"\n1 was selected ! You now have {coins} coins...")
  elif randomNumber == 2:
    coins += 10
    print (f"\n1 was selected ! You now have {coins} coins...")
  elif randomNumber == 3:
    coins += 3
    print (f"\n1 was selected ! You now have {coins} coins...")
  else:
    stars += 1
  
    print (f"\n4 was selected ! You now have {stars} stars ")

  time.sleep(3)
  os.system("clear")
  return coins, stars

def specialEvent(coins, stars, ticks, starChance):

  print ("A random event will occur from the following list ! hope it's not bad...")

  print ("\t1. Decrease Mr. Countdown's ticks\n\t2. Increase star chance\n\t3. Lose a star\n\t4. Win a star")
  
  time.sleep(4)
  randomNumber = random.randint(1, 4)

  if randomNumber == 1:
    ticks -= 1
    print (f"\n1 was selected ! Mr. Countdown is now at {ticks} ticks")
  elif randomNumber == 2:
    starChance = 2
    print ("\n2 was selected ! You now have a 50% chance at winning a star every round")
  elif randomNumber == 3:
    stars -= 1
    print (f"\n3 was selected ! You now have {stars} stars...")
  else:
    stars += 1
  
    print (f"\n4 was selected ! You now have {stars} stars ")

  time.sleep(3)
  os.system("clear")
  
  return coins, stars, ticks, starChance

def itemShop (coins, stars, ticks, starChance):

  print ("Purchase an item from the following list:\n\t1. a Star (25 coins)\n\t2. Increase Mr. Countdown ticks (10 coins)\n\t3. Increase star chance (40 coins)\n\t4. 10 coins (free)")

  userSelection = input("Input: ")

  if userSelection == "1":
    stars += 1
    print (f"\nYou now have {stars} stars")

  elif userSelection == "2":
    ticks += 1
    print (f"\nMr. Countdown now has {ticks} ticks")

  elif userSelection == "3":
    starChance = 2
    print ("\nYou now have a 50% star chance !")

  else:
    coins += 10
    print (f"\nYou now have {coins} coins")

  return coins, stars, ticks, starChance

def starGame(stars, chance):

  os.system("clear")
  randomNumber = random.randint(1, chance)

  tempOutput = "Digging for star."

  os.system("clear")
  
  for x in range (5):
    
    print (f"{tempOutput}")
    time.sleep(0.2)
    os.system("clear")
    print (f"{tempOutput}.")
    time.sleep(0.2)
    os.system("clear")
    print (f"{tempOutput}..")
    time.sleep(0.2)
    os.system("clear")
    
  if randomNumber == 2:
    print ("You found a star !")
    stars += 1
  else:
    print ("No star found !")

  time.sleep(3)
  os.system("clear")

  return stars
  

def miniGame(coins):

  print ("Welcome to the Minigame round brought to you by Wario !")
  time.sleep(3)
  os.system("clear")
  
  print ("Contestants will battle it out with each to determine one winner that wins BIG...")
  time.sleep(3)
  os.system("clear")

  tempOutput = "This round's game is."

  os.system("clear")
  
  for x in range (5):
    
    print (f"{tempOutput}")
    time.sleep(0.2)
    os.system("clear")
    print (f"{tempOutput}.")
    time.sleep(0.2)
    os.system("clear")
    print (f"{tempOutput}..")
    time.sleep(0.2)
    os.system("clear")

  randomSelection = random.randint(1,4)

  if randomSelection == 1:
    print ("Rock Paper Scissors !")

    userSelection = int(input("\nInput (1 - rock, 2 - paper, 3 - scissors): "))

    while userSelection != 1 and userSelection != 2 and userSelection != 3:
        userSelection = int(input("\nInput Error. Input (1 - rock, 2 - paper, 3 - scissors): "))
    indextoMaterial = ["Rock", "Paper", "Scissors"]
    
    warioSelection = random.randint(1,3)

    print (f"\nYou selected {indextoMaterial[userSelection-1]}")
    print (f"\nWario selected {indextoMaterial[warioSelection-1]}")
    
    if userSelection == warioSelection:
      print ("\nTie!")

    if userSelection == warioSelection + 1 or userSelection == warioSelection - 2:
      print ("\n You win !")
      coins += 10
      print (f"\n You now have {coins} coins")
      time.sleep(4)
      os.system("clear")

    else:
      print ("\n You lose !")
      coins -= 5
      print (f"\n You now have {coins} coins")
      time.sleep(4)
      os.system("clear")
      
  elif randomSelection == 2:
    print ("Guess the number !")

    randomNumber = random.randint(1, 100)

    userSelection = int(input("\nInput a number from 1 - 100: "))
    warioSelection = random.randint(1,100)

    print (f"\nYou picked {userSelection}, Wario picked {warioSelection}...The number is {randomNumber} !")
    
    if abs(randomNumber-userSelection) < abs(randomNumber-warioSelection):
      print ("\n You win !")
      coins += 10
      print (f"\n You now have {coins} coins")
      time.sleep(4)
      os.system("clear")
    else:
      print ("\n You lose !")
      coins -= 5
      print (f"\n You now have {coins} coins")
      time.sleep(4)
      os.system("clear")

  elif randomSelection == 3:
    print ("Math Clash !")

    correct = 0
    
    for x in range(1, 11):
      multiple = random.randint(2, 12)

      userInput = int(input(f"\nWhat is {multiple} * {x}: "))

      if userInput == multiple * x:
        correct += 1

    warioCorrect = random.randint(1, 10)

    print (f"\nYou got {correct} correct, Wario got {warioCorrect} correct...")
    
    if correct > warioCorrect:
      print ("\n You win !")
      coins += 10
      print (f"\n You now have {coins} coins")
      time.sleep(4)
      os.system("clear")      
    else:
      print ("\n You lose !")
      coins -= 5
      print (f"\n You now have {coins} coins")
      time.sleep(4)
      os.system("clear")
      
  elif randomSelection == 4:
    print ("Typing Test !")

    userInput = input("\n Type the following text 'Hello, my name is Mario, the king of all characters. With my plumbing skills and moustache I'm sure to defeat any conquest!' \n\ninput: ")

    if userInput == "Hello, my name is Mario, the king of all characters. With my plumbing skills and moustache I'm sure to defeat any conquest!":
      print ("\n You win !")
      coins += 10
      print (f"\n You now have {coins} coins")
      time.sleep(4)
      os.system("clear")  

    else:
      print ("\n You lose !")
      coins -= 5
      print (f"\n You now have {coins} coins")
      time.sleep(4)
      os.system("clear")
      
  print ("Minigame round over !")

  time.sleep(2)
  os.system("clear")

  return coins

start()

defaultBlock = [1,2,3]

userBlock = chooseCharacter("YOUR OWN") # choosing user block

countdownTicks = 3

starChance = 4

userCoins = 10
userStars = 0
userLocation = "Starting Square"
userCoins, userStars, countdownTicks, starChance = locationInformation(userLocation, userCoins, userStars, countdownTicks, starChance)


for x in range (1, 11):

  print (f"Round {x}")
  time.sleep(2)
  os.system("clear")
  
  userRoll = roll(userBlock, defaultBlock)

  userOptions = options(userLocation, userRoll)

  userLocation = displayOptions (userOptions)

  userStars = starGame(userStars, starChance)
  
  userCoins, userStars, countdownTicks, starChance = locationInformation(userLocation, userCoins, userStars, countdownTicks, starChance)

  userCoins = miniGame(userCoins)

if userStars*30 + userCoins > 110:
  print ("Congratulations ! You beat the game.")
else:
  print ("You lost the game...")