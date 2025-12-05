import re

def multiply_and_add(data: "str") -> int:
    digit_matches = re.findall(r"mul\(\d{0,3},\d{0,3}\)", data)
    result = 0
    for _ in digit_matches:
        first = _.split("(")[1].split(")")[0].split(",")[0]
        second = _.split("(")[1].split(")")[0].split(",")[1]
        result += int(first) * int(second)

    return result

with open("input") as file:
    data = file.read()


answer = multiply_and_add(data)
print(answer)

