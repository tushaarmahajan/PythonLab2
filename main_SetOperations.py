import module_SetOperations as so

# Demonstrate add_element and remove_element
s = {1, 2, 3}
print("Original set:", s)
so.add_element(s, 4)
print("After adding 4:", s)
so.add_element(s, 2)
print("After adding 2 again:", s)
so.remove_element(s, 2)
print("After removing 2:", s)
so.remove_element(s, 5)
print("After trying to remove 5:", s)

# Demonstrate union_intersection
s1 = {1, 2, 3}
s2 = {3, 4, 5}
union, intersection = so.union_intersection(s1, s2)
print("\nSet 1:", s1)
print("Set 2:", s2)
print("Union:", union)
print("Intersection:", intersection)

# Demonstrate difference
print("\nDifference S1 - S2:", so.difference(s1, s2))

# Demonstrate is_subset
s3 = {1, 2}
print("\nSet 3:", s3)
print("Is Set 3 a subset of Set 1?", so.is_subset(s3, s1))

# Demonstrate set_length
print("\nLength of Set 1:", so.set_length(s1))

# Demonstrate symmetric_difference
print("\nSymmetric difference of Set 1 and Set 2:", so.symmetric_difference(s1, s2))

# Demonstrate power_set
print("\nPower set of Set 1:")
for subset in so.power_set(s1):
    print(subset)

# Demonstrate unique_subsets
print("\nUnique subsets of Set 1:")
for subset in so.unique_subsets(s1):
    print(subset)
