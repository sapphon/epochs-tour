# THE EPOCHS TOUR

Braylor Swift's EPOCHS Tour is coming to town, and everybody wants a ticket.  The catch is, seating is limited - and since BrayBray is the world's favorite singer, she won't stay in town for long.

Luckily, you are prepared!  Having found the vendor's API, your job is to write a script that will automatically buy the tickets you and your friends want, as soon as they go on sale.

## Kata Rules

* Suitable for any language
* Suitable for any skill level via iterative expectations
* You may not modify the functionality of the fake "API" except when the requirements direct you to; only write in the area indicated by the comments
* It's more fun if you treat the data that the acceptance tests use as a black box as well
* For each requirement, try to determine O(n) and Θ(n) of your solution

## Repository Structure
It is recommended that you fork this repository.  At the same level as this README are directories per language in which the kata has been implemented.  Each language's directory contains subdirectories named after the requirements that particular friend or group has for their tickets, listed below.

Within each problem's directory, `tickets.json` is the API data, `answers.json` is the expected answer given that API data, and a "blank" (not actually empty) source file outline for that language that will allow you to run code against the problem and time your solution.

## The Requirements

### \#1: Buy Any Ticket
	Use the 'buy' method to purchase any available ticket.

### \#2: Buy Cheapest Available Ticket

### \#3: Buy Two Consecutive Tickets
	Use the 'buy' method to purchase any available two tickets next to each other.

### \#4: Buy Cheapest Two Consecutive Tickets

### \#5: Buy $300 worth of consecutive tickets, and get as many as you can

### \#6: Buy Cheapest Ticket If Under $150 OR Closest-to-Stage Ticket Otherwise
	The orchestra (section 1) is closest to the stage, then the mezzanine (2), then the balcony (3).  Letters towards the beginning of the alphabet denote closer rows within those sections.

### \#7: Buy two tickets as far from the stage as possible, for the in-laws
	The orchestra (section 1) is closest to the stage, then the mezzanine (2), then the balcony (3).  Letters towards the beginning of the alphabet denote closer rows within those sections.

### \#8: Buy Cheapest 3 Consecutive Tickets OR Cheapest Single Orchestra Ticket
	If your two married friends can't sit together and with you, they don't want to come.  Get 3 consecutive seats if possible.  If not, just one for you.

### \#9: Handle Latency
	Modify the 'buy' method to take two seconds and to return a boolean.  Modify the tickets array to be a function.  Simulate tickets disappearing between when you call buy and when it completes!

### \#10: Buy 3 Unscalped Non-Consecutive Tickets

### \#11: Buy Cheapest 4 Tickets in a Square, At Least 3 Unscalped

### \#++: Combine Previous Requirements To Create New Ones!
