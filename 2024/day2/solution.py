with open('input') as reports:
    list_of_reports = reports.readlines()[:1000]

class Remover:
    removed = 0

def check_ascending_or_descending(report: list[int]) -> bool:
    return report == sorted(report) or report == sorted(report, reverse=True)


def generate_list_of_ints(inp: str) -> list[int]:
    return [int(e) for e in inp.split()]

def check_proximity(report: list[int]) -> bool:
    safe = False
    for i, e in enumerate(report):
        if i == len(report) - 1:
            continue
        elif e - report[i+1] in [-3,-2,-1,1,2,3]:
            safe = True
        else:
            return False
    return safe

count = 0

for report in list_of_reports:
    print(report)
    Remover.removed = 0
    print(report)
    unsafe = 0
    safe = True
    int_report = generate_list_of_ints(report)
    if not check_ascending_or_descending(int_report):
        continue
    if check_proximity(int_report):
        count += 1

print(count)


