print("USN: 1BM25CS489")
print("NAME: OMKAR SADASHIV KOKATNOOR")

states = [
    ("D", "D", "A"), 
    ("D", "D", "B"), 
    ("C", "D", "A"),  
    ("D", "C", "B"),
    ("D", "C", "A"),  
    ("C", "D", "B"),  
    ("C", "C", "A"), 
    ("C", "C", "B"), 
]


for state_number, (room_a, room_b, position) in enumerate(states, 1):
    print(f"\nState {state_number}")
    print(f"Room A: {room_a} | Room B: {room_b} | Agent: Room {position}")

    while room_a == "D" or room_b == "D":
        if position == "A":
            if room_a == "D":
                print("CLEAN Room A")
                room_a = "C"
            else:
                print("MOVE RIGHT: Room A -> Room B")
                position = "B"
        else:
            if room_b == "D":
                print("CLEAN Room B")
                room_b = "C"
            else:
                print("MOVE LEFT: Room B -> Room A")
                position = "A"

    print("Both rooms are clean")