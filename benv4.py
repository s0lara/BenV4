ben = 0 

while ben <= 10000000000000000000000000000000000000000000000000:
    ben += 1
    if ben == 1:
        start_ben = input("Start Ben? y or n")
        if start_ben == "n":
            break
    if ben > 1:
        play_again = input("play again? y or n")
        if play_again == "n":
            break
    
    print("Ben?")
    print("Please select operation -\n" 
        "1. talk\n" 
        "2. call\n" 
        "3. potions\n"
        "4. Sosa")
    cmd = (input("Command"))
    if cmd == "1":
        talk = (input("talk to ben"))
        print("Ben: ", talk)
    
    if cmd == "2":
        print("Ring Ring Ring")
        print("Ben?")
        input("Ask ben a question: ")
        import random
        words = ['blehhhhhh','ben','hohoho','No','Yes','slams phone'] 
        word = random.choice(words)
        print(word)
    if cmd == "4":
        with open('penis.txt') as f:
            contents = f.read()
            print(contents)

    if cmd == "3":
        potion_list = print("1. Red, 2. Blue, 3 Green, 4 Yellow") 

        color1 = input("First potion color number here: ")
            
        
        color2 = input("Second potion color number here: ")
        
        if color1 == "1":
            if color2 == "2":
                print("Poof!")
                print("Ben: hohoho")
                print("Congrats! You have synthesized LEAN!!!!!")
            else:
        
        
        
                if color1 == "2":
                    if color2 == "1":
                        print("Poof!")
                        print("Ben: hohoho")
                        print("Congrats! You have synthesized LEAN!!!!!")    
        else:
            
        
    
            if color1 == "3":
                if color2 == "4":
                    print("Poof!")
                    print("Ben: hohoho")
                    print("Congrats! You have synthesized MELATONIN!!!!!")
            else:
                play_again = input("play again? y or n")
                if play_again == "n":
                    break
        
        
                if color1 == "4":
                    if color2 == "3":
                        print("Poof!")
                        print("Ben: hohoho")
                        print("Congrats! You have synthesized MELATONIN!!!!!")



        
                            