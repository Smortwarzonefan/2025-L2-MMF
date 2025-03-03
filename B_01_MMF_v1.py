# Functions go here

def make_statement(statement, decoration, lines=1):
    """Creates headings (3 lines), subheadings (2 lines) and
    emphasised text / mini-headings (1 line). Only use emoji for
    single line statements"""

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    else:
        print(top_bottom)
        print(middle)
        print(top_bottom)

def string_check(question, valid_ans_list=['yes', 'no']):
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

def instructions():
    make_statement("Instructions", "ℹ️", 1)
    print('''
    
For each ticket holder enter...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the
ticket cost (and the profit).

Once you have either sold all of the tickets or entered the
exit code ('xxx'), the program will display the ticket
sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the
draw (their ticket is free).

    ''')

def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response !="":
            return response

        print("Sorry, this can't be blank. Please try again.\n")

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

#Main routine goes here

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# Initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to view the instructions? ", ['yes', 'no'])

if want_instructions == "yes":
    instructions()

print()
while tickets_sold != MAX_TICKETS:
    # Ask user for their name (and check it's not blank)
    name = not_blank("Name: ")

    # if name is exit code, break out of loop
    if name == "xxx":
        break

    # Ask the user for their age (and check it's between 12 and 120
    age = num_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"Sorry, {name} is too young for this movie.")
        continue
    elif age > 120:
        print(f"??, that looks like a typo (too old)")
        continue
    else:
        pass

    # Asks the user for payment method (cash / credit)
    pay_method = string_check("Payment method: ", payment_ans)
    print(f"{name} has bought a ticket ({pay_method})")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets")