from models import Hotel, Room, Service, Booking
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
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




# Implement other hotel-related functions similarly
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
        print("11. Exit")
        
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
            exit_program()
        else:
            print("Invalid choice. Please try again.")




if __name__ == "__main__":
    main_menu()
