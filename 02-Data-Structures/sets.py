set1 = { 1,2,3,4,5,6}
set2 = {7,8,9,10,1,2,3}
print(set1.union(set2))
print(set1, set2)
print(set1.intersection(set2))
set1.discard(3)
print(set1)
set1.add(3)
print(set1)