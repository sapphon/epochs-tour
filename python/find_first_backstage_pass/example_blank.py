import json
import time

tickets_file = open("tickets.json");
tickets = json.loads(tickets_file.read());
answers_file = open("answers.json");
answers = json.loads(answers_file.read());
bought = [];

def buy(ticket):
	print("Buying ticket: " + str(ticket))
	bought.append(ticket)

start_time = time.time()
'''
You need to buy EPOCHS TOUR tickets before they sell out.  

You have decided to automate attempting to buy some a few times per second, so as not to miss out.

`tickets` is an array of objects representing the available tickets.  Each ticket has:
	* `price`, a price in dollars, 
	* `seat`, a seat designation consisting of a letter and number (such as "S7"),
	* `section`, a section number (1 for orchestra, 2 for mezzanine, 3 for balcony)
	* `origin`, an originality ("ORIGINAL" or "SCALPED"),
	* `date`, an event date and time
	* `includes_backstage_pass`, whether or not the ticket includes a backstage pass
		* False or True

If a ticket looks good you can add it to your cart with `buy(reference_to_ticket)`

Based on the tickets available and the requirements, write a program that correctly buys the tickets you want as fast as possible.  Good luck!

Do not write above this line
'''

'''
Do not write below this line
'''
print("Time: " + str(time.time() - start_time))
print("Success!" if answers == bought else "Not quite...")