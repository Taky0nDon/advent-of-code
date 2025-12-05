from day3_p1 import get_input, get_banks, sample

def turn_on_batteries(bank: string, num_on: int):
    bank_size = len(bank)
    l = 0
    r = bank_size - num_on + 1
    on_bats = []
    while r <= bank_size and len(on_bats) < 12:
        index_batt_list = list(enumerate(bank))
        index, batt = max(index_batt_list[l:r], key=lambda x: x[1])
        on_bats.append(batt)
        old_l = l
        l = index + 1
        r += 1
    return int("".join(on_bats))


actual = get_input("input")

if __name__ == "__main__":
    all_banks = get_banks(actual, "\n")
    res = 0
    for bank in all_banks:
        res += turn_on_batteries(bank, 12)
    print(res)

