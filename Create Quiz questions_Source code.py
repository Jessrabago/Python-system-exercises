#assessment 1
import random

def questions(q):
    print("Selected number of questions: ", q)
    CountCorrects=0
    Answer=""
    Position=0

    #List of total number of questions
    List_position=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
    
    
    #Pick random number of the questions to ask
    PickedNumbers=random.sample(List_position,q)
    

    #Questions
    #List with answers:
    AnswerQuestion=["RUSSIA","CHINA","AFRICA","MOUNT EVEREST","THE MOUNT EVEREST","EVEREST",
                    "VENICE","FRANCE","EGYPT","VICTORIA FALLS","VICTORIA",
                    "ANTARTICA","PENINSULA","THE PACIFIC OCEAN","PACIFIC OCEAN","PACIFIC",
                    "THE SOUTH POLE", "SOUTH POLE","SOUTH","11","ELEVEN", "ASIA", "MOUNT LOGAN",
                    "THE MOUNT LOGAN","LOGAN"]

    for i in PickedNumbers:
        #1 question
        if i==1:
            print("What is the largest country in the world?")
            #Answer:RUSSIA
            Answer=input("").upper()
            if (AnswerQuestion[0]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")

        
        #2 question
        elif i==2:
            print("What country has the largest population in the world?")
            #Answer:CHINA
            Answer=input("").upper()
            if (AnswerQuestion[1]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #3 question
        elif i==3:        
            print("What is the hottest continent in the world?")
            #Answer:AFRICA
            Answer=input("").upper()
            if (AnswerQuestion[2]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #4 question
        elif i==4:        
            print("What is the tallest mountain in the world?")
            #Answer:MOUNT EVEREST or THE MOUNT EVEREST or EVEREST
            Answer=input("").upper()
            if (AnswerQuestion[3]==Answer) or (AnswerQuestion[4]==Answer) or (AnswerQuestion[5]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #5 question
        elif i==5:        
            print("Which Italian city is famous for its canals?")
            #Answer:VENICE
            Answer=input("").upper()
            if (AnswerQuestion[6]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #6 question
        elif i==6:        
            print("In what country would you find the Eiffel Tower?")
            #Answer:FRANCE
            Answer=input("").upper()
            if (AnswerQuestion[7]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #7 question
        elif i==7:        
            print("In what country would you find the Great Pyramids of Giza?")
            #Answer:EGYPT
            Answer=input("").upper()
            if (AnswerQuestion[8]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #8 question
        elif i==8:        
            print("Which is the largest waterfall in the worl?")
            #Answer:VICTORIA FALLS or VICTORIA
            Answer=input("").upper()
            if (AnswerQuestion[9]==Answer) or (AnswerQuestion[10]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #9 question
        elif i==9:        
            print("Which is the coldest place on Earth?")
            #Answer:ANTARTICA
            Answer=input("").upper()
            if (AnswerQuestion[11]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #10 question
        elif i==10:        
            print("What do you call land with water on 3 sides?")
            #Answer:PENINSULA
            Answer=input("").upper()
            if (AnswerQuestion[12]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #11 question
        elif i==11:        
            print("What is the name of the biggest ocean on Earth?")
            #Answer:THE PACIFIC OCEAN or PACIFIC OCEAN or PACIFIC
            Answer=input("").upper()
            if (AnswerQuestion[13]==Answer) or (AnswerQuestion[14]==Answer) or (AnswerQuestion[15]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #12 question
        elif i==12:        
            print("Which is colder: The North Pole or the South Pole?")
            #Answer:THE SOUTH POLE or SOUTH POLE or SOUTH
            Answer=input("").upper()
            if (AnswerQuestion[16]==Answer) or (AnswerQuestion[17]==Answer) or (AnswerQuestion[18]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #13 question
        elif i==13:        
            print("How many time zones does Russia have?")
            #Answer:11 or ELEVEN
            Answer=input("").upper()
            if (AnswerQuestion[19]==Answer) or (AnswerQuestion[20]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #14 question
        elif i==14:        
            print("What is the largest continent?")
            #Answer:ASIA
            Answer=input("").upper()
            if (AnswerQuestion[21]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")


        #15 question
        elif i==15:        
            print("What is the tallest mountain in Canada?")
            #Answer:MOUNT LOGAN or THE MOUNT LOGAN or LOGAN
            Answer=input("").upper()
            if (AnswerQuestion[22]==Answer) or (AnswerQuestion[23]==Answer) or (AnswerQuestion[24]==Answer):
                print("correct")
                CountCorrects=CountCorrects+1
                Answer=""
            else:
                print("Incorrect")

        
    #Return data
    return CountCorrects


def user_name(r):
    List_Users=[]
    List_Users.append(r)
    return List_Users

def number_questions(s):
        Percentage_score=0
        #Total of question decided by the user
        Total=s
        #Number of correct answers
        NumCorrect=questions(s)
        Percentage_score= NumCorrect/Total * 100
        print("Total of correct answers", NumCorrect)
        print("Percentage score of ", Total, "questions: ", Percentage_score)
        return Percentage_score
    
def Restart_question(t):
        Repeate_question=0
        if t=="YES" or t=="NO" or t=="QUIT":
          Repeate_question=1
          Restart=t
        while (t!="NO" or t!="QUIT" or t!="YES") and Repeate_question==0:
            if t!="NO" or t!="QUIT" or t!="YES":
                print("I am sorry, I did not recognize the command, try again")
                 
            Restart=input("Does anybody else wants to take the quiz? ").upper()
            print()
            if Restart=="NO" or Restart=="QUIT" or Restart=="YES":
                break
            
        Ready=Restart
        return Ready


        
def main():
    User=[]
    Dict_users={}
    Start=""
    
    #Start the test
    while Start!="NO" or Start=="QUIT":
        num_quest_ok=0
        #Ask for name of the user
        x=input("What is your name? ").upper()
        if x=="" or x==" " and Start!="QUIT":
            continue
        if x=="QUIT":
            break
        #Save the names in a List
        User=user_name(x)
        print(User)
        
        #Number of questions to answer given by the user
        y=input("How many questions you want to asnwer between 1 and 15? ")
        if y.isnumeric():
            int_y=int(y)
            if int_y>0 and int_y<16:
                Score_per_User=number_questions(int_y)
            else:
                print("Number not valid, start again")
                print()
                continue
                
        else:
            print("Number not valid, start again")
            print()
            continue

        #Save users and scores
        Dict_users[x]=Score_per_User
            
###
        #Ask if someone else want to try
        z=input("Does anybody else wants to take the quiz? ").upper()
        print()
        Start=Restart_question(z)
        

##    
    if  x=="QUIT" and (len(Dict_users)==0):
        print("NO USERS")
    else:
        #Print the best score
        print("The user(s) with the best score(s) is/are:")
        Best_user=max(Dict_users.values())
        if Best_user!=0:
            for Best in Dict_users.keys():
                if (Best_user == Dict_users[Best]):
                        print("{0} score = {1}".format(Best, Dict_users[Best]),"%")
        else:
            print("Best score is 0")
        print()
        
        #Print all users and scores
        print("All scores are:")
        for UserQuiz in Dict_users.keys():
            print("{0} score = {1}".format(UserQuiz, Dict_users[UserQuiz]),"%")
        print()

        #The avarage Score of all users
        Value_score=Dict_users.values()
        Avarage_total=(sum(Value_score))/(len(Dict_users))
        print("The avarage Score of all users: ",Avarage_total, "%")
        print()

    #Close the program
        print("QUIZ DONE!")
        Exit=input("Press ENTER to exit")

    
    
main()
