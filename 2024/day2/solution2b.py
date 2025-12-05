def is_safe(report: list[int]) -> bool:
    global removed
    acceptable_range = [_ for _ in range(-3,4) if _ != 0]
    diffs = []
    if any([report.count(x) > 2 for x in report]):
        return False
    for i, num in enumerate(report[:-1]):
        cur = num
        next = report[i+1]
        difference = cur - next
        diffs.append(difference)
        if difference not in acceptable_range:
            return False
        if len(diffs) > 1:
            if diffs[-1] * diffs[-2] <= 0:
                return False
    return True

with open('input') as reports:
    list_of_reports = reports.readlines()[:-1]


count = 0

failed_first_pass = []
failed_twice = []

for reportsub in list_of_reports:
    levels = [int(l) for l in reportsub.split()]
    original = levels.copy()
    if is_safe(levels):
        safe = True
        count += 1
    else:
        failed_first_pass.append(levels)

for report in failed_first_pass:
    print(report)
    working_copy = report.copy()
    for i in range(len(report)):
        safe = False
        working_copy.pop(i)
        print("checking", working_copy)
        if is_safe(working_copy):
            count += 1
            safe = True
            break
        else:
            working_copy = report.copy()

print(count)



