sum = 0
array  = []

for i in range(10):
    number = int(input())
    array.append(number)
    sum += number

def func(arr):
    flag = True
    for x in range(9):
        if array[x]  >  array[x+1]:
            return False
            break
        else:
             flag = True
    return flag






print(sum)
print(func(array))
