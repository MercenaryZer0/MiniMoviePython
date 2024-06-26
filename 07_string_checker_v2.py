# checks that the user enters a valid response (eg yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):
    while True:
        response = input(question).lower

        for item in valid_responses:
            if response == item[0] or response == item:
                return item
            
        print("Please enter a valid response")

# Main Routine starts here...
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

for case in range(0, 5):
    want_instructions = string_checker("Do you want to read the instructions (y/n)")
    print("You chose", want_instructions)

for case in range(0, 5):
    payment_method = string_checker("", 2, payment_list)
    print("You chose", payment_method)  