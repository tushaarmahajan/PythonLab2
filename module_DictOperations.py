def merging_Dict(*args):
    """Merge multiple dictionaries into one."""
    merged_dict = {}
    for dictionary in args:
        merged_dict.update(dictionary)
    return merged_dict

def common_keys(*args):
    """Find common keys in multiple dictionaries."""
    if not args:
        return set()
    common_keys_set = set(args[0].keys())
    for dictionary in args[1:]:
        common_keys_set &= set(dictionary.keys())
    return common_keys_set

def invert_dict(d):
    """Invert a dictionary, swapping keys and values. If multiple keys have the same value, group these keys in a list."""
    inverted_dict = {}
    for key, value in d.items():
        if value not in inverted_dict:
            inverted_dict[value] = []
        inverted_dict[value].append(key)
    return inverted_dict

def common_key_value_pairs(*args):
    """Find common key-value pairs across multiple dictionaries."""
    if not args:
        return {}
    common_pairs = args[0].items()
    for dictionary in args[1:]:
        common_pairs = common_pairs & dictionary.items()
    return dict(common_pairs)
