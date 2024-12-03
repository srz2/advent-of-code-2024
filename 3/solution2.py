import re

REGEX_DO = 'do\\(\\)'
REGEX_DONOT = "don't\\(\\)"
REGEX_MEMORY = 'mul\\([0-9]{1,3},[0-9]{1,3}\\)'

with open('3/data2.dat', 'r') as f:
    memory = f.read()

def process_mul_op(str) -> int:
    pos_comma = str.find(',')
    first = int(str[4:pos_comma])
    second = int(str[pos_comma + 1:-1])
    return first * second

def op_is_active(op):
    pass


# Assume ops are active
op_active = True

# Process
index = 0
total = 0
while True:
    if not op_active:
        next_enable = re.search(REGEX_DO, memory)
        if next_enable == None:
            break
        
        # Move index to next available
        index = next_enable.end()
        memory = memory[index:]
        index = 0
        
    next_disable = re.search(REGEX_DONOT, memory)
    active_memory = ''
    if next_disable == None:
        active_memory = memory[index:]
    else:
        active_memory = memory[index:next_disable.start()]

    ops = re.findall(REGEX_MEMORY, active_memory)
    for op in ops:
        total += process_mul_op(op)
    op_active = False

    # Move index and process string
    if next_disable == None:
        break
    index += next_disable.end()    
    memory = memory[index:]

print(total)