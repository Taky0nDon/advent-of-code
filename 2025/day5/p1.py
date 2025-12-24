from copy import deepcopy as copy


def get_input(path: str) -> str:
    with open(path) as f:
        data = f.read()
    return data


def process_input(data: str) -> tuple[list[str], list[str]]:
    fresh_ranges, ingredient_ids = data.split("\n\n")
    return fresh_ranges.split(), ingredient_ids.split()


def get_range_boundaries(_range: list[str]) -> tuple[int, int]:
    lower, upper = (int(b) for b in _range.split("-"))
    upper += 1
    return lower, upper


def yield_range(ranges: list[str]) -> tuple[int, int]:
    for r in ranges:
        min, max = tuple(int(_) for _ in r.split("-"))
        yield min, max


def merge_boundaries(ranges: list[str]) -> set:
    """This may not be necessary."""
    ranges_generator = yield_range(ranges)
    valid_ranges = set()
    valid_ranges.add(tuple(next(ranges_generator)))
    merged = True
    while ranges_generator:
        try:
            current_pair = next(ranges_generator)
        except StopIteration:
            break
        else:
            valid_ranges.add(current_pair)
            print(current_pair)
            for new_pair in list(valid_ranges):
                print("1", valid_ranges)
                print(f"checking {current_pair=} and {new_pair=}")
                if pairs_overlap(current_pair, new_pair):
                    pass
                else:
                    valid_ranges.add(new_pair)

    merged = True
    start = None
    while start != list(valid_ranges):
        start = copy(list(valid_ranges))
        for rang in copy(list(valid_ranges)):
            for rang2 in list(valid_ranges):
                if rang is rang2:
                    continue
                if pairs_overlap(rang, rang2):
                    print("abcdef")
                    print(f"need to merge {rang} and {rang2}")
                    try:
                        valid_ranges.remove(rang)
                    except KeyError:
                        pass
                    valid_ranges.remove(rang2)
                    new_r = tuple([min(rang[0], rang2[0]), max(rang[1], rang2[1])])
                    valid_ranges.add(new_r)

        print(rang)
    return valid_ranges


def pairs_overlap(*args: tuple[int, int]) -> bool:
    overlaps = False
    p1 = args[0]
    p2 = args[1]
    if p2[0] > p1[1]:
        return False
    return True


def part1(ranges: list[str], ids: list[str]) -> int:
    print("here")
    int_ids = (int(id) for id in ids)
    range_boundaries = tuple([range(*get_range_boundaries(r)) for r in ranges])
    fresh = 0
    for id in int_ids:
        if any([id in r for r in range_boundaries]):
            fresh += 1
    return fresh


def part2(ranges: list[str]) -> int:
    result = 0
    range_list = []
    for _range in ranges:
        range_list.append(tuple(int(_) for _ in _range.split("-")))
    range_list.sort(key=lambda x: x[0])
    print(range_list)
    merged = [range_list[0]]
    print(merged)
    for i in range(1, len(range_list)):
        small, big = range_list[i]
        if small > merged[-1][1] + 1:
            merged.append(range_list[i])
        else:
            merged[-1] = tuple([merged[-1][0], max(merged[-1][1], big)])

    print(merged)
    for small, big in merged:
        result += (big - small) + 1

    return result

    # valid = merge_boundaries(ranges)
    # result = 0
    # print("*****")
    # for small, big in valid:
    #    result += (big - small) + 1
    # return result


if __name__ == "__main__":
    # Need to separate FRESH and SPOILED ingredients
    # Data consists of list of FRESH ID RANGES (inclusive),
    # a blank line
    # list of available ingredient IDs
    raw_data = get_input("input")
    ranges, ids = process_input(raw_data)
    ans1 = part1(ranges, ids)
    ans2 = part2(ranges)
    print(f"part 1: {ans1}")  # ~90ms
    print(f"part 2: {ans2}")
