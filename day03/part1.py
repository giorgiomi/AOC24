import re

pattern = r'mul\(\d{1,3},\d{1,3}\)'

with open('input.txt', 'r') as f:
    data = f.read()
    sum = 0
    x = re.findall(pattern, data)
    for el in x:
        num1 = int(el.split('(')[1].split(',')[0])
        num2 = int(el.split('(')[1].split(',')[1].split(')')[0])
        sum += num1 * num2

    print(sum)
