with open("padded_input") as data:
    lines = data.readlines()

from pathlib import Path


def parse_input(input: str) -> list[str]:
    return input.strip().splitlines()

rights = 0
def extract_strings_one(m: int, n: int, haystack: list[str], l: int = 4) -> list[str]:
    global rights
    result = []
    # Right
    if m + l <= len(haystack[n]):
        right_str = haystack[n][m : m + l]
        result.append(right_str)
        if right_str == "XMAS":
            rights += 1
        print(f"right {rights}")
    # Up-Right
    if m + l <= len(haystack[n]) and n > l - 2:
        result.append("".join([haystack[n - i][m + i] for i in range(l)]))
    # Up
    if n > l - 2:
        result.append("".join([haystack[n - i][m] for i in range(l)]))
    # Up-Left
    if m > l - 2 and n > l - 2:
        result.append("".join([haystack[n - i][m - i] for i in range(l)]))
    # Left
    if m > l - 2:
        result.append("".join([haystack[n][m - i] for i in range(l)]))
    # Down-Left
    if m > l - 2 and n + l <= len(haystack):
        result.append("".join([haystack[n + i][m - i] for i in range(l)]))
    # Down
    if n + l <= len(haystack):
        result.append("".join([haystack[n + i][m] for i in range(l)]))
    # Down-Right
    if m + l <= len(haystack[n]) and n + l <= len(haystack):
        result.append("".join([haystack[n + i][m + i] for i in range(l)]))
    return result


def extract_strings_two(m: int, n: int, haystack: list[str], d: int = 1) -> list[str]:
    result = []
    if 0 <= m - d and m + d < len(haystack[n]) and 0 <= n - d and n + d < len(haystack):
        result.append("".join([haystack[n + i][m + i] for i in range(-d, d + 1)]))
        result.append("".join([haystack[n - i][m + i] for i in range(-d, d + 1)]))
    return result


def part_one(input: str) -> int:
    lines = parse_input(input)
    xmas_count = 0
    for i, line in enumerate(lines):
        x = line.find("X", 0)
        while x != -1:
            xmas_count += len(
                list(filter(lambda s: s == "XMAS", extract_strings_one(x, i, lines)))
            )
            x = line.find("X", x + 1)
    return xmas_count


def part_two(input: str) -> int:
    lines = parse_input(input)
    x_mas_count = 0
    for i, line in enumerate(lines[1:-1], 1):
        a = line.find("A", 0)
        while a != -1:
            if (
                len(
                    list(
                        filter(
                            lambda s: s in ("MAS", "SAM"),
                            extract_strings_two(a, i, lines),
                        )
                    )
                )
                == 2
            ):
                x_mas_count += 1
            a = line.find("A", a + 1)
    return x_mas_count


if __name__ == "__main__":
    input = Path("input").read_text("utf-8")
    print(part_one(input))
    print(part_two(input))# acc = 0
# for row, l in enumerate(lines):
#     for col, c in enumerate(l):
#         if c == 'X':
#             w = l[col - 3:col + 1]
#             e = l[col:col + 4]
#             n = c + lines[row - 1][col] + \
#                 lines[row - 2][col] + lines[row - 3][col]
#             s = c + lines[row + 1][col] + \
#                 lines[row + 2][col] + lines[row + 3][col]
#             nw = c + lines[row - 1][col - 1] + \
#                 lines[row - 2][col - 2] + lines[row - 3][col - 3]
#             ne = c + lines[row - 1][col + 1] + \
#                 lines[row - 2][col + 2] + lines[row - 3][col + 3]
#             sw = c + lines[row + 1][col - 1] + \
#                 lines[row + 2][col - 2] + lines[row + 3][col - 3]
#             se = c + lines[row + 1][col + 1] + \
#                 lines[row + 2][col + 2] + lines[row + 3][col + 3]
#             for word in [w, e, n, s, nw, ne, sw, se]:
#                 if word in ['XMAS', 'SAMX']:
#                     acc += 1
# print(acc)
