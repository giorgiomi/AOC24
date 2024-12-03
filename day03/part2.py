import re
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

with open('input.txt', 'r') as f:
    data = f.read()
    sum = 0
    x = re.findall(pattern, data)
    flag = True
    for el in x:
        if el == 'do()':
            flag = True
        elif el == "don't()":
            flag = False
        elif flag:
            num1 = int(el.split('(')[1].split(',')[0])
            num2 = int(el.split('(')[1].split(',')[1].split(')')[0])
            sum += num1 * num2

    print(sum)
