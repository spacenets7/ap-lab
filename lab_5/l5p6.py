class BookingError(Exception):
    pass

available_seats = 20
fare_per_ticket = 500

try:
    name = input("Enter Passenger Name: ").strip()
    if not name:
        raise BookingError("Passenger name cannot be empty")

    age = int(input("Enter Age: "))
    tickets = int(input("Enter Number of Tickets: "))

    if age <= 0:
        raise BookingError("Age must be greater than zero")
    if tickets <= 0:
        raise BookingError("Number of tickets must be greater than zero")
    if tickets > 6:
        raise BookingError("Maximum 6 tickets can be booked")
    if tickets > available_seats:
        raise BookingError("Requested tickets exceed available seats")

    fare = fare_per_ticket * tickets
    available_seats -= tickets

    print("\nPassenger Name:", name)
    print("Age:", age)
    print("Tickets:", tickets)
    print("Fare:", fare)
    print("Remaining Seats:", available_seats)

except ValueError:
    print("Age and tickets must be integers")
except BookingError as e:
    print(e)
