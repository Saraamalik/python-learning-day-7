import datetime

# Current date
today = datetime.date.today()
print("Today's date is:", today)

# Current date and time
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)

# Current time
current_time = datetime.datetime.now().time()
print("Current time is:", current_time)

# Year, month and day
year = today.year
month = today.month
day = today.day

print("Year:", year)
print("Month:", month)
print("Day:", day)

# Custom date
my_date = datetime.date(2007, 2, 18)
print("My date is:", my_date)

# Date difference
date1 = datetime.date(2026, 9, 19)
date2 = datetime.date(2026, 12, 25)

difference = date2 - date1

print("Difference:", difference.days, "days")
