#Welcome Message to the program
print("Welcome to my Python program!")

#Gets users hours and turns it into a float then multiplies by 7 for weekly hours 
hours = input("How many hours did you study today? ")
hours = float(hours)
weekly_hours = hours * 7

#Prints calulated result
print(f"You are on track to study {weekly_hours} hours this week.")

#Error Prevention
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()