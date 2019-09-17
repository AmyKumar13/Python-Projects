Instructions: https://documentcloud.adobe.com/link/track?uri=urn%3Aaaid%3Ascds%3AUS%3A64c41ed3-9de1-42d3-b79d-b8e6df0458d9
class Character:        #class
    '''This class holds the main character for this game.      #style 1 of commenting
    Contains internal functions to add/subtract health as well as add coins.
    It also holds the starting values for the dragon, which you will battle at the final stage.'''
    def __init__(self, name = "Character", hair = "S", eye = "H", accessory = "N"):
        self.name = name
        self.hair = hair
        self.eye = eye
        self.accessory = accessory
        self.coins = 50
        self.health = 100
        self.dragon_health = 100
    def changeHealthUser(self, healthFactor):         #function definition with parameters
        self.health -= healthFactor                   #-+ operator
    def changeCoins(self, coinsFactor):
        self.coins += coinsFactor                     #+= operator
    def changeHealthDragon(self, healthFactor):
        self.dragon_health -= healthFactor
    def buyPotion(self):
        self.health += 30
        self.coins -= 30

def create():
    character = Character()
    while True:            #while loop
        nameInp = input("What is your character's name? ")
        character.name = nameInp.upper()                        #x.upper()
        print("Welcome"+ ' ' + character.name+"!")   #print statement
        break
    while True:
        hairInp = input("Select a hair color for your character: (B)lack, B(R)own, Re(D), (G)ray or Blond(E) ")
        if hairInp.upper() in ["B", "R", "D", "G", "E"]:
            character.hair = hairInp.upper()
            break
        else:
            print("That is not a valid hair color selection. Try again.")
    while True:
        eyeInp = input("Select an eye color for your character: (B)lue, B(R)own, (G)reen, or (H)azel ")
        if eyeInp.upper() in ["B", "R", "G", "H"]:
            character.eye = eyeInp.upper()
            break
        else:
            print("That is not a valid eye color selection. Try again")
    while True:
        accessoryInp = input("Select a weapon for your character: (C)rossbow, (S)word, (A)xe, or (W)hip ")
        if accessoryInp.upper() in ["C", "S", "A", "W"]:
            character.accessory = accessoryInp.upper()
            break
        else:
            print("That is not a valid accessory selection. Try again.")
    return character

#https://medium.com/@george.seif94/a-tour-of-the-top-5-sorting-algorithms-with-python-code-43ea9aa02889     #style 2 of commenting
def bubbleSortReversed(aList):        #sort contents of a list (not built-in sort)
    #taken from code shown in class
    for i in range(0, len(aList)):    #nested loop
        for j in range(i, len(aList)):
            if aList[j] > aList[i]:
                temp = aList[i]       #assigment statement
                aList[i] = aList[j]
                aList[j] = temp

    return aList


def countVowel(str):        #recursive function
    str = str.upper()
    if len(str) == 0:
        return 0
    count = 0
    if str[0:1] in ['A', 'E', 'I', 'O', 'U', 'Y']:
        count = 1
    return count + countVowel(str[1:])

