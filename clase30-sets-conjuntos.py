# manno de sets
s = set([1, 2, 3])
t = set([3, 4, 5])

print("\n union sets ")
unionSet = s.union(t)
print(unionSet)

print("\n intersection sets ")
interseccionSet = s.intersection(t)
print(interseccionSet)

print("\n diferencia sets ")
differenceSet = s.difference(t)
print(differenceSet)

print("\n existe elemento en sets ")
print(1 in s)
print(40 in s)
print(40 not in s)