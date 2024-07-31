print("Madlibs Ver 1.0")
Noun1 = input("Choose A Noun: ")
while Noun1 == (""):
    print("Your response can't be empty!")
    Noun1 = input("Please Enter A Noun: ")
PluralNoun1 = input("Choose A Plural Noun: ")
while PluralNoun1 == (""):
    print("Your response can't be empty!")
    PluralNoun1 = input("Please Enter in A Plural Noun: ")
Noun2 = input("Choose A Noun: ")
NamePlace1 = input("Name A place: ")
Adj1 = input("Choose and adjective: ")


# Output line

print("Here is your Mad lib: ")
print("Did you Know I have a pet " +Noun1 +"?") 
print("He likes to run around and play with all the " +PluralNoun1+ ".")
print("One Morning, I woke up and he was wearing a " +Noun2+ " for a hat!")
print("I especially like to take him to the " +NamePlace1+ " because he shows off his " +Adj1+ "side." )