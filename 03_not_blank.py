#Function goes here...

#Checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        #If the response is blank, outputs error
        if response == "":
            print("Sorry, this cannot be blank. Please try again")

        else:
            return response

#Main routine goes here...
while True:
    name = not_blank("Enter your name or q to quit ")
    if name == "q":
        break

print("We are done.")