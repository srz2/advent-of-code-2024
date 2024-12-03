safe_count = 0
with open('input-test.dat', 'r') as f:
    lines = f.read().splitlines()

for line in lines:
    reports = line.split(' ')
    
    # analize tests
    first = True
    last = 0
    safe = True
    slope = 'unknown'
    for x in reports:
        val = int(x)
        if first:
            last = val
            first = False
            continue
        dif = val - last

        if dif > 0:
            if slope == 'decreasing':
                safe = False
                break
            slope = 'increasing'
        else:
            if slope == 'increasing':
                safe = False
                break
            slope = 'decreasing'

        dif_abs = abs(dif)
        if (dif == 0 or dif_abs > 3):
            safe = False
            break
        last = val
    if safe:
        safe_count += 1
        print('safe')
    else:
        print('unsafe')

print(safe_count)
