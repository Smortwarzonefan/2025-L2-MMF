# Functions Go Here
def string_check(question, valid_ans_list=['yes', 'no'], num_letters = 1):
    """Checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_ans_list:

            # Check if response is in the entire word
            if response == item:
                return item

            elif response == item[0]:
                return item

        print(f"Please choose an option from the following: {valid_ans_list}")
# Main Routine Goes Here
payment_list = ['cash', 'card']

while True:
    want_instructions = string_check("Do you want to see the instructions? ")
    print(f"You chose {want_instructions}")
    print()


# payment_method = string_check(f"Choose a payment method: ", payment_list, num_letters=2)
# print(f"you chose {payment_method}")
