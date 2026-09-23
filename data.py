""" def counting():
    sentence = input("Type a sentence ")
    wordcount = sentence.split()
    words = len(wordcount)
    print("There are " + str(words) + " words in your sentence!")
counting() """

def calculator():
    bill = float(input("How much was the bill?"))
    tip = int(input("How much would you like to tip? 0% / 15% / 20% / 25% (no % sign)"))
    tip = tip / 100
    total = bill * (1 + tip)
    print(f"Your total is ${total}")
calculator()

#students = ["Natalie", "Martin", "Ben", "Stefania"]
#students.append("Karas")
#print(students.pop(0), students)
#for student in students:
#    if(student == "Ben"):
#        print("Found Him!")

