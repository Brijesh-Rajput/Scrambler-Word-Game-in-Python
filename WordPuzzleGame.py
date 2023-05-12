#Game:- Word Puzzle Game
#Scrambled Word means:- to put things such as words or letters in the wrong order so that they do not make sense

print("Welcome To 'Word Puzzle Game'")
print("In this Game, you have to Unscramble the words which was given to you.")
print("You can play this game as many times you want to play. For that You have to mention the Total Number of rounds You will Play this game.")
print("In Each Round there will be 5 Words. Which you have to unscramble it.")
print("If you Unscramble that given scramble word correctly then In your score +1 will be added, Otherwise score will decrease by 1 (score=score-1)")

choice=input("Are You ready to Play this Game[Y/N] :- ")
if choice.upper()=="Y":
    import random as rd #To suffle the List of Scrambled Word

    wordList={"RAEHTF":"FATHER","KABRE":("BRAKE","BREAK","BAKER"),"CYROTNU":"COUNTRY","RENEG":"GREEN","OAERELANP":"AEROPLANE","SILTNE":("LISTEN","SILENT"),
              "ROPMINGGRA":"PROGRAMMING","EECFRPT":"PERFECT","AEECHTR":["TEACHER","CHEATER","RECHEAT","RETEACH","HECTARE"],"AEICCLPS":"SPECIAL",
              "AOESMEW ":"AWESOME","AOULPPR ":"POPULAR"}
    scramble_word_List=list(wordList.keys())

    round=int(input("How many rounds you want to play a Word Puzzle Game ? \nAnswer:- "))

    for e in range(0,round): #Loop for every round to play the game. ======> Instead of this we can use while loop for endless game in which we will ask the user that whether he wants to play a game again or not. if not then we will break the while loop.
        print("Round %d of game start"%(e+1))

        rd.shuffle(scramble_word_List) #To shuffle the scramble_word_List in each round
        #set1 = set(scramble_word)  # here set is used to show the user word in random sequence ====> But Every time set stores the same value once it is created. Only at first time set values are random compare to list

        count=0  #In each round, there should be only 5 word to solve it.
        score=0 #To store the score of the player of each round

        #code for each round game starts from below line
        for word in scramble_word_List: #Loop for fetching each word from the set of scramble word
            count+=1
            if count==6:
                break

            print("Arrange the letters to form a valid word:- ",word)
            answer=input().upper() #Entered word will converted into uppercase letter

            if type(wordList[word])==tuple: #Whether Unscrumble word has more than one solution or not ? --> to check this
                for str in wordList[word]: #When Unscramble word have more than one solution --> for that we have use this for loop
                    if answer==str:
                        print("Correct")
                        score+=1
                        break
                else:
                    print("Wrong")
                    score-=1
            elif answer==wordList[word]:
                print("Correct")
                score+=1
            else:
                print("Wrong")
                score-=1

        print("Round %d is completed and your score is %d"%(e+1,score))
        print()
    # else:
    #     print("Game Over!!!")
elif choice.upper()=="N":
    pass
    # print("Game Over!!!")
else:
    print("Invalid Choice")
print("Game Over!!!")
input("Press Enter Key to Kill the program") #Note:- Enter Key Not any Key

"""Below commented is for my understanding ==
#At this point think about case-insensitive
#Note:- in every round there will be only 5 words
#How to show random sequence of word
"""