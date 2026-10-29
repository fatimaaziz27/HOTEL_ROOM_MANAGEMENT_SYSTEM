# Hotel details
total_rooms = 10
available_rooms = []
occupied_rooms = []

# Add hotel rooms
for room_number in range(1, total_rooms + 1):
    available_rooms.append({
        "room": room_number,
        "guest": "",
        "rate": 2000
    })

# Function to show available rooms
def show_rooms():
    print(f"\nAvailable Rooms: {len(available_rooms)} / {total_rooms}")

    if not available_rooms:
        print("No rooms available!\n")
    else:
        for room in available_rooms:
            print(f"Room: {room['room']}, Rate: Rs.{room['rate']}/night")
        print()

# Function to check in a guest
def check_in():
    if not available_rooms:
        print("Hotel is fully occupied!\n")
        return

    guest_name = input("Enter guest name: ")
    room_number = int(input("Enter room number: "))

    for room in available_rooms:
        if room["room"] == room_number:
            room["guest"] = guest_name
            available_rooms.remove(room)
            occupied_rooms.append(room)

            print(f"Guest {guest_name} checked in successfully!")
            print(f"Room Number: {room_number}\n")
            return

    print("Room not available or invalid room number!\n")

# Function to check out a guest
def check_out():
    room_number = int(input("Enter room number for checkout: "))

    for room in occupied_rooms:
        if room["room"] == room_number:
            nights = int(input("Enter number of nights stayed: "))

            if nights <= 0:
                print("Number of nights must be greater than zero!\n")
                return

            total_bill = nights * room["rate"]

            print("\n--- Checkout Details ---")
            print(f"Guest Name: {room['guest']}")
            print(f"Room Number: {room['room']}")
            print(f"Nights Stayed: {nights}")
            print(f"Total Bill: Rs.{total_bill}")

            room["guest"] = ""
            occupied_rooms.remove(room)
            available_rooms.append(room)

            print("Guest checked out successfully!\n")
            return

    print("Occupied room not found!\n")

# Function to display occupied rooms
def show_occupied_rooms():
    if not occupied_rooms:
        print("No rooms are currently occupied.\n")
    else:
        print("\n--- Occupied Rooms ---")

        for room in occupied_rooms:
            print(
                f"Room: {room['room']}, "
                f"Guest: {room['guest']}, "
                f"Rate: Rs.{room['rate']}/night"
            )

        print()

# Main loop
while True:
    print("0. Exit")
    print("1. Show Available Rooms")
    print("2. Check In Guest")
    print("3. Check Out Guest")
    print("4. Show Occupied Rooms")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting Hotel Room Management System...")
        break
    elif choice == "1":
        show_rooms()
    elif choice == "2":
        check_in()
    elif choice == "3":
        check_out()
    elif choice == "4":
        show_occupied_rooms()
    else:
        print("Invalid choice, try again.\n")
