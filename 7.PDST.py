def Distance(DNA1,DNA2):
    diff = 0
    for i in range(len(DNA1)):
        if DNA1[i] != DNA2[i]:
            diff += 1
    return "%.5f" % round((diff/len(DNA1)), 5)

with open('C:/Users/gpdel/Desktop/pdst.txt', 'r') as file:
    content = file.read()
DNAs_number, lines, line_number, DNAs = content.count('>'), content.splitlines(), 0, []
for i in range(DNAs_number):
    DNA = ''
    line_number += 1
    while lines[line_number][0] != '>':
        DNA += lines[line_number]
        line_number += 1
        if line_number+1 > len(lines):
            break
    DNAs.append(DNA)
for i in range(len(DNAs)):
    line = ''
    for j in range(len(DNAs)):
        line += str(Distance(DNAs[i],DNAs[j]))+ ' '
    print(line)