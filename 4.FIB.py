parents = 0
offspring = 1
count = 1
freshparent = 0
n = 5
k = 3
while (count < n):
    freshparent = parents + offspring
    offspring = parents * k
    parents = freshparent
    count = count + 1
print(parents + offspring)