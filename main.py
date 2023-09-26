# write a function that gives the user options. if the user chooses to exit, then exit
def option(user):
  # boolean to control loop
  exit = False
  
  # user choice input
  userInput = 0;

  # loop to provide menu to user; for now, this will print what the user enters (if it's a valid option)
  while (exit==False):
    print("Please choose from these options:\n1.) Make a purchase\n2.) Speak with a representative\n3.) Apply for a position with Company X\n4.) Exit")
    userInput = input("How would you like to continue this conversation? >>> ")
    if (userInput=="1"):
      exit=True
      print("Option 1")
    elif (userInput=="2"):
      print("Option 2")
      exit=True
    elif (userInput=="3"):
      print("Option 3")
      exit=True
    elif (userInput=="4"):
      print("Goodbye, " + user + "!")
      exit=True
    else:
      continue

# welcome the user
print("Welcome! I am Company X's chatbot, at your service.")

# instantiate variables to store the user's name and age
userName = ""
userAge=10;

# prompt the user for their name and age. update variables with their input.
userName = input("What's your name? >>> ")
userAge = input("What's your age? >>> ")

#an appropriate response 
print("A pleasure to meet you, " + userName + "! How can I help you today?\n")

# call the function to prompt the user on how to continue their conversation with the chatbot
option(userName)