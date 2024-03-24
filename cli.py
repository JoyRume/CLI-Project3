from helpers import (
    exit_program,
    list_hotels,
    find_hotel_by_name,
    create_hotel,
    update_hotel,
    delete_hotel,
    list_rooms,
    find_room_by_number,
    create_room,
    update_room,
    update_room,
    delete_room,
    list_bookings,
    find_booking_by_id,
    delete_booking,
    list_services,
    find_service_by_id,
    create_service,
    update_service,
    delete_service,
    
)

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
        print("13. Delete Booking")
        print("14. List Services")
        print("15. Find Service by ID")
        print("16. Create Service")
        print("17. Update Service")
        print("18. Delete Service")
        print("19. Exit")

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
            delete_booking()
        elif choice == "14":
            list_services()
        elif choice == "15":
            find_service_by_id()
        elif choice == "16":
            create_service()
        elif choice == "17":
            update_service()
        elif choice == "18":
            delete_service()
        elif choice == "19":
            exit_program()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

