import operator

def get_input(data: str) -> list[str]:
    with open(data) as f:
        content = f.read()
    lines = content.split("\n")
    lines = [l.split(" ") for l in lines if l != ""]
    for i_l, line in enumerate(lines):
        for i, v in enumerate(line):
            if i - 1 >= 0 and i - 1 < len(line):
                if line[i-1] == "":
                    line[i] = f" {v}"
        lines[i_l] = [_ for _ in line if _ not in ("", " ")]
    return lines



# only supports add or multiply operations
def solve_problem(op: function, *vals):
    return op(*vals)

def get_function(str_op: str) -> function:
    fn = None
    match str_op:
        case "+":
            result = 0
            fn = operator.add
        case "*":
            result = 1
            fn = operator.mul
    return fn

def part1(values: list[list[str]]) -> None:
    num_columns = len(values[0])
    final_result = 0
    for col in range(num_columns):
        op = values[-1][col]
        fn = get_function(values[-1][col])
        match fn:
            case operator.add:
                result = 0
            case operator.mul:
                result = 1
        for row in values[:-1]:
            result = solve_problem(fn, result, int(row[col]))
        final_result += result
    print(final_result)

PUZZLE = "sample"
if __name__ == "__main__":
    raw_data = get_input(PUZZLE)
    part1(raw_data)
