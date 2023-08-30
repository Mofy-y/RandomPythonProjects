#Ticket Price
age = int(input("Enter your age: "))
time_of_day = input("Enter the time of day (morning, afternoon, evening): ").casefold()

base_price = 5000
final_price = base_price

if age < 6:
    print("Free tickets for children under the age of 6")
elif age >= 6 and age <= 12:
    final_price = base_price * 0.5
    print("Children aged 6-12 get a 50% discount")
    if time_of_day == "morning":
        final_price *= 0.8
        print("Applied a 20% discount for morning tickets")
    elif time_of_day == "evening":
        print("Applied a 20% surcharge for evening tickets")
        final_price *= 1.2
    elif time_of_day == "afternoon":
        print("No discounts for afternoon tickets")
    else:
        print("Enter valid response")
elif age >= 65:
    print("base_price = 5000 naira")
    final_price = base_price * 0.7
    print("Seniors aged 65 and above get a 30% discount")
    print("Price = ", final_price)
else:
    print("base_price = 5000 naira")
    print("You are to pay normal price")

#condition statement for the time of day price

if time_of_day == "morning":
    final_price *= 0.8
    print("Applied a 20% discount for morning tickets")
elif time_of_day == "evening":
    final_price *= 1.2
    print("Applied a 20% surcharge for evening tickets")
elif time_of_day == "afternoon":
    print("No discounts for afternoon tickets")
else:
    print("Enter valid response")

print("Final Price= ", final_price)

