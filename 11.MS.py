input = open('C:/Users/gpdel/Desktop/ms.txt', 'r').read().strip().split('\n')
n = int(input[0])
num = list(map(int, input[1].split(' ')))

def merge(A,B):
    C = []
    while A and B:
        if A[0] < B[0]:
            C += [A.pop(0)]
        else:
            C += [B.pop(0)]
    C += A+B
    return C

def MS(num):
    if len(num) > 1:
        num = merge(MS(num[:len(num)//2]), MS(num[len(num)//2:]))
    return num
print(MS(num))
print(*MS(num))