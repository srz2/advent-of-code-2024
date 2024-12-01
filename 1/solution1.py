# Hold left and right values
left = []
right = []

# Read in values and convert to ints
with open('input.dat', 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        parts = line.split()
        left.append(int(parts[0]))
        right.append(int(parts[1]))

# sort lists
left.sort()
right.sort()

# find difs
diff = []
for index in range(0, len(left)):
    diff.append(abs(left[index] - right[index]))

# Calculate and display total
total = sum(diff)
print(total)