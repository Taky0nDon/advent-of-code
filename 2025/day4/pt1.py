def get_input(path: str, sep: str) -> str:
    with open(path) as f:
        return [_.strip() for _ in f.readlines()]


def pad_data(data: list[list[str]]) -> list[list[str]]:
    boundary = list("." * (len(data[0]) + 2))
    for i in range(len(data)):
        data[i] = list(f".{data[i]}.")
    data.insert(0, boundary)
    data.append(boundary)
    return data


def part_1(data: list[str]) -> int:
    num_rows = len(data)
    num_chars = len(data[0])
    accessible = 0
    for irow in range(1, num_rows - 1):
        for ichar in range(1, num_chars - 1):
            if data[irow][ichar] == "@":
                up = data[irow - 1][ichar - 1 : ichar + 2]
                down = data[irow + 1][ichar - 1 : ichar + 2]
                left = data[irow][ichar - 1]
                right = data[irow][ichar + 1]
                adjacent_rolls = f"{up}{down}{left}{right}".count("@")
                if adjacent_rolls < 4:
                    accessible += 1
    return accessible

def part_2(data):
    result = 0
    num_chars = len(data[0])
    accessible = None
    num_rows = len(data)
    num_chars = len(data[0])
    while accessible != 0:
        print("result: ", result)
        accessible = 0
        coords = []
        for irow in range(1, num_rows - 1):
            for ichar in range(1, num_chars - 1):
                if data[irow][ichar] == "@":
                    up = data[irow - 1][ichar - 1 : ichar + 2]
                    down = data[irow + 1][ichar - 1 : ichar + 2]
                    left = data[irow][ichar - 1]
                    right = data[irow][ichar + 1]
                    adjacent_rolls = f"{up}{down}{left}{right}".count("@")
                    if adjacent_rolls < 4:
                        print("accessible: ", accessible)
                        coords.append((irow, ichar))
                        accessible += 1
        result += accessible
                        
        for irow, ichar in coords:
            print(data[irow][ichar])
            data[irow][ichar] = "."

    return result

if __name__ == "__main__":
    DATA = "..@@.@@@@. @@@.@.@.@@ @@@@@.@.@@ @.@@@@..@. @@.@@@@.@@ .@@@@@@@.@ .@.@.@.@@@ @.@@@.@@@@ .@@@@@@@@. @.@.@@@.@.".split()
    safe_data = pad_data(get_input("input", "\n"))
    ans = part_1(safe_data)
    ans = part_2(safe_data)
    print(ans)
