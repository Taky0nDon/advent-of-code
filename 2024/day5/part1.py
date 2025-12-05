with open('input') as data:
    parts = data.read().rstrip().split("\n\n")
    ordering_rules = parts[0].split("\n")
    updates = parts[1].split("\n")

correct_updates = []
middle_updates = []

def find_relevant_rules(pg_num: str, rules: list[str]) -> list[str] | None:
    for rule in rules:
        return list(filter(lambda x: x.split("|")[0] == pg_num, rules))

def interpret_rule(rule: str) -> list[str]:
    return rule.split("|")

def interpret_update(update: str) -> list[str]:
    return update.split(",")

def find_middle_update_index(update: list[str]) -> int:
    num_of_elements = len(update)
    return num_of_elements // 2

for update in updates:
    is_correct = True
    for i, page in enumerate(interpret_update(update)):
       rules_to_check = find_relevant_rules(page, ordering_rules) 
       for rule in rules_to_check:
           if rule.split("|")[1] in interpret_update(update)[:i]:
               is_correct = False
    if is_correct:
        correct_updates.append(update)

for update in correct_updates:
    split_update = update.split(",")
    middle_updates.append(int(split_update[find_middle_update_index(split_update)]))
print(sum(middle_updates))
