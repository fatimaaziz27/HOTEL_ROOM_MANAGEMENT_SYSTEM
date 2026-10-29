# Hotel Room Management System

A simple, menu-driven Hotel Room Management System built using Python to manage hotel rooms, guest check-ins, check-outs, and billing.

## About

This project is a console-based application that manages **10 hotel rooms**. Users can view available rooms, check guests in, check guests out, and display occupied rooms.

Each room has a fixed rate of **Rs. 2,000 per night**. When a guest checks out, the system calculates the total bill based on the number of nights stayed.

## Features

- Display available rooms
- Manage 10 hotel rooms
- Check guests in
- Check guests out
- Store guest names
- Track occupied rooms
- Display occupied room details
- Calculate bills based on nights stayed
- Validate the number of nights
- Handle invalid menu choices

## Technologies Used

- Python

## Python Concepts Practiced

- Variables and data types
- Lists
- Dictionaries
- Functions
- `for` loops
- `while` loops
- Conditional statements
- `range()`
- User input using `input()`
- Type conversion using `int()`
- List methods such as `append()` and `remove()`
- F-strings
- Arithmetic operations

## How It Works

### 1. Room Initialization

The system creates 10 rooms automatically when the program starts. Each room has a room number, an empty guest name, and a fixed nightly rate.

### 2. Show Available Rooms

Displays the number of available rooms and their room numbers and nightly rates.

### 3. Check In Guest

The user enters a guest name and room number. If the room is available, it is assigned to the guest and moved to the occupied rooms list.

### 4. Check Out Guest

The user enters the occupied room number and the number of nights stayed. The system calculates the bill and makes the room available again.

### 5. Calculate Hotel Bill

The total bill is calculated using this formula:

```text
Total Bill = Number of Nights × Room Rate
```

**Example:**

- Room rate: Rs. 2,000 per night
- Nights stayed: 3
- Total bill: Rs. 6,000

### 6. Show Occupied Rooms

Displays the room numbers, guest names, and nightly rates for all occupied rooms.

## Menu Options

| Option | Function |
|---|---|
| 0 | Exit |
| 1 | Show Available Rooms |
| 2 | Check In Guest |
| 3 | Check Out Guest |
| 4 | Show Occupied Rooms |

## How to Run

1. Clone or download the repository.
2. Open the project folder in your code editor.
3. Make sure Python is installed.
4. Run the following command in the terminal:

```bash
python Hotel_Room_Management_System.py
```
