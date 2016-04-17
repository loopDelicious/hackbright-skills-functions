# SOLUTIONS!

################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".
def greeting():
    print "Hello World"

#greeting()

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.
def personal_greeting(name):
    print "Hi %s" % name

#personal_greeting("Joyce")

# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.

def multiplier(x, y):
    print x * y

#multiplier(2, 3)

# 4. Write a function that takes a string and an integer and
#    prints the string that many times

def repeater(string, integer):
    print string * integer

#repeater("Joyce", 3)


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If integer is 0 print "Zero".

def higher_than_zero (x):
    if x > 0:
        print "Higher than 0"
    elif x < 0:
        print "Lower than 0"
    else:
        print "Zero"

#higher_than_zero(-1)

# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.

def divisible_by_3(x):
    if x % 3 == 0:
        print True

#divisible_by_3(9)

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.

def space_counter(string):
    return string.count(" ")

#space_counter("Hello I'd like you to open the window please.")

# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def tip_calcky(meal_price, tip_percent = 0.15):
    total = meal_price + (meal_price * tip_percent)
    print "${:.2f}".format(total) 

#tip_calcky(14, .20)

# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#	 should be returned in a list.
#
# 	Then, write code that shows the calling of this function
# 	on a number and unpack what is returned into two
# 	variables --- sign and parity (whether it's positive
# 	or negative). Print sign and parity.

def sign_and_parity(x):
    
    results = []
    
    if x >= 0:
        results.append("Positive")
    else:
        results.append("Negative")

    if x % 2 == 0:
        results.append("Even")
    else:
        results.append("Odd")

    return results

results = sign_and_parity(9)

sign = results[0]
parity = results[1]

#print sign + " " + parity

################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviaton, and the
#    default tax amount as parameters.
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item including tax.

def tax_calcky(price, state, tax = 0.05):

    if state == "CA":
        tax = 0.07

    total = price + (price * tax)

    print total

#tax_calcky(8, "CA")


# 2. Turn the block of code from the directions into a function.
#	 Take a name and a job title as parameters, making it so the
# 	 job title defaults to "Engineer" if a job title is not passed in.
#	 Return the person's title and name.

def title_giver(name, title = "Engineer"):
    return title + " " + name

#title_giver("Joyce")


# 3. Given a receiver's name, receiver's job title, and sender's name, print the following letter:      
#       Dear JOB_TITLE RECEIVER_NAME, I think you are amazing! Sincerely,
#       SENDER_NAME. 
#    Use the function from #2 to construct the full title for the letter's greeting.

receiver = title_giver("Joyce")

#print "Dear {}, I think you are amazing!  Sincerely, {}.".format(receiver, "Donna")


# 4. Turn the block of code from the directions into a function. This
#    function will take a number and append it to *numbers*. It doesn't
#    need to return anything.

numbers = [1,2]

def appender(num):
    numbers.append(num)

#appender(3)
