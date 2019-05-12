#README: This file is a spin off minecraft through a fun text adventure game  !
#Through helping code this game you will learn awesome techniques such as spreading
#input, lists, sleep functionjs, if conditionals, and for loops!

#NOTE: if you finish early, feel free to add your own spin on to the game with the skills you have learned!!!

#imports time package to support time.sleep
import _____ #TODO

#creates a list to make answers of user input not case sensitive (You will see later :D)
answer_F = ["F", "f"]
answer_A = ["___", "___"] // #TODO
answer_B = [__, __] #TODO
yes = [__, __, __,__] #TODO
no = [__, __, __,__] #TODO

#intro that mocks  generating and initializing a minecraft world
def intro():
  print("+----ONLY WORKS IN Python 3.7 IDLE----+")
  print("+----switch to fullscreen mode in IDLE for full experiance----+")

  #time.sleep function halts program execution for 1.5 seconds
  _______ #TODO

  #ascii art!
  print('''
█████████████████
█░░░░░░░░░░░░░░░█
█░░░░░░░░░░░░░░░█
█░░████░░░████░░█
█░░████░░░████░░█
█░░░░░░███░░░░░░█
█░░░░███████░░░░█
█░░░░███████░░░░█
█░░░░██░░░██░░░░█
█░░░░░░░░░░░░░░░█
█████████████████
''')

  # How do we print "loading resource packs...." in the line below?
  _______ #TODO

  time.sleep(1)
  print("......47%")
  time.sleep(1)
  print(".........74%")
  time.sleep(1)
  print("...............100%")
  time.sleep(1)
  print("")
  time.sleep(1)

  print('''
░░░░░░░░░░░░░░░░▄▓▄
░░░░▄█▄░░░░░░░░▄▓▓▓▄
░░▄█████▄░░░░░▄▓▓▓▓▓▄
░▀██┼█┼██▀░░░▄▓▓▓▓▓▓▓▄
▄▄███████▄▄▄▄▄▄▄▄█▄▄▄▄
      ''')
  print("+----------------------------------------------------------------------------+")
  print("")

  print("Generating World....")
  time.sleep(1)
  print("......27%")
  time.sleep(1)
  print(".........64%")
  time.sleep(1)
  print("................100%")
  time.sleep(0.5)
  print('''
──▒▒▒▒▒▒▒▒───▒▒▒▒▒▒▒▒
─▒▐▒▐▒▒▒▒▌▒─▒▒▌▒▒▐▒▒▌▒
──▒▀▄█▒▄▀▒───▒▀▄▒▌▄▀▒
─────██─────────██
░░░▄▄██▄░░░░░░░▄██▄░░░
    ''')
  print("+----------------------------------------------------------------------------+")
  print("")

  print("Initializing Server......... (this may take a moment)")
  time.sleep(1)
  print("......57%")
  time.sleep(1)
  print(".........84%")
  time.sleep(2)
  print("...............99%")
  time.sleep(3)
  print("")
  print("+----------------------------------------------------------------------------+")
  print("17:26 World Created")
  print("")

  print('''
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
       ''')
  print("+----------------------------------------------------------------------------+")

  time.sleep(1)

  #This is the way we will be using to output an animated message to our console!
  welcomeMessage = "Welcome to Textcraft! would you like to read the tutorial? (y/n)"

  #for loop that iterates through all the characters in string welcome
  for ___ in _____: #TODO
    #prints every character of that string on the same string, using end='' prevents a new line
    print (___ , ___) #TODO
    #sleep time for the animation (feel free to use whatever time you want!)
    time.sleep(___) #TODO

  #for scanning user input
  choice = ("\n_____ ") #TODO

  #conditional statement if choice is in yes array
  ___________ #TODO
      time.sleep(1)
      print("\nTextcraft is a game of infinitely-generated worlds of wide open terrain")
      print("journey through icy mountains, swampy bayous, vast pastures and much more")
      print("filled with secrets, wonders and peril! survive, build, mine, thrive!")
      time.sleep(1)
      print("\nLet the adventure begin :3")

  #if user does not want to read the tutorial
  ______ #TODO
    time.sleep(1)
    print("\nLet the adventure begin :3")


