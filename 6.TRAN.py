seq_list=[]
seq=''
with open("C:/Users/gpdel/Desktop/Rosalintran.txt") as infile:
    for line in infile:
        if line[0] == '>':
            if seq != '':
                seq_list.append(seq)
                seq = ''
            continue
        else:
            seq = seq + line.strip()
    seq_list.append(seq)



s1=seq_list[0]
s2=seq_list[1]

transversion=0
transition=0
for i in range(len(s1)):
    if s1[i]!= s2[i]:
        if s1[i]=='A' and (s2[i] == "C" or s2[i] == "T"):
            transversion += 1
        elif s1[i]=='C' and (s2[i] == "A" or s2[i] == "G"):
            transversion += 1
        elif s1[i]=='G' and (s2[i] == "C" or s2[i] == "T"):
            transversion += 1
        elif s1[i]=='T' and (s2[i] == "A" or s2[i] == "G"):
            transversion += 1
        else:
            transition += 1


print(transition/transversion)