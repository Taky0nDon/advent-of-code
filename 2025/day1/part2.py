from doubly_linked_list import DoublyLinkedNode

def get_input(path) -> str:
    with open(path) as file:
        inp = file.read().strip()
    return inp

def parse_instructions(instructions: str) -> tuple(str, int):
    dir = instructions[0]
    clicks = int(instructions[1:])
    return dir, clicks

def get_next_position(dir: str, clicks: int, current_position: int) -> int:
    match dir:
        case "L":
            new_pos = current_position - clicks
        case "R":
            new_pos = current_position + clicks

    if new_pos not in range(0, 100):
        new_pos %= 100
    return new_pos

def rot_passes_zero_n_times(dir: str, clicks: int, current_position: int) -> bool:
    start = DoublyLinkedNode().build_list(current_position)
    print(f"start: {start.val}")
    print(f"rotating {clicks} clicks")
    passes_zero = 0
    match dir:
        case "L":
            for _ in range(clicks):
                start = start.prev
                if start.val == 0:
                    passes_zero += 1
            print("new pos: ", start.val)
        case "R":
            for _ in range(clicks):
                start = start.next
                if start.val == 0:
                    passes_zero += 1
            print("new pos: ", start.val)
    return passes_zero


if __name__ == "__main__":
    inp = get_input("input")
    #inp = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"
    instructions = inp.split("\n")
    current_position = 50
    pw = 0
    print(f"pos: {current_position}")
    for i in instructions:
        d, c = parse_instructions(i)
        pw += rot_passes_zero_n_times(d, c, current_position)
        current_position = get_next_position(d, c, current_position)
        print(f"pos: {current_position}")
    print(pw)
