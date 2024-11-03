import json
import time

tickets_file = open("tickets.json")
tickets = json.loads(tickets_file.read())
answers_file = open("answers.json")
answers = json.loads(answers_file.read())
bought = []
sold = []

def sell(ticket):
	if ticket not in sold:
		print("Selling ticket: " + str(ticket))
		sold.append(ticket)
		return True
	return False

def buy(ticket):
	if ticket not in bought:
		print("Buying ticket: " + str(ticket))
		bought.append(ticket)
		return True
	return False

def check_availability():
	time.sleep(3)
	return [ticket for ticket in tickets if ticket not in bought]


start_time = time.time()
'''
You need to buy EPOCHS TOUR tickets before they sell out.  

You have decided to automate attempting to buy some, so as not to miss out.

`check_availability` is a parameterless method that returns an array of available tickets.

Each ticket has:
	* `price`, a price in dollars, 
	* `seat`, a seat designation consisting of a letter and number (such as "S7"),
	* `section`, a section number (1 for orchestra, 2 for mezzanine, 3 for balcony)
	* `origin`, an originality ("ORIGINAL" or "SCALPED"),
	* `date`, an event date and time
	* `includes_backstage_pass`, whether or not the ticket includes a backstage pass
		* False or True

If a ticket looks good you can buy it with `buy(reference_to_ticket)`.  This method returns false if the purchase was unsuccessful.

You can also sell tickets similarly, with `sell(reference_to_ticket)`.  This method returns false if the sale was unsuccessful.

Based on the tickets available and the requirements, write a program that correctly performs the transactions you want as fast as possible.  Good luck!

Do not write above this line
'''




'''
Do not write below this line
'''
print("Time: " + str(time.time() - start_time))
print("Success!" if answers['toBuy'] == bought and answers['toSell'] == sold else "Not quite...")