print("Vaccum cleaner using Table Driven agent")
rooms = {"A": "dirty", "B": "dirty", "C": "dirty", "D": "dirty"}  # Initial state
print("Table Driven Approach")

lookup_table = {
    ("dirty",): "clean",
    ("clean",): "move",
}
def table_driven_agent(current_room):
    # Check the state of the current room
    room_state = (rooms[current_room],)

    # Perform action based on the lookup table
    if lookup_table[room_state] == "clean":
        print(f"Cleaning {current_room}.")
        rooms[current_room] = "clean"
    elif lookup_table[room_state] == "move":
        print(f"{current_room} is already clean. Moving to the next room.")

# Execution
for room in rooms:
    table_driven_agent(room)

print("Final state of rooms:",rooms)
#Using Simple Reflexive
print("Vaccum cleaner using Simple reflexive agent")
rooms = ["A", "B", "C", "D"]
room_states = {room: "dirty" for room in rooms}  # Initial state: all rooms dirty
print("Simple Reflexive Approach")
def reflex_agent():
    for room in rooms:
        if room_states[room] == "dirty":
            print(f"Cleaning room {room}.")
            room_states[room] = "clean"
        elif room_states[room] == "clean":
            print(f"Room {room} is already clean.")
        print(f"State of rooms: {room_states}")

# Execute cleaning process
reflex_agent()
print("Final state of rooms:",room_states)
