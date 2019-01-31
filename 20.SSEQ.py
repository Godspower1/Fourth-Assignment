sseq = []
seq = ''
with open('C:/Users/gpdel/Desktop/sseq.txt', 'r') as infile:
    for line in infile:
        if line[0] == '>':
            if seq != '':
                sseq.append(seq)
                seq = ''
            continue
        else:
            seq = seq + line.strip()
    sseq.append(seq)

print(sseq)
g = sseq[0]
d = sseq[1]
print(g)
print(d)
a=[]
i = j = 0
while i < len(g) and j < len(d):
    if g[i] == d[j]:
        a.append(i + 1)
        j += 1
    i += 1
print(' '.join(map(str, a)))