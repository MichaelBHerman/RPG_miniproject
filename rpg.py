#!/usr/bin/python3
import random
import requests
import sys

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game


========
You are a Snorlax. You awake from your slumber to find yourself in a strange, creepy old house.
You must find a way out! 

Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
#   random_combat_encounter(e1, p1)
  #print the current inventory
  
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")


#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                 
                }, 

            'Kitchen' : {
                  'north' : 'Hall',
                   'item'  : 'key',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'master ball',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

## class for player(Snorlax) and enemy(ghost pokemon)
class Player:
    def __init__(self):
        self.name = "Snorlax"
        self.hp = 100
    def claw(self, enemy):
        print("------------------------------")
        print("\nSnorlax used Claw!") 
        random_damage = random.randint(10, 100)
        enemy.hp - random_damage
        print("\nThe " + enemy.name + " lost " + str(enemy.hp))
        

    def bite(self, enemy):
        print("------------------------------")
        print("\nSnorlax used Bite!")
        print("\n" + enemy.name + " lost 35 hp. ")
        enemy.hp -= 35

class Enemy:
    def __init__(self, pokemon_encounter):
        self.name = pokemon_encounter
        self.hp = 40  #maybe set a random health value based on min max range

    def dark_pulse(self, player, name):
        print("------------------------------")
        print("\n" + name + " used Dark Pulse!")
        print("\n" + player.name + " lost 20 hp. ")
        player.hp -= 20

ghost_pokemon = ["Ghastly", "Haunter", "Spiritomb", "Mimikyu", "Polteageist"]

pokemon_encounter = random.choice(ghost_pokemon)

p1 = Player()
e1 = Enemy(pokemon_encounter)

def random_combat_encounter(enemy, player):
    # pokemon_encounter = random.choice(ghost_pokemon)
    
    if pokemon_encounter != "":
        enemy.hp = 40
        combat = True
        print("A wild " + pokemon_encounter + " appreared!\n")

        while combat == True:
        
            move = int(input("Select a move. [1] Bite, [2] Claw\n>>>"))
            if move == 1:
                player.bite(enemy)
                print(enemy.name + "'s HP: " +str(enemy.hp))
            else:
                player.claw(enemy) 
                print(enemy.name + "'s HP: " +str(enemy.hp))
            if enemy.hp <= 0:
                print("\nThe wild " + enemy.name + " fainted!\n") 
                # ghost_pokemon.remove(pokemon_encounter)
                # print(ghost_pokemon)
                combat = False  
            else: 
                enemy.dark_pulse(player, pokemon_encounter) 
                print(player.name + "'s HP: " +str(player.hp))
            ##checkwin()
                if player.hp <= 0:
                    print("Snorlax fainted!  Game over.") 
                    sys.exit() 
                continue
            ##continue should loop back to the begnining of the combat while loop
                
    else: 
        print("After looking around, the coast is clear.")

showInstructions()

#loop forever
while True:

  showStatus()
  

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'master ball' in inventory:
    print("------------------------------")
    print("You are in the Garden\n")
    print('\nA wild Necrozma appeared!')
    choice = int(input("Use master ball? [1] yes [2] no\n>>>"))
    if choice == 1:
        print("\nYou captured Necrozma with the master ball! You used the key and exited through the garden gate.  You WIN!")
        sys.exit()
  elif currentRoom == 'Garden' and 'key' not in inventory and 'master ball' not in inventory:
    print("You are in the Garden.\n")
    print("\nA wild Necrozma Appeared!")
    print("\nNecrozma used Prismatic Laser") 
    print("\nSnorlax fainted.  You LOSE!")   
    sys.exit()
    
   

  if currentRoom == "Kitchen":
      print("Kanye West appears and offers you some wisdom: \n") 
      response = requests.get("https://api.kanye.rest")
      wisdom = response.json()
      print("Kanye says: " + wisdom["quote"])
      print("\nWTH......okay?  Moving on...")

  if currentRoom == "Pantry":
      pokemon_encounter = ""
      pokemon_encounter = random.choice(ghost_pokemon)
      e1 = Enemy(pokemon_encounter)
      random_combat_encounter(e1, p1)  

  if currentRoom == "Hall":
      random_combat_encounter(e1, p1)    
 
  if currentRoom == "Dining room":
      random_combat_encounter(e1, p1)      

#   if currentRoom == "Music Studio":
#       print("Kanye West appears and offers you some wisdom: \n") 
#       response = requests.get("https://api.kanye.rest")
#       wisdom = response.json()
#       print("Kanye says: " + wisdom["quote"])
#       print("\nWTH......okay?  Moving on...")
     

