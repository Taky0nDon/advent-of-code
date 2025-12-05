def get_input(path: str) -> str:
    with open("input") as f:
        data = f.read()
    return data.strip()

def get_banks(data: str, sep=" ") -> list[str]:
    return data.split(sep)

def find_max_battery(bank: str, heap_size=2) -> int:
    batteries = list(enumerate([int(c) for c in bank]))
    first_digit = max(batteries, key=lambda x: x[1])
    if first_digit[0] == len(bank) - 1:
        first_digit = max(batteries[:-1], key=lambda x: x[1])
    second_digit = max(batteries[first_digit[0]+1:], key=lambda x: x[1])
    return first_digit[1] * 10 + second_digit[1]



sample = "987654321111111 811111111111119 234234234234278 818181911112111" 
actual = get_input("input")

DATA = actual
if __name__ == "__main__":
    all_banks = get_banks(DATA, "\n")
    res = 0
    for bank in all_banks:
        res += find_max_battery(bank)
    print(res)
