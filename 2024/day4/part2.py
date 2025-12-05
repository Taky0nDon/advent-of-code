with open('input') as data:
    lines = list(filter(lambda x: x != '', [l.strip() for l in data.readlines()]))
    
xmases = 0
# Iterate from second line to second to last line.
# Check each char of each line, if it's A, proceed.
for i in range(1, len(lines)):
    for j in range(1, len(lines[i])):
        if lines[i][j] == "A":
# Check char up one line and back one char, and char down one line and over one char:
            try:
                up_back = lines[i-1][j-1]
                down_over = lines[i+1][j+1]
                up_over = lines[i-1][j+1]
                down_back = lines[i+1][j-1]
            except IndexError:
                continue
            else:
                if {up_back, down_over} == set("MS") and {up_over, down_back} == set("MS"):
                    xmases += 1

print(xmases)

    # If they are "MS", proceed
# Check char up one line and over one char, and char down one line and back one char:
    # If they are "MS", proceed
# Increment counter
# Print Counter
