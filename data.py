def counting():
    sentence = input("Type a sentence ")
    wordcount = sentence.split()
    characters = len(sentence)
    print("There are " + str(characters) + " letters in your sentence!")
counting()