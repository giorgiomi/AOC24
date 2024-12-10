import numpy as np

with open('input.txt', 'r') as f:
    data = f.readlines()
    res = 0
    for equation in data:
        value = int(equation.split(sep=':')[0])
        strings = equation.split(sep=':')[1].split()
        numbers = [int(str) for str in strings] 

        dim = 3**(len(numbers) - 1)
        for n in range(dim):
            ternary = np.base_repr(n, base=3)
            operations = list(map(int, ternary.zfill(len(numbers) - 1)))
            #print(operations)
            check_sum = numbers[0]
            for i in range(len(numbers) - 1):
                if operations[i] == 0:
                    sum = check_sum + numbers[i+1]
                    check_sum = sum
                elif operations[i] == 1:
                    mul = check_sum * numbers[i+1]
                    check_sum = mul
                elif operations[i] == 2:
                    conc = int(str(check_sum) + str(numbers[i+1]))
                    check_sum = conc
                else:
                    print("ERROR")
                    exit()

            #print(check_sum)
            if check_sum == value:
                res += value
                break
        
    print(res)