def main():
    import random
    scores = {}   #Dictionary
    sortedValues = []             #list
    while True:
        while True:
            UserInput = input(
                "Welcome to Dragon's Creed. To begin your adventure, please press 1. To quit the game, press 2. ")
            if UserInput not in [1,2, "1", "2"]:
                print("That is not a valid input. Please try again.")
            else:
                break
        if UserInput == 2 or UserInput == "2":              #if statement
            print("View Top Leaders in the file 'leaderboard.txt'!")
            leaders = open("leaderboard.txt", "a")  #file read
            for x in sortedValues:     #for loop
                leaders.write(x+"\n")  #file writing
            break
        elif UserInput == 1 or UserInput == "1":
            if bool(scores) == True:
                print("Current Gameplay Scores: ")
                print(scores)
            print()

            player1 = create()
            print()
            print("In this game you will be scored by the number of coins you end up with. You start with 50 coins. Make your decisions wisely!")
            print("You have " + str(player1.coins) + " coins.")
            print("Your mission is to defeat the dragon and collect the golden egg from his lair.")

            print()
            print(
                "You will start your journey outside SilverHallow Falls, the enchanted forest within King Percival’s kingdom, Esdeal.")
            print(
                "The forest is a few miles away from the Highlands, where Kirdeen Mountain is.")
            print(
                "To reach the treasure you came seeking, you must first prove your worth and travel through the unforgiving forest.")
            print()

        def dragon_attack():
            print('A screeching roar emanates from your left side.')
            print()
            while True:
                dragon_encounter = input(
                    'Type (A) if you would like to keep walking at an idle pace. Type (B) if you would like to sprint frantically. '
                    'Type (C) if you would like to investigate. ')
                if dragon_encounter.upper() not in ["A", "B", "C"]:
                    print("That is not a valid input. Please try again.")
                else:
                    break
            if dragon_encounter.upper() == 'A':
                print(
                    'A dragon has lacerated your back. In the midst of this attack. You must now battle the dragon.')
            if dragon_encounter.upper() == 'B':
                print(
                    'While sprinting a dragon has mauled your leg. You must now battle the dragon.')
            if dragon_encounter.upper() == 'C':
                print()
                print(
                    'You pivot to the left and encounter a menacing dragon in your midst.\n' 
                    'Two gnarled horns sprout from its head. It raises its head from a freshly killed Elk carcas and faces you, uttering a menacing snarl. \n'
                    'You must now battle the dragon.')
            print()

            while True:
                bridgeinput = input('Press (A) to battle the dragon. ')
                if bridgeinput.upper() not in ["A"]:
                    print("That is not a valid input. Please try again.")
                else:
                    break

            print()

            print('During a battle, you and the dragon will have the choice to either attack or shield yourself.')
            print('If you choose to attack and the dragon chooses to attack, both of you have a high likelihood of being injured')
            print('If you shield yourself and the dragon attacks you, you will suffer less damage, and vice versa.')
            print("You may purchase a potion before each round of your battle, but beware, it will cost you." )
            print()
            while True:
                if player1.dragon_health <= 0:
                    print()
                    print("Congrats, you killed the dragon!")
                    print("You enter the dragon's lair and collect his golden egg.")
                    print("Your name will be forever remembered in the Dragon's Creed Leader Board.")
                    print()
                    break
                elif player1.health <=0:
                    print("The dragon cast his final blow. You are now dead. Game over.")
                    break
                print()
                if player1.coins >= 30:       #nested if statement
                    while True:
                        try:
                            potionInput = eval(input('To purchase a potion, press 1 now, or press any other key to continue.'))
                            if potionInput == 1:
                                player1.buyPotion()
                                print("That looked delicious!")
                                print(player1.name + 'health:' + str(player1.health))
                                break
                            else:
                                break
                        except SyntaxError:        #try except block
                            break
                        except NameError:
                            break
                while True:
                    userSelection = input('To melee the dragon with your sword, press (1). To shield yourself press (2). ')
                    if userSelection not in [1,2, "1", "2"]:
                        print("That is not a valid input. Please try again.")
                    else:
                        break
                print()
                userSelection = int(userSelection)
                dragonSelection = random.randint(1, 2)   #random number generator
                # both of you shield
                if userSelection == 2 and dragonSelection == 2:
                    print()
                    print("You have both shielded yourselves. No health points lost.")

                # both of you attack
                elif (userSelection == 1 and dragonSelection == 1):
                    print()
                    print('You have attacked the dragon, and it has attacked you!')
                    print()
                    userOutcome = random.randint(1, 101)
                    dragonOutcome = random.randint(1, 101)
                    if userOutcome <= 70:
                        player1.changeHealthUser(20)         #calling a function with parameters
                        print('The dragon has lacerated your spleen. You lose 20 health points.')
                        print(player1.name + ' ' + 'Health:' + str(player1.health))
                        if player1.health <= 0:
                            print("The dragon cast his final blow. You are now dead. Game over.")
                            break
                    elif userOutcome <= 90 and userOutcome >= 70:
                        player1.changeHealthUser(40)
                        print('The dragon has enveloped you in fire. This is a critical hit. You lose 40 health points.')
                        print(player1.name + ' ' + 'Health:' + str(player1.health))
                        if player1.health <= 0:
                            print("The dragon cast his final blow. You are now dead. Game over.")
                            break
                    elif userOutcome <= 100 and userOutcome > 90:
                        print("Your have dodged the dragon's attack. No health points lost.")
                        print(player1.name + ' ' + 'Health:' + str(player1.health))
                        if player1.health <= 0:
                            print("The dragon cast his final blow. You are now dead. Game over.")
                            break
                    if dragonOutcome <= 80:
                        player1.changeHealthDragon(20)
                        print("You have lacerated the dragon's eye. The dragon has lost 20 health points.")
                        print('DRAGON Health:' + str(player1.dragon_health))
                    elif userOutcome <= 95 and userOutcome >= 80:
                        player1.changeHealthDragon(40)
                        print("You have pierced the dragon's spleen the dragon in fire. This is a critical hit. The dragon lost 40 health points.")
                        print('DRAGON Health:' + str(player1.dragon_health))
                    elif userOutcome <= 100 and userOutcome > 95:
                        print("The dragon has dodged your attack. The dragon lost no health points.")
                        print('DRAGON Health:' + str(player1.dragon_health))
                    # the dragon shields and you attack
                elif (userSelection == 1 and dragonSelection == 2):
                    print()
                    print('You have attacked the dragon, and it has shielded itself!')
                    print()
                    userOutcome = random.randint(1, 101)
                    dragonOutcome = random.randint(1, 101)
                    if dragonOutcome <= 40:
                        player1.changeHealthDragon(10)
                        print("You have lacerated the dragons spleen. The dragon has lost 10 health points.")
                        print('DRAGON Health:' + str(player1.dragon_health))
                    elif userOutcome <= 80 and userOutcome >= 40:
                        player1.changeHealthDragon(20)
                        print("You have cut off the dragon's tail. This is a critical hit. The dragon lost 20 health points.")
                        print('DRAGON Health:' + str(player1.dragon_health))
                    elif userOutcome <= 100 and userOutcome > 80:
                        print("The dragon has shielded your attack. The dragon lost no health points.")
                        print('DRAGON Health:' + str(player1.dragon_health))
                    # you shield and the dragon attacks
                elif (userSelection == 2 and dragonSelection == 1):
                    print()
                    print('The dragon has attacked you, and you have shielded yourself!')
                    print()
                    userOutcome = random.randint(1, 101)
                    dragonOutcome = random.randint(1, 101)
                    if userOutcome <= 40:
                        player1.changeHealthUser(10)
                        print('The dragon has chewed off your ear. You lost 10 health points.')
                        print(player1.name + ' ' + 'Health:' + str(player1.health))
                        if player1.health <= 0:
                            print("The dragon cast his final blow. You are now dead. Game over.")
                            break
                    elif userOutcome <= 80 and userOutcome >= 40:
                        player1.changeHealthUser(20)
                        print('The dragon has annihilated your core. STOP SHIELDING! You have lost 20 health points.')
                        print(player1.name + ' ' + 'Health:' + str(player1.health))
                        if player1.health <= 0:
                            print("The dragon cast his final blow. You are now dead. Game over.")
                            break
                    elif userOutcome <= 100 and userOutcome > 80:
                        print("You have shielded the dragon's attack. You lost no health points.")
                        print(player1.name + ' ' + 'Health:' + str(player1.health))

        def castle_code():
            while True:
                # get user inputs for secret word and secret message
                print()
                print(
                    "Welcome to the Esdeal. King Percival's men are dangerous. Do not trust anyone. Look! An eagle is heading your way!")
                print(
                    "The eagle is the Queen's pet. The Queen is planning an uprising.\nHer message asks you to write a message in code to the Queen with the magic wand.")
                print()
                # https://stackoverflow.com/questions/36432954/python-validation-to-ensure-input-only-contains-characters-a-z
                while True:
                    secret_word = input("First enter your secret word.")
                    if secret_word.isalpha():
                        break
                    else:
                        print("Please enter characters A-Z only.")

                secret_message = input("Next enter your secret message.")
                print("We will encrypt your message using a personal shift determined by the number of vowels in your name.")
                shift = countVowel(player1.name)
                print("Your personal shift is " + str(shift) + ".")
                # transcribe user inputs into string lists upper case
                # transcribe user inputs into string lists upper case
                secret_word_caps = secret_word.upper()
                secret_message_caps = secret_message.upper()

                # transcribe user inputs into ASCII string lists
                secret_word_ASCII_shiftless = [ord(c) for c in secret_word_caps]           #ord()
                secret_message_ASCII_shiftless = [ord(c) for c in secret_message_caps]

                # add shift
                secret_word_ASCII = [i + shift for i in secret_word_ASCII_shiftless]
                secret_message_ASCII = [i + shift for i in secret_message_ASCII_shiftless]

                # remove spaces
                for i in secret_message_ASCII:
                    if i == 32 + shift:
                        secret_message_ASCII.remove(i)

                for i in secret_word_ASCII:
                    if i == 32 + shift:
                        secret_word_ASCII.remove(i)

                # Extend word to size
                multiplier = len(secret_message_ASCII) // len(secret_word_ASCII)
                remainder = len(secret_message_ASCII) % len(secret_word_ASCII)
                secret_word_extended = (multiplier * secret_word_ASCII) + secret_word_ASCII[:remainder]

                # Wrap
                secret_message_wrapped = [((i - 64) % 26) for i in secret_message_ASCII]
                secret_word_extended_wrapped = [((i - 64) % 26) for i in secret_word_extended]

                for y, i in enumerate(secret_message_wrapped):
                    if i == 0:
                        secret_message_wrapped[y] = 26

                for y, i in enumerate(secret_word_extended_wrapped):
                    if i == 0:
                        secret_word_extended_wrapped[y] = 26

                # Shift Secret Message
                secret_message_wrapped_shifted = [secret_message_wrapped[i] + secret_word_extended_wrapped[i] for i in
                                                  range(len(secret_message_wrapped))]

                # Wrap Secret Message Again
                secret_message_shifted_wrapped2 = [(i - shift) % 26 for i in secret_message_wrapped_shifted]

                for y, i in enumerate(secret_message_shifted_wrapped2):
                    if i == 0:
                        secret_message_shifted_wrapped2[y] = 26

                # Ciper Secret Message
                secret_message_ciphered = [chr(i + 64) for i in secret_message_shifted_wrapped2]       #chr()
                print(*secret_message_ciphered, sep='')

                while True:
                    bridgeinput2 = input("Place your message in the beak of the Queen's Eagle by pressing (A).")  #input function
                    if bridgeinput2.upper() not in ["A"]:
                        print("That is not a valid input. Please try again.")
                    else:
                        break

                print()
                break

        def troll():     #basic function
            print()
            while True:
                print("I am Druxan, the chosen guardian of Silver Hallow Falls. This forest hides dangerous secrets.")
                print(
                    "To cross into the Falls, you must first answer three riddles. Walk away now, you live. Answer wrong, you lose a coin.")
                while True:
                    try:
                        print()
                        riddle1 = int(input(
                            "A fool once gave a duck nine coins, a spider 36 coins, and the bee was given twenty-seven coins.\n"
                            "His fool of a brother then gave some money to a white calico cat. How much did he give, human?"))
                        print()
                        if riddle1 == 18:
                            print(
                                "So you think you're smart, huh? A cat has nine lives, not you. Answer this next one, or die.")
                            player1.changeCoins(5)
                            print(player1.name + ' coins' + ':' + str(player1.coins))
                            break
                        else:
                            print()
                            print("Silly human! You have lost 2 coins.")
                            player1.changeCoins(-2)
                            print(player1.name + ' coins' + ':' + str(player1.coins))
                    except:
                        print("You have entered an invalid input. Please try again")
                while True:
                    try:
                        print()
                        riddle2 = input(
                            "A thief tried to steal from the king and cut the king's throat. The king did not have a head though. What has a neck but no head?")
                        # ASK FOR TRY EXCEPT HERE
                        if riddle2.upper() == "A BOTTLE" or riddle2.upper() == "BOTTLE":
                            print()
                            print(
                                "Congrats human, you have been awarded 5 coins.\n"
                                "You might be ready for the Falls yet, human. Answer the last one, carefully. Remember Druxan is not forgiving and neither is the forest.")
                            player1.changeCoins(5)
                            print(player1.name + ' coins' + ':' + str(player1.coins))
                            break
                        else:
                            print()
                            print("Silly human! You have lost 2 coins.")
                            player1.changeCoins(-2)
                            print(player1.name + ' coins' + ':' + str(player1.coins))
                    except:
                        print('You have entered an invalid input. Please try again.')
                print()
                while True:
                    try:
                        riddle3 = input(
                            "The villagers play a game to determine who gets the harvest. The one who throws the magical mushroom ball the furthest, wins.\n"
                            "What can be caught, but not thrown?")
                        if riddle3.upper() == 'A COLD' or riddle3.upper() == 'COLD':
                            print()
                            print("Well done " + str(
                                player1.name) + ". You have answered all three correctly and awarded another 5 coins.\n"
                                                "You may now pass through the forest into Esdeal.")
                            player1.changeCoins(5)
                            print(player1.name + ' coins' + ':' + str(player1.coins))
                            break
                        else:
                            print()
                            print("Silly human! You have lost 2 coins.")
                            player1.changeCoins(-2)
                            print(player1.name + ' coins' + ':' + str(player1.coins))
                    except:
                        print("You have entered an invalid input. Please try again.")
                break

        troll()       #call basic function
        castle_code()
        dragon_attack()
        if player1.health > 0:
            scores[player1.name] = player1.coins
            leaderBoard = []
            for x in scores:                      #walking through list
                leaderBoard.append(str(scores[x]) + " / " + x)    #using built-in list functionality
            sortedValues = bubbleSortReversed(leaderBoard)

main()
