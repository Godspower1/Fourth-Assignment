def Bin_search(Array, ray):
    low = 0
    high = len(Array)-1
    while low <= high:
        index = (low + high) // 2
        if ray == Array[index]:
            return index + 1
        elif ray > Array[index]:
            low = index + 1
        else:
            high = index - 1
    return -1

with open('C:/Users/gpdel/Desktop/bins.txt', 'r') as file:
    content = file.read().splitlines()

array = [int(i) for i in content[2].split()]
ray = [int(i) for i in content[3].split()]
line = ''

for i in range(len(ray)):
    line += str(Bin_search(array, ray[i])) + ' '

print(line)