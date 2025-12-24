import operator

from p1 import solve_problem, get_function

def get_input(data) -> list[str]:
    with open(data) as f:
        lines = f.readlines()[:-1]
    return [l.strip("\n") for l in lines]

def part2(values: list[list[str]]):
    final_result = 0
    *v, opr = values
    cols = extract_columns(v)
    for c, opr in zip(cols, opr.split()):
        op = get_function(opr)
        match op:
            case operator.add:
                result = 0
            case operator.mul:
                result = 1
        for num in c:
            if num == "":
                continue
            result = op(result, int(num))
        final_result += result
    return final_result

def extract_columns(values: list[str]) -> list[str]:
    final_result = 0
    rtl_nums = []
    columnar_nums = []
    start = 0
    end = 0
    trans_table = str.maketrans({" ": "0"})

    for c in range(NUM_COLS):
        col = []
        current_line = ""
        end += COL_LENGTHS[c] + 1
        for row in values:
            col.append(row[start:end])
        start = end
        rtl_nums.append([c.translate(trans_table) for c in col])

    for num_list in rtl_nums:
        num_digits = len(num_list[0])
        final_nums = []
        for i in range(num_digits):
            final_num = []
            for num in num_list:
                final_num.append(num[i])
            if final_num.count("0") != len(final_num):
                final_nums.append("".join(final_num).strip("0"))
        columnar_nums.append(final_nums)

    return columnar_nums

def get_column_lengths(operator_col: list[str]) -> list[int]:
    col_length = 0
    result = []
    for ch in operator_col:
        if ch == " ":
            col_length += 1
        elif col_length > 0:
            result.append(col_length)
            col_length = 0
# Add one to because there is no delimiting space which was counted in the
# previous cols
    result.append(col_length + 1)
    return result


PUZZLE = "input"
if __name__ == "__main__":
    print('hi')
    ANSWER = 9348430857627
    data = get_input(PUZZLE)
    COL_LENGTHS = get_column_lengths(data[-1])
    NUM_COLS = len(COL_LENGTHS)
    ans = part2(data)
    if ans == ANSWER:
        print("THAT IS RIGHT!")

# Each number is given in its own column, with the most significant digit
#The rightmost problem is 4 + 431 + 623 = 1058

#check if index < current_length?
#if it is, do nothing
#if it's not concat digit
#when done, cast to int
