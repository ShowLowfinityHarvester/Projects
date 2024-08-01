# var examples

Name = "Name"
Age = 24
FavYear = "2012"

print(Name)
print(Age)
print(FavYear)

# input

VehModel = input('What model of vehicle do currently have? be sure to include the year: ')

print("You said you have a " + VehModel+ ". Looking at parts for you!")

# Syntax and comments

# print nombre <- This will not print!!!!

print("Under Development!")

#           |
# data types V

# "32" is a string!
# 32 (no quotes) is an integer!
# 32.0 is a float!

Temp = -23
cars = 2

# converting data types

# Integer

NumberOfFord = 15
NumberOfFord = int("15")
print(NumberOfFord)

#String

NumberOfFord = 2340
NumberOfFord = str(2340)
print(NumberOfFord)

# Float

NumberOfFord = 1293
NumberOfFord = float(1293)
print(NumberOfFord)

# Converting inputs

ManufacturePlant = int(input("How many cars are in the Plant? "))
FordCars = ManufacturePlant + 5
print(FordCars)

# Concatenation Exs

Car1 = "Car Make is"
Car2 = "2002 "
Car3 = "Ford Focus"
Car4 = Car1 + Car2 + Car3

print(Car4)

# Extra Code

MakeYear = '2002'
MakeYear = int("2002")
Miles = 142527
Engine = 5.68
Engine = int(5.68)

print(MakeYear)
print(Engine)

WheelPSI = 41
WheelPSI = float(41)
print(WheelPSI)

# wh?

c = 4 % 4
print(c)

# String Methods

string1 = "sissy liberals"
print(string1[4:9])
print(string1.split())
print(len(string1))
print(string1.find("s"))

# check strings

string1 = "Firetrucks are red"
Check = "red" in string1
print(Check)

# conctenating numbers

string1 = "The total milage of the car you are looking to by is {} miles."
milage = 210872
print(string1.format(milage))

string1 = "The total milage of the car you are looking to by is {} miles. Your car is expected to run without breaking down for about {} more miles."
milage = 210872
RemainingMilage = 500
print(string1.format(milage, RemainingMilage))

# lists

AlbumsTurning10YrsOld = ["V", "Whatever else came out in 2014"]
print(list)

# If statements

AvaTyAge = 28
RandoAge = 17

if RandoAge > 18:
    print("You are in the clear")
else:
    print("Exposed!!!")

# Conditionals (Buggy!)

age = int(input('What is your age? -> '))
license = True
if age >= 16 and "license" == True:
    print("You are old enough to drive")
else:
    print("You are not able to drive")

# Else if statements

coins = 10

if coins > 20:
    print("You have more than enough to buy a puppy")
elif coins == 20:
    print("You have exactly enough to buy a puppy")
else:
    print("you do not have enough to buy a puppy")