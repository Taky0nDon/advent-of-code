with open('input') as data:
    lines = [l.strip() for l in data.readlines()]
# Remove empty line
class Result():
    def __init__(self):
        self.count = 0


def analyze_lines(lines: list[str]):
    ans.count += get_rights(lines)
    ans.count += get_ups(lines)
    ans.count += get_downs(lines)
    ans.count += get_down_rights(lines)
    ans.count += get_down_lefts(lines)
    ans.count += get_up_lefts(lines)
    ans.count += get_up_rights(lines)
    for line in lines:
        ans.count += get_lefts(line)




def get_ups(lines: list[str]) -> int:
    up_count = 0
    for i_l, line in enumerate(lines):
        result = ""
        if i_l < 3:
            continue
        for i_c, char in enumerate(line):
            if char == "X":
                result = char
                result += "".join([lines[i_l - n][i_c] for n in range(1, 4)])
                if result == "XMAS":
                    up_count += 1
                else:
                    result = ""
    return up_count


def get_downs(lines: list[str]) -> int:
    down_count = 0
    for i_l, l in enumerate(lines):
        result = ""
        for i_c, c in enumerate(l):
            if c == "X":
                result += c
                try:
                    result += "".join([lines[i_l + n][i_c] for n in range(1, 4)])
                except IndexError:
                    result = ""
                    continue
                finally:
                    if result == "XMAS":
                        down_count += 1
                    result = ""
    return down_count


        
def get_lefts(line: str) -> int:
    left_count = 0
    for i, char in enumerate(line):
        if i < 3:
            continue
        elif char == "X" and line[i-1] == "M" and line[i-2] == "A" and line[i-3] == "S":
            left_count += 1
    return left_count


def get_rights(lines: list[str]) -> int:
    right_counts = 0
    for l in lines:
        right_counts += l.count("XMAS")
    return right_counts

def get_down_rights(lines: list[str]) -> int:
    down_right_count = 0
    for i_l, l in enumerate(lines):
        result = ""
        for i_c, c in enumerate(l):
            if c == "X":
                result += c
                try:
                    result += "".join(
                            [lines[i_l + n][i_c + n] for n in range(1,4)]
                            )
                except IndexError:
                    result = ""
                    continue
                finally:
                    if result == "XMAS":
                        down_right_count += 1
                    result = ""
    return down_right_count

def get_down_lefts(lines: list[str]) -> int:
    down_left_count = 0
    for i_l, l in enumerate(lines):
        result = ""
        for i_c, c in enumerate(l):
            if i_c < 3:
                continue
            if c == "X":
                result += c
                try:
                    result += "".join(
                            [lines[i_l + n][i_c - n] for n in range(1,4)]
                            )
                except IndexError:
                    result = ""
                    continue
                finally:
                    if result == "XMAS":
                        down_left_count += 1
                    result = ""
    return down_left_count

def get_up_rights(lines: list[str]) -> int:
    up_right_count = 0
    for i_l, l in enumerate(lines):
        result = ""
        if i_l < 3:
            continue
        for i_c, c in enumerate(l):
            if c == "X":
                result += c
                try:
                    result += "".join(
                            [lines[i_l - n][i_c + n] for n in range(1,4)]
                            )
                except IndexError:
                    result = ""
                    continue
                finally:
                    if result == "XMAS":
                        up_right_count += 1
                    result = ""
    return up_right_count


def get_up_lefts(lines: list[str]) -> int:
    up_left_count = 0
    for i_l, l in enumerate(lines):
        result = ""
        if i_l < 3:
            continue
        for i_c, c in enumerate(l):
            if i_c < 3:
                continue
            if c == "X":
                result = c
                try:
                    result += "".join(
                            [lines[i_l - n][i_c - n] for n in range(1,4)]
                            )
                except IndexError as e:
                    result = ""
                    continue
                finally:
                    if result == "XMAS":
                        up_left_count += 1
                    result = ""
    return up_left_count

ans = Result()
analyze_lines(lines)
print(ans.count)
