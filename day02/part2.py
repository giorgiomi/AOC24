from part1 import isSafe

def isSafeDamp(report):
    if isSafe(report):
        return True
    else:
        for i in range(len(report)):
            report_damp = report[0:i] + report[i+1:]
            if isSafe(report_damp):
                return True
            else:
                if i == len(report) - 1:
                    return False
                else:
                    continue
        
count = 0
with open("input.txt") as f:
    reports = f.readlines()
    for i,report in enumerate(reports):
        print(i)
        report_list = [int(el) for el in report.split()]
        #print(levels)
        if isSafeDamp(report_list):
            count += 1
print(count)