import art


word=art.text2art("Welcome to Jabari's Game")
print (word)


name = input("What is your name?")
print ("Hello!",name)
inp = input("Enter y if you want to play this Riddle Game!")
if "y" in inp.lower():
    print ("Alright!", name)
    print ()
    summary = input ("Jabari is very afraid to go onto the diving board. If you can answer these riddles, he will be able to gain confidence. The more energy you get, the cooler dive he can do at the end! (After 7 tries, you will have to restart your code) Enter anything once you have finished reading")
    print ()
    first = input("What belongs to you but your friends use it more?")
    count = 0
    correct = False
    reset = False
    while correct == False and reset == False :
        if ("name" in first.lower()and count <= 5):
            print("Correct!", name)
            print ("Jabari just gained 1+ confidence and 7+ energy!")
            correct = True
        elif (count <= 5):
            print("try again!")
            first = input("Come on you got this!")
            count += 1
        else: 
          if count < 4:
            first = input("Hint: People call you by your _ _ _ _?:")
            count +=1
          else: 
            print("Sorry", name)
            print ("Ran out of tries, you can try again if you restart the code!")
            print()
            gameover=art.text2art("GAME OVER", name)
            print (gameover)
            validInput = True
            count += 1
             
    word2=art.text2art("You passed the first level!")
    print (word2)

    word3=art.text2art(name)
    print (word3)


    print ()
    second = input("A farmer has 17 sheep all but 8 escape. How many are left?")
    count = 0
    correct = False
    reset = False
    while correct == False and reset == False :
        if ("8" in second.lower()and count <= 5):
            print()
            print ("Correct! Jabari just gained 2+ confidence and 9+ energy!")
            correct = True
        elif (count <= 5):
            print("try again!")
            second = input("Come on you got this!")
            count += 1
        else: 
          if count < 4:
            second = input("Hint: watch the wording on this riddle!:")
            count +=1
          else: 
            print("Sorry", name)
            print ("Ran out of tries, you can try again if you restart the code!")
            print()
            gameover=art.text2art("GAME OVER", name)
            print (gameover)
            validInput = True
            count += 1
          
          
          
    word4=art.text2art("You passed the second level!")
    print (word4)

    print () 
    print("   (-:'  `; `-._")
    print("  (_,           )")
    print(" ,'o(            )> ")
    print("(__,-'            )")
    print("   (             )")
    print("    |`-'._.--._.-'")
    print("        |  |    ")
            


    print ()
    third = input("I am an odd number. I have 3 tens. My ones digit is the same as my tens digit, What am I?")
    count = 0
    correct = False
    reset = False
    while correct == False and reset == False :
        if ("33" in third.lower()and count <= 5):
            print()
            print ("Correct! Jabari just gained 2+ confidence and 9+ energy!")
            correct = True
        elif (count <= 5):
            print("try again!")
            third = input("Come on you got this!")
            count += 1
        else: 
           if count < 4:
            third = input("Hint: the ones digit is 3:")
            count +=1
           else: 
            print("Sorry", name)
        print ("Ran out of tries, you can try again if you restart the code!")
        print()
        gameover=art.text2art("GAME OVER", name)
        print (gameover)
        validInput = True
        count += 1

    word5=art.text2art("You passed the third level!")
    print (word5)

    print ()
    print("     3333    3333")
    print("    33  33  33  33")
    print("       333     333")
    print("    33  33  33  33")
    print("     3333    3333 ")

    print ()   
    last = input("Great Job! It is time to see if Jabari can jump off the diving board! How much energy did you get?")
    correct = False
    while correct == False:
        if ("27" in last.lower()):
            print()
            print ("Correct! Jabari has enough confidence to jump off the diving board!")
            correct = True
        elif (count <= 5):
            print("try again!")
            last = input("Come on you got this!")
            count += 1
        else:
            if count < 4:
             last = input("Hint: 7+9+11:")
            count +=1
            

        
    word6=art.text2art("CONGRATS ON FINISHING THE GAME!!!")
    print (word6)
    
    
    print ()
    print("     .-''-,   ")
    print("    ;--.   \    ")
    print("  _/oo==\===|")
    print(" (_ ___, \  | ")
    print("   \\_/  / /  ")
    print("    `--'\\`   ")
    print("       /U/`--.  ")
    print("      ///,____)   ")
    print("     /// //  /  ")
    print("    ''  // <`   ")
    print("        \`\ \    ")
    print("       _/_/__\_   ")
    print("      \        |   ")
    print("    =====   4  '--.   ")
    print("        \         |    ")
    print("~^~^~^~^~^~[_________|   ")
    print("~^~^~^~^~^///////////    ")
    print("~^~^~^~^~^~^//////////) ")
    
    
else:   
    print ("Rerun the code to play again")


































