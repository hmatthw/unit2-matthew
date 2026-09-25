""" def counting():
    sentence = input("Type a sentence ")
    wordcount = sentence.split()
    words = len(wordcount)
    print("There are " + str(words) + " words in your sentence!")
counting() """

""" def calculator():
    bill = float(input("How much was the bill?"))
    tip = int(input("How much would you like to tip? 0% / 15% / 20% / 25% (no % sign)"))
    tip = tip / 100
    total = bill * (1 + tip)
    print(f"Your total is ${total}")
calculator() """

#students = ["Natalie", "Martin", "Ben", "Stefania"]
#students.append("Karas")
#print(students.pop(0), students)
#for student in students:
#    if(student == "Ben"):
#        print("Found Him!")

""" def oddoreven():
    number = int(input("Enter A Number"))
    if number % 2 == 0:
        print(f'The number {number} is even')
    else:
        print(f'The number {number} is odd')
oddoreven() """

""" def billcalculator():
    bill = int(input("How much was the bill?"))
    service = str(input("How was the service? bad / okay / good / great"))
    if service == "bad":
        print(f"Your total is {bill:.2f}")
    elif service == "okay":
        bill = (bill * 1.15)
        print(f'Your total is {bill:.2f}')
    elif service == "good":
        bill = (bill * 1.2)
        print(f'Your total is {bill:.2f}')
    elif service == "great":
        bill = (bill * 1.25)
        print(f'Your total is {bill:.2f}')
billcalculator() """

""" def factor():
    factors = []
    n = int(input("Enter a number"))
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    print(factors)
factor() """

#fix el problemo tomorrow
n1 = int(input("Enter a number"))
n2 = int(input("Enter another number"))
def commonfactors(x, y):
    factors = []
    for i in range(1, x+1):
        if x % i and y % i == 0:
            factors.append(i)
    print(factors[-1])
commonfactors(n1, n2)
