with open('input') as reports:
    list_of_reports = reports.readlines()[:1000]

class ReportInspector:
    last_inspected_element = "d"
    removed = 0

def check_ascending_or_descending(report: list[int]) -> bool:
    item_pairs = [(report[n], report[n+1]) for n in range(len(report)-1)]
    # item_pairs[x][0||1] xth or x + 1th element
    num_asc_pairs = [p[0] < p[1] for p in item_pairs].count(True)
    num_dec_pairs = [p[0] > p[1] for p in item_pairs].count(True)
    if all([p[0] > p[1] for p in item_pairs]) or all([p[0] < p[1] for p in item_pairs]):
        return True
    if num_asc_pairs > 1 and num_dec_pairs > 1:
        return False
    if num_asc_pairs > num_dec_pairs:
        char = "asc"
    else:
        char = "dec"
    if char == "asc":
        # if the list is primarily ascending, we need to remove the first p[1]
        # for which p[0] > p[1]
        for p in item_pairs:
            if p[0] > p[1]:
                report.remove(p[1])
                check_ascending_or_descending(report)
    else:
        for p in item_pairs:
            if p[0] < p[1]:
                report.remove(p[1])
                check_ascending_or_descending(report)

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
            ReportInspector.last_inspected_element = report[i+1]
            report.remove(ReportInspector.last_inspected_element)
            return False
    return safe

def check_safe(report):
    return  check_proximity(report) and check_ascending_or_descending(report)
count = 0

for report in list_of_reports:
    print(report)
    ReportInspector.removed = 0
    int_report = generate_list_of_ints(report)
    original = int_report.copy()
    if check_safe(int_report):
        safe = True
        print(original, file=open("safe", "a"))
        count += 1
    else:
        print(ReportInspector.last_inspected_element)
        if check_safe(int_report):
            print(original, file=open("safe", "a"))
            count += 1
            
        # I need to check only removing elements that would cause report to be
        # unsafe, not every element.
        # When an element causes the checks to fail, remove that element and try again.

print(count)


