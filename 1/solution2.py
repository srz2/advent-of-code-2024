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

total_distance = 0

b_occurrences = {}
for b in left:
    count = b_occurrences.get(b, 0)
    b_occurrences[b] = count + 1

for a in right:
    total_distance += b_occurrences.get(a, 0) * a

print(total_distance)