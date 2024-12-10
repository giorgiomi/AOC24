import numpy as np

with open('input.txt', 'r') as f:
    data = f.readlines()
    res = 0
    for equation in data:
        value = int(equation.split(sep=':')[0])
        strings = equation.split(sep=':')[1].split()
        numbers = [int(str) for str in strings] 

        dim = 2**(len(numbers) - 1)
        for n in range(dim):
            binary = bin(n)
            operations = list(map(int, binary[2:].zfill(len(numbers) - 1)))
            #print(operations)
            check_sum = numbers[0]
            for i in range(len(numbers) - 1):
                if operations[i] == 0:
                    sum = check_sum + numbers[i+1]
                    check_sum = sum
                elif operations[i] == 1:
                    mul = check_sum * numbers[i+1]
                    check_sum = mul
                else:
                    print("ERROR")
                    exit()

            #print(check_sum)
            if check_sum == value:
                res += value
                break
        
    print(res)

