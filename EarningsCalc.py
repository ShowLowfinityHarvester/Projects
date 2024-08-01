while True:
    try:
        askusr = int(input("How much money do you want to save in a year? (Please do not put commas in your number!!!) -> "))
        break
    except ValueError:
        print("Are we using letters and symbols for money now? Please enter in the amount of money you want to save per year, so we can calculate how much you need to save in a month, week and day!")
totalMonth = round(askusr / 12, 2)
totalWeek = round(askusr / 52, 2)
totalDay = round(askusr / 365, 2)


Message = "To save up {} dollars in 1 year, you will need to save {} dollars per month, which is about {} dollars per week, and {} dollars per day."
print(Message.format(askusr, totalMonth, totalWeek, totalDay))