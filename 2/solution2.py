safe_count = 0

with open('input.dat', 'r') as f:
    lines = f.read().splitlines()

def is_consistent_slope(reports):
    slope = None
    for i in range(1, len(reports)):
        diff = reports[i] - reports[i - 1]
        if not (1 <= abs(diff) <= 3):
            return False
        current_slope = 'increasing' if diff > 0 else 'decreasing'
        if slope is None:
            slope = current_slope
        elif slope != current_slope:
            return False
    return True

def check_with_removal(reports):
    for i in range(len(reports)):
        modified_reports = reports[:i] + reports[i + 1:]
        if is_consistent_slope(modified_reports):
            return True
    return False

def is_safe_report(reports):
    reports = [int(x) for x in reports]
    if is_consistent_slope(reports):
        return True
    return check_with_removal(reports)

for line in lines:
    reports = line.split(' ')
    if is_safe_report(reports):
        safe_count += 1
        print('safe')
    else:
        print('unsafe')

print(safe_count)
