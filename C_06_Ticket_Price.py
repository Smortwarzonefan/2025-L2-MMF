# Functions go here

def num_check(question):
    """Checks users enter an integer / float that is more than zero (or the optimal exit code)"""

    error = f"Oops! - please enter a whole number greater than 0."

    while True:

        try:
            # Changes response to an integer and check that it's more than zero
            response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response !="":
            return response

        print("Sorry, this can't be blank. Please try again.\n")

def string_check(question, valid_ans_list):
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

# Main routine goes here

# Initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# Ticket Price List
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# Loop for testing purposes
while True:
    print()

    # Ask user for their name (and check it's not blank)
    name = not_blank("Name: ")

    # Ask the user for their age (and check it's between 12 and 120
    age = num_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young.")
        continue

    # Child ticket price ($7.50)
    elif 12 <= age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket ($10.50)
    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

    # Senior Ticket ($6.50)
    elif 65 <= age < 120:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # Asks the user for payment method (cash / credit)
    pay_method = string_check("Payment method: ", payment_ans)

    if pay_method == "cash":
        surcharge = 0

    # If paying with credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # Calculate total payable...
    total_to_pay = ticket_price + surcharge

    print(f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f"The total payable is ${total_to_pay:.2f}\n")