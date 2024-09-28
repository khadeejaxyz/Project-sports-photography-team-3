str="""Welcome to sports photography booking
"Great photography is about depth of feeling not depth of the feild"
                                                        ~ Peter Adam
Experience our newest photography booking session now.
created for the greater good :)"""
print(str)                                                        
class Booking:
    def __init__(self, client_name, date, event_time, location):
        self.client_name = client_name
        self.date = date  # (year, month, day)
        self.event_time = event_time
        self.location = location
    def __str__(self):
        yy, mm, dd = self.date
        return f"Booking for {self.client_name} on {yy}/{mm}/{dd} at {self.event_time} at {self.location}."

class PhotographyBookingSystem:
    def __init__(self):
        self.bookings = []
        
    def add_booking(self, client_name, date, event_time, location):
        new_booking = Booking(client_name, date, event_time, location)
        self.bookings.append(new_booking)
        print(f"Booking added: {new_booking}")

    def view_bookings(self):
        if not self.bookings:
            print("No bookings available.")
        else:
            for booking in self.bookings:
                print(booking)

    def cancel_booking(self, client_name, date):
        for booking in self.bookings:
            if booking.client_name == client_name and booking.date == date:
                self.bookings.remove(booking)
                print(f"Booking canceled: {booking}")
                return
        print("Booking not found.")

def is_valid_date(yy, mm, dd):
    if mm < 1 or mm > 12:
        return False
    if dd < 1 or dd > 31:
        return False
    if mm in {4, 6, 9, 11} and dd > 30:
        return False
    if mm == 2:
        if (yy % 4 == 0 and yy % 100 != 0) or (yy % 400 == 0):
            return dd <= 29  # Leap year
        return dd <= 28
    return True

def main():
    system = PhotographyBookingSystem()

    while True:
        print("\nSPORTS PHOTOGRAPHY BOOKING")
        print("1. Add Booking")
        print("2. View Bookings")
        print("3. Cancel Booking")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            client_name = input("Enter client name: ")
            while True:
                try:
                    yy, mm, dd = map(int, input("Enter the event date (YYYY MM DD): ").split())
                    if not is_valid_date(yy, mm, dd):
                        print("Please enter a valid date.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter the date in valid format.")

            event_time = input("Enter event time (HH:MM): ")
            location = input("Enter location: ")
            system.add_booking(client_name, (yy, mm, dd), event_time, location)

        elif choice == '2':
            system.view_bookings()

        elif choice == '3':
            client_name = input("Enter client name: ")
            try:
                yy, mm, dd = map(int, input("Enter event date (YYYY MM DD): ").split())
                system.cancel_booking(client_name, (yy, mm, dd))
            except ValueError:
                print("Invalid input. Please enter the date as three integers.")

        elif choice == '4':
            str="""Exiting the system.
Thankyou for choosing us for your booking
Hoping you had an esay and convenient booking session
Have a great day!"""
            print(str)
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
