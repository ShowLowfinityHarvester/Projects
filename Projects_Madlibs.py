print("Madlibs Ver 1.0")
Noun1 = input("Choose A Noun: ")
while Noun1 == (""):
    print("Your response can't be empty!")
    Noun1 = input("Please Enter In A Noun: ")
PluralNoun = input("Choose A Plural Noun: ")
while PluralNoun == (""):
    print("Your response can't be empty!")
    PluralNoun = input("Please Enter In A Plural Noun: ")
Noun2 = input("Choose A Noun: ")
while Noun2 ==(""):
    print("Your response can't be empty!")
    Noun2 = input("Please Enter In A Noun: ")
Place = input("Name A place: ")
while Place ==(""):
    print("Your response can't be empty!")
    Place = input("Please Enter In A Place (ex. Walmart): ")
Adj = input("Choose and adjective: ")
while Adj ==(""):
    print("Your response can't be empty!")
    Adj = input("Please Enter In A Noun: ")


# Output line

print("Here is your Mad lib: ")
print("Did you Know I have a pet " +Noun1 +"?") 
print("He likes to run around and play with all the " +PluralNoun+ ".")
print("One Morning, I woke up and he was wearing a " +Noun2+ " for a hat!")
print("I especially like to take him to the " +Place+ " because he shows off his " +Adj+ " side." )