#method for setting up plot of game!
def setup():
  time.sleep(1)
  print("")
  print("\n+----------------------------------------------------------------------------+")
  print("|Weapon:Fists|HP:10|Attack:5|Hunger:4|")
  print("\n+----------------------------------------------------------------------------+")

  #asks user for their name
  _____ = "Ah.... you have ventured far to get to this world! What is your name traveler?\n"
  for ____ in _____
    print (___ , ___)
    time.sleep(.04)

  #How do we make name equal to scanner input??
  name = _____ #TODO

  #name created log
  time.sleep(0.5)
  print("\n17:27 Name Created")

  #grabs name variable defined above and prints a welcome message
  print("\nWelcome to the world " + ______ + "!")
  time.sleep(0.5)

  #prompts user a message on the choices they want to make
  i = "\nMy name is Steve, what would you like to do today?"
  for char in intro:
   ______ #TODO, how do we iterate through every character for a string?
    time.sleep(.04)

  time.sleep(.05)

#starts the actual choice part of our RPG!
def choice():

  print("\n+----------------------------------------------------------------------------+")
  print("\nA. Mine!")
  print("B. Explore!")
  print("\n+----------------------------------------------------------------------------+")

  #choice variable equal to user input
  choice = _____ #TODO

  #cases where A or B is chosen, these methods are to be called~
  ______________ #TODO
    mine()

  #how method would we need to call if user chooses answer B?
  elif choice in answer_B:
    _______ #TODO

  #case where the user throws an illegal argument
  else:
    print("")
    print('''
║║║░░▄██║║║║░░░▄█░╔╗
╚╬╝░██▄█╬╬╬╬╬╬███░║║
░║░░░▀██║║║║░░░▀█░╠╝
░║░░░░░░░░░░░░░░░░║
      ''')
    #print your own illegal argument message
    print (___________________) #TODO


#when user chooses to mine, mine function is called
def mine():

  #mocks coordinates of users in minecraft
  time.sleep(1)
  print("X:-762 Z:12 Y:300")
  time.sleep(1)
  print('''
  .    '    ,
     _______
_  .`_|___|_`.  _
    \ \   / /
     \ ' ' /
      \ " /
       \./
        V

    ''')

  #getting a bit harder now, how do we animate and print this string? look at past examples??
  mineMessage= "\nAfter 20 minutes of mining cobble and gravel you manage to find diamonds! :o\n"
    _____________________ #TODO
      _____________ #TODO
      _____________ #TODO

  #prompts user with choice what to do with those diamonds
  print("\n+----------------------------------------------------------------------------+")
  print("A. Mine the diamond block below you")
  print("B. Build back up to the surface")
  print("\n+----------------------------------------------------------------------------+")

  #new choice equal to user input, remember this is a local variable so choice can be used again
  choice = ______ #TODO

  #if inputted choice in list A
  ___________________ #TODO
    mineDiamond()
  #if user chooses build
  elif choice in answer_B:


    building = "building......"
    #iterates through every char in building string
    for ____ in _________: #TODO
      print (___,___) #TODO
       time.sleep(_____) #TODO

    #sleep and print statements to simulate building
    time.sleep(1)
    print("\n.................")
    time.sleep(1)
    print("..........................\n")
    time.sleep(1.3)
    print("You are mining and building straight up when sand blocks fall on you ;-;")
    #calls dieing method
    _______ #TODO
    #if user inputs illegal argument

  else:
    print("")
    print('''
║║║░░▄██║║║║░░░▄█░╔╗
╚╬╝░██▄█╬╬╬╬╬╬███░║║
░║░░░▀██║║║║░░░▀█░╠╝
░║░░░░░░░░░░░░░░░░║
      ''')
    print ("Illegal Argument, ;-; you may have typed something in wrong")

#case where user wants to mine diamond
def mineDiamond():

      #how do we animate this string?
      mining = "mining......"
      _______________ #TODO

      time.sleep(1)
      print("\n.................")
      time.sleep(1)
      print("..........................\n")
      time.sleep(1.3)
      print("NOOO THERE WAS LAVA UNDER THE BLOCK ;-;\n")
      #calls dieing method
      dieing()

#if user decides to explore instead
def explore():
  print("X:1200 Z:132 Y:708")
  print("biome: desert")
  print('''
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▄▄▄▒▒▒█▒▒▒▒▄▒▒▒▒▒▒▒▒S
▒█▀█▀█▒█▀█▒▒█▀█▒▄███▄▒
░█▀█▀█░█▀██░█▀█░█▄█▄█░
░█▀█▀█░█▀████▀█░█▄█▄█░
████████▀█████████████
    ''')
  time.sleep(1)

  # I want to animate a string called exploreMessage that says "After 10 minutes of exploring you find a sand village!"
  ____________________________ #TODO

  time.sleep(1)
  print("\n+----------------------------------------------------------------------------+")
  print("A. Attack the villagers")
  print("B. Protect the villagers")
  print("\n+----------------------------------------------------------------------------+")

  choice = input("\n>>> ")

  #case where user chooses to attack the village
  if choice in answer_A:
    _________ #TODO

  #case where user decides to protect the village
  elif choice in answer_B:
    _________ #TODO

  #case where illegal arg inputted
  _____ #TODO
    print("")
    print('''
║║║░░▄██║║║║░░░▄█░╔╗
╚╬╝░██▄█╬╬╬╬╬╬███░║║
░║░░░▀██║║║║░░░▀█░╠╝
░║░░░░░░░░░░░░░░░░║
      ''')
    print ("Illegal Argument, ;-; you may have typed something in wrong")

#method called if user decides to attack villagewrs
def attackVillage():
  time.sleep(____) #TODO

  ##attack message displayed
  attackMessage= "\nAfter attacking the village blacksmith an iron golem appears and attacks you!\n"
  for char in attackMessage:
      print (char,end='')
      time.sleep(.04)

  time.sleep(1)
  #I want user to die here, what do i call?
  _______ #TODO

def protectVillage():

    ##protect message displayed
    protectMessage= "\nYou decide to stand watch and guard the village over night"
    ___ char __ protectMessage: #TODO
      print (______) #TODO
      time.sleep(.04)

    #encounter with skeletons
    time.sleep(1)
    print("\nA mob of skeletons appear at the west gate! what do you do?")
    time.sleep(1)
    print("\n+----------------------------------------------------------------------------+")
    print("A. Fight the skeletons")
    print("B. flee the village")
    print("\n+----------------------------------------------------------------------------+")

    #choice equals user input
    choice = input("\n>>> ")

    #if user decides to fight
    if _____ in answer_A: #if what?
      fight()

    #if user decides to leave
    elif choice in ________: #what list do we need to access
      time.sleep(1)
      print("\n As you flee the village you are poisoned by a witch and finished by a skeleton arrow")
      dieing()

    #case where there is an illegal arg
    else:
      print("")
      print('''
║║║░░▄██║║║║░░░▄█░╔╗
╚╬╝░██▄█╬╬╬╬╬╬███░║║
░║░░░▀██║║║║░░░▀█░╠╝
░║░░░░░░░░░░░░░░░░║
      ''')
      print ("Illegal Argument, ;-; you may have typed something in wrong")

#fight method called if user decides to fault
def fight():

  time.sleep(1)
  print('''
     |\                     /)
 /\_\\__               (_//
|   `>\-`     _._       //`)
 \ /` \\  _.-`:::`-._  //
  `    \|`    :::    `|/
        |     :::     |
        |.....:::.....|
        |:::::::::::::|
        |     :::     |
        \     :::     /
         \    :::    /
          `-. ::: .-'
           //`:::`\\
          //   '   \\
         |/         \\

    ''')

  #print your own animated win message!
  winMessage= "\nAfter a long battle and many casualities, you slay the endermen and protect the villagers!"
  ________________________ #TODO

  # what method do we need to call to win the game?
  _____ #TODO

#dieing method you will implement
def dieing():

  #for loop iterrating through you HP
  for __ in range(_______:
    time.sleep(0.5)
    #How do we show the HP decrementing through a for loop, (Hint: look up casting in python)
    print(________)
  time.sleep(1)

  print('''
──────▄▀▄─────▄▀▄
─────▄█░░▀▀▀▀▀░░█▄
─▄▄──█░░░░░░░░░░░█──▄▄
█▄▄█─█░░▀░░┬░░▀░░█─█▄▄█
    ''')
  print("\nYou died, press F to pay respects ")

  #respect choice
  ____________ =  input("\n>>> ") #TODO
  if respectChoice in answer_F:
        time.sleep(.5)
        print("\nRespects paid, Rip in pepperonis\n")
        print('''
FFFFFFFFFFFFFFFFFFFFFF
F::::::::::::::::::::F
F::::::::::::::::::::F
FF::::::FFFFFFFFF::::F
  F:::::F       FFFFFF
  F:::::F
  F::::::FFFFFFFFFF
  F:::::::::::::::F
  F:::::::::::::::F
  F::::::FFFFFFFFFF
  F:::::F
  F:::::F
FF:::::::FF
F::::::::FF
F::::::::FF
FFFFFFFFFFF
       ''')

  #if no respects paid D:
  else:
        time.sleep(.5)
        print("\nno respect paid D:")
        time.sleep(1)
        print('''
 ▄██████████████▄▐█▄▄▄▄█▌
██████▌▄▌▄▐▐▌███▌▀▀██▀▀
████▄█▌▄▌▄▐▐▌▀███▄▄█▌
▄▄▄▄▄██████████████▀
       ''')

#when wub is called!
def win():
  print("\n+----------------------------------------------------------------------------+")
  print('''
YOU WON ^-^
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░▄▄▄▄▄▄▄░░░░░░░░░
░░░░░░░░░▄▀▀▀░░░░░░░▀▄░░░░░░░
░░░░░░░▄▀░░░░░░░░░░░░▀▄░░░░░░
░░░░░░▄▀░░░░░░░░░░▄▀▀▄▀▄░░░░░
░░░░▄▀░░░░░░░░░░▄▀░░██▄▀▄░░░░
░░░▄▀░░▄▀▀▀▄░░░░█░░░▀▀░█▀▄░░░
░░░█░░█▄▄░░░█░░░▀▄░░░░░▐░█░░░
░░▐▌░░█▀▀░░▄▀░░░░░▀▄▄▄▄▀░░█░░
░░▐▌░░█░░░▄▀░░░░░░░░░░░░░░█░░
░░▐▌░░░▀▀▀░░░░░░░░░░░░░░░░▐▌░
░░▐▌░░░░░░░░░░░░░░░▄░░░░░░▐▌░
░░▐▌░░░░░░░░░▄░░░░░█░░░░░░▐▌░
░░░█░░░░░░░░░▀█▄░░▄█░░░░░░▐▌░
░░░▐▌░░░░░░░░░░▀▀▀▀░░░░░░░▐▌░
░░░░█░░░░░░░░░░░░░░░░░░░░░█░░
░░░░▐▌▀▄░░░░░░░░░░░░░░░░░▐▌░░
░░░░░█░░▀░░░░░░░░░░░░░░░░▀░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ''')
  print("\n+----------------------------------------------------------------------------+")

  #customize last message of program if user won! try to animate it :D"
  winMessage= ____________________ #TODO

#main method that calls your messages after execution, very useful to comment certain methods out when testing
intro()
setup()
choice()

#Congratulations!!!! although you got the base game to work, feel free to use the skills you learned
#to get creative (no pun intended) and create a story of your own
