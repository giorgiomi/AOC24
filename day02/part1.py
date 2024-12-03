def isSafe(report):
    incr_old = report[1] - report[0]
    for i in range(len(report) - 1):
        incr_new = report[i+1] - report[i]
        if incr_new == 0 or incr_new < -3 or incr_new > 3:
            return False
        if incr_new * incr_old < 0:
            return False
        incr_old = incr_new
    return True
        
count = 0
with open("input.txt") as f:
    reports = f.readlines()
    for report in reports:
        report_list = [int(el) for el in report.split()]
        #print(levels)
        if isSafe(report_list):
            count += 1
print(count)