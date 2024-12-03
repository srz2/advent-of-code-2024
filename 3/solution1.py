import re

def process_mul_op(str) -> int:
    pos_comma = str.find(',')
    first = int(str[4:pos_comma])
    second = int(str[pos_comma + 1:-1])
    return first * second

with open('data.dat', 'r') as f:
    memory = f.read()

results = re.findall('mul\\([0-9]{1,3},[0-9]{1,3}\\)', memory)
total = 0
for op in results:
    val = process_mul_op(op)
    total += val
print(total)