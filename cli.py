from models import Hotel, Room, Service, Booking
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from datetime import datetime
import sys

# Create SQLite engine
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Bind the engine to a sessionmaker
Session = sessionmaker(bind=engine)

# Create a session object
session = Session()

def exit_program():
    print("Goodbye!")
    sys.exit()

def list_hotels():
    """Function to list all hotels."""
    hotels = session.query(Hotel).all()
    for hotel in hotels:
        print(hotel.name)  

def find_hotel_by_name():
    name = input("Enter the hotel's name: ")
    hotel = session.query(Hotel).filter(Hotel.name == name).first()
    if hotel:
        print(f"Hotel Name: {hotel.name}")
        print(f"Location: {hotel.location}")
        print(f"Description: {hotel.description}")
        
    else:
        print(f'Hotel {name} not found')
def create_hotel():
    name = input("Enter the hotel's name: ")
    location = input("Enter the hotel's location: ")
    description = input("Enter the hotel's description: ")

    new_hotel = Hotel(name=name, location=location, description=description)
    session.add(new_hotel)
    session.commit()
    print(f"Hotel {name} created successfully.")

def update_hotel():
    name = input("Enter the hotel's name to update: ")
    hotel = session.query(Hotel).filter(Hotel.name == name).first()
    if hotel:
        new_name = input("Enter the new name for the hotel: ")
        new_location = input("Enter the new location for the hotel: ")
        new_description = input("Enter the new description for the hotel: ")

        hotel.name = new_name
        hotel.location = new_location
        hotel.description = new_description

        session.commit()
        print(f"Hotel {name} updated successfully.")
    else:
        print(f'Hotel {name} not found.')

def delete_hotel():
    name = input("Enter the hotel's name to delete: ")
    hotel = session.query(Hotel).filter(Hotel.name == name).first()
    if hotel:
        session.delete(hotel)
        session.commit()
        print(f"Hotel {name} deleted successfully.")
    else:
        print(f'Hotel {name} not found.')

def list_rooms():
    """Function to list all rooms."""
    rooms = session.query(Room).all()
    for room in rooms:
        print(room.number)

def find_room_by_number():
    number = input("Enter the room's number: ")
    room = session.query(Room).filter(Room.number == number).first()
    if room:
        print(f"Hotel Number: {room.number}")
        print(f"Capacity: {room.capacity}")
        print(f"Price_per_night: {room.price_per_night}")

def create_room():
    number = input("Enter the room's number: ")
    capacity = input("Enter the room's capacity: ")
    price_per_night= input("Enter the room's price_per_night: ")

    new_room = Room(number=number, capacity=capacity,price_per_night=price_per_night)
    session.add(new_room)
    session.commit()
    print(f"Room {number} created successfully.")

def update_room():
    number = input("Enter the room's number to update: ")
    room = session.query(Room).filter(Room.number==number).first()
    if room:
        new_number = input("Enter the new number for the room: ")
        new_capacity= input("Enter the new capacity for the room: ")
        new_price_per_night = input("Enter the new price per night for the room: ")

        room.number = new_number
        room.capacity = new_capacity
        room.price_per_night = new_price_per_night

        session.commit()
        print(f"Room {number} updated successfully.")
    else:
        print(f'Room {number} not found.')


def delete_room():
    number = input("Enter the room's number to delete: ")
    room = session.query(Room).filter(Room.number == number).first()
    if room:
        session.delete(room)
        session.commit()
        print(f"Room {number} deleted successfully.")
    else:
        print(f'Room {number} not found.')

def list_bookings():
    """Function to list all bookings."""
    bookings = session.query(Booking).all()
    for booking in bookings:
        print(f"Booking ID: {booking.id}, Check-in Date: {booking.check_in_date}, Check-out Date: {booking.check_out_date}")

def find_booking_by_id():
    booking_id = int(input("Enter the booking ID: "))
    booking = session.query(Booking).get(booking_id)
    if booking:
        print(f"Booking ID: {booking.id}, Check-in Date: {booking.check_in_date}, Check-out Date: {booking.check_out_date}")
    else:
        print("Booking not found.")


# Convert the check-in date string to a date object
check_in_date_str = '2023-01-03'
check_in_date = datetime.strptime(check_in_date_str, '%Y-%m-%d').date()



def create_booking():
    check_out_date = input("Enter the check-out date (YYYY-MM-DD): ")
    room_id = input("Enter the room ID: ")
    new_booking = Booking(check_in_date=check_in_date, check_out_date=check_out_date, room_id=room_id)
    session.add(new_booking)
    session.commit()
    print("Booking created successfully.")

def update_booking():
    booking_id = input("Enter the booking ID to update: ")
    booking = session.query(Booking).get(booking_id)
    if booking:
        check_out_date = input("Enter the new check-out date (YYYY-MM-DD): ")
        room_id = input("Enter the new room ID: ")

        # Update the Booking instance with the converted check_in_date
        booking.check_in_date = check_in_date
        booking.check_out_date = check_out_date
        booking.room_id = room_id

        session.commit()
        print("Booking updated successfully.")
    else:
        print("Booking not found.")



def delete_booking():
    booking_id = input("Enter the booking ID to delete: ")
    booking = session.query(Booking).get(booking_id)
    if booking:
        session.delete(booking)
        session.commit()
        print("Booking deleted successfully.")
    else:
        print("Booking not found.")

def list_services():
    services = session.query(Service).all()
    for service in services:
        print(service.name)

def find_service_by_id():
    service_id = input("Enter the service ID: ")
    service = session.query(Service).filter(Service.id == service_id).first()
    if service:
        print(f"Service ID: {service.id}")
        print(f"Service Name: {service.name}")
    else:
        print("Service not found.")


def create_service():
    name = input("Enter the service name: ")

    new_service = Service(name=name)
    session.add(new_service)
    session.commit()
    print("Service created successfully.")

def update_service():
    service_id = input("Enter the service ID to update: ")
    service = session.query(Service).get(service_id)
    if service:
        new_name = input("Enter the new service name: ")
        service.name = new_name
        session.commit()
        print("Service updated successfully.")
    else:
        print("Service not found.")

def delete_service():
    service_id = input("Enter the service ID to delete: ")
    service = session.query(Service).get(service_id)
    if service:
        session.delete(service)
        session.commit()
        print("Service deleted successfully.")
    else:
        print("Service not found.")

def main_menu():
    while True:
        print("\n=== Hotel Management System ===")
        print("1. List Hotels")
        print("2. Find Hotel by Name")
        print("3. Create Hotel")
        print("4. Update Hotel")
        print("5. Delete Hotel")
        print("6. List Rooms")
        print("7. Find Room by Number")
        print("8. Create Room")
        print("9. Update Room")
        print("10. Delete Room")
        print("11. List Bookings")
        print("12. Find Booking by ID")
        print("13. Create Booking")
        print("14. Update Booking")
        print("15. Delete Booking")
        print("16. List Services")
        print("17. Find Service by ID")
        print("18. Create Service")
        print("19. Update Service")
        print("20. Delete Service")
        print("21. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_hotels()
        elif choice == "2":
            find_hotel_by_name()
        elif choice == "3":
            create_hotel()
        elif choice == "4":
            update_hotel()
        elif choice == "5":
            delete_hotel()
        elif choice == "6":
            list_rooms()
        elif choice == "7":
            find_room_by_number()
        elif choice == "8":
            create_room()
        elif choice == "9":
            update_room()
        elif choice == "10":
            delete_room()
        elif choice == "11":
            list_bookings()
        elif choice == "12":
            find_booking_by_id()
        elif choice == "13":
            create_booking()
        elif choice == "14":
            update_booking()
        elif choice == "15":
            delete_booking()
        elif choice == "16":
            list_services()
        elif choice == "17":
            find_service_by_id()
        elif choice == "18":
            create_service()
        elif choice == "19":
            update_service()
        elif choice == "20":
            delete_service()
        elif choice == "21":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
