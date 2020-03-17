#This code is meant to be submitted to Python Learn From Home program by TinkerHub
class Tech:
	
    info = {}

#The key of the dictionary is the name of the participant.
#And the value is a list comprising of [stack, designation, available time]

    # Adds the tech stack of the participant
    def addStacks(self,name):
        stack=input("\nThe available Stacks are : Python, GO, Web, UI/UX, Flutter \nEnter a stack you are expert at/interested in[Case sensitive] : ")
        self.info[name] = [None, None, None]
        if name in self.info:
            self.info[name][0] = stack
        return

    # Sets a participant as a mentor or a learner
    # 1 denotes Mentor and 2 denotes Learner      
    def setMentorOrLearner(self,name):
        desig = int(input("\nAre you a \n1.Mentor\n2.Learner\n\nEnter your choice : "))        
        if name in self.info:
            self.info[name][1] = desig
        return
        
    # Sets the available time for a mentor
    def setAvailableTime(self,name):
        if self.info[name][1] == 1 :
            available_time=int(input("\nEnter available time(in minutes) : ")) 
            if name in self.info:
                self.info[name][2] = available_time
        return

    #Gives the mentors satisfying the given specifications    
    def getMentor(self,stack,time):
        flag = 0
        print("\nThe available mentors are : ")
        for mentor in self.info:
            if self.info[mentor][0] == stack and self.info[mentor][2] >= time:
                print("{} ".format(mentor))
                flag = 1
        if flag == 0:
            print("None")
        return


obj = Tech()
go = True
while go:

	# A menu-driven program
	print("\nWELCOME Tech learner/mentor")
	print("\nMENU")
	print("\n[1].Enter the details of a participant")
	print("[2].Check the availablity of mentors")
	print("[3].EXIT")
	choice = int(input("\nEnter your choice : "))
	if(choice == 1):
		
		name = input("\nEnter your name : ")
		obj.addStacks(name)
		obj.setMentorOrLearner(name)
		obj.setAvailableTime(name)
		
	elif(choice == 2):
		stack=input("\nThe available Stacks are : Python, GO, Web, UI/UX, Flutter,\nEnter a stack you are interested in learning [Case Sensitive]: ")
		time=int(input("Enter the required time you need mentoring for : "))
		obj.getMentor(stack,time)

	elif(choice == 3):
		print("\nExiting \nThank You")
		break
	else:
		print("INVALID CHOICE!!!")
		
	flag = input("\nDo you want to continue (Y/N)? ")
	if(flag == 'n' or flag == 'N'):
		print("\nExiting \nThank You")
		go = False
