import module_DictOperations as do

# Demonstrate merging_Dict
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
dict3 = {'c': 5, 'd': 6, 'e': 7}

merged = do.merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)

# Demonstrate common_keys
common_keys = do.common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys)

# Demonstrate invert_dict
inverted_dict1 = do.invert_dict(dict1)
inverted_dict2 = do.invert_dict(merged)
print("\nInverted Dictionary 1:", inverted_dict1)
print("Inverted Merged Dictionary:", inverted_dict2)

# Demonstrate common_key_value_pairs
common_pairs = do.common_key_value_pairs(dict1, dict2, dict3)
print("\nCommon Key-Value Pairs:", common_pairs)
