n =6
m =3
Wabbit = [1, 1]
months = 2
while months < n:
    if months < m:
        Wabbit.append(Wabbit[-2] + Wabbit[-1])
    elif months == m :
        Wabbit.append(Wabbit[-2] + Wabbit[-1] - 1)
    else:
        Wabbit.append(Wabbit[-2] + Wabbit[-1] - Wabbit[-(m + 1)])
    months += 1
print(Wabbit[-1])                               