# Bus Ticket Booking System
print(" Bus Ticket Booking system")
print("1. City A - ₹100")
print("2. City B - ₹270")
print("3. City C - ₹700")
print("4. City D - ₹934")
print("5. Exit")

# Ticket prices
ticket_cost= {
    "1": 100,
    "2": 270,
    "3": 700,
    "4": 934,
}

Desire_cities = ["City A", "City B", "City C", "City D"]

while True:
    # Input destination from user we take  for going or want to exit
    dest = input("Choose your destination (1-4) or 5 to Exit: ")
    
    if dest == "5":
        print("Exit")
        break

    if dest not in ticket_cost:
        print("Invalid choice. please try again.")
        continue

    # Number of tickets that we  want
    try:
        fare_tickets = int(input("How many tickets do you want? "))
        if fare_tickets<= 0:
            print("Invalid ticket number.")
            continue

        # Check for return ticket if you want or not
        is_return = input("Return ticket? (yes/no): ") 
        # Calculate total cost or if want to return
        cost = ticket_cost[dest] * fare_tickets
        if is_return:
                cost *= 2

        # Apply discount in booking over ticket price is greater than or equal to 5
        if fare_tickets >= 5:
            cost -= cost * 0.10

        # Summary of booking details
        print("Booking Details")
        print(f"City: {Desire_cities[int(dest)-1]}")
        print(f"Tickets: {fare_tickets}")
        print(f"Return: {'Yes' if is_return else 'No'}")
        print(f"Total Cost: ₹{cost}")

        # Confirmation of booking that you want to confirm or not
        confirm = input("Confirm booking? (yes/no): ")
        if confirm in ["yes"]:
            print("Booking confirmed! Enjoy your trip.")
        else:
            print("Booking cancelled.")
    except ValueError:
        print("Invalid input. Enter numbers only for tickets.")
