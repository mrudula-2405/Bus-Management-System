from system import BusManagementSystem

system = BusManagementSystem()

while True:
    print("\n====== Bus Management System ======")
    print("1. Add Bus")
    print("2. View Buses")
    print("3. Delete Bus")
    print("4. Book Ticket")
    print("5. View Passengers")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_bus()
    elif choice == "2":
        system.view_buses()
    elif choice == "3":
        system.delete_bus()
    elif choice == "4":
        system.book_ticket()
    elif choice == "5":
        system.view_passengers()
    elif choice == "6":
        break
    else:
        print("Invalid choice!")
