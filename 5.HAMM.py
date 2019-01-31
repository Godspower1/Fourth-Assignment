s='GAGCCTACTAACGGGAT'
t='CATCGTAATGACGGCCT'
hamm=0
for i in range(len(s)):
    if s[i]!=t[i]:
        hamm+=1
print(hamm)