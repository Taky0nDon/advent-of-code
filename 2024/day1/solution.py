with open("input") as input:
    list_of_pairs = list(filter(lambda x: len(x) > 1,
                           [line.split() for line in input.readlines()]
                           ))

diffs = []
first = sorted([int(p[0]) for p in list_of_pairs])
second = sorted([int(p[1]) for p in list_of_pairs])

sorted_pairs = zip(first,second)

for pair in sorted_pairs:
    diff = max(pair) - min(pair)
    diffs.append(diff)

print(sum(diffs))

sim_scores = []
for e in first:
    sim_scores.append(e*second.count(e))

print(sum(sim_scores))
