from itertools import cycle 

def get_input(path) -> str:
    with open(path) as file:
        inp = file.read().strip()
    return inp

def get_next_position(instructions: str, current_position: int) -> int:
    dir = instructions[0]
    clicks = int(instructions[1:])

    match dir:
        case "L":
            new_pos = current_position - clicks
        case "R":
            new_pos = current_position + clicks

    if new_pos not in range(0, 100):
        new_pos %= 100
    return new_pos





if __name__ == "__main__":
    inp = get_input("input")
    instructions = inp.split("\n")
    current_position = 50
    pw = 0

    for i in instructions:
        t += 1
        current_position = get_next_position(i, current_position)
        if current_position == 0:
            pw += 1
    print(pw)
