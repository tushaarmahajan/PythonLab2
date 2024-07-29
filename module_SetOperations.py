def add_element(s, element):
    """Add an element to a set, ensuring no errors if the element is already present."""
    s.add(element)

def remove_element(s, element):
    """Remove an element from a set, ensuring no errors if the element is not present."""
    s.discard(element)

def union_intersection(s1, s2):
    """Return the union and intersection of two sets, handling empty sets correctly."""
    union = s1 | s2
    intersection = s1 & s2
    return union, intersection

def difference(s1, s2):
    """Return the difference S1−S2, handling empty sets correctly."""
    return s1 - s2

def is_subset(s1, s2):
    """Check if set S1 is a subset of set S2, handling empty sets correctly."""
    return s1 <= s2

def set_length(s):
    """Find the length of a set without using the len() function."""
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    """Compute the symmetric difference of two sets."""
    return s1 ^ s2

def power_set(s):
    """Compute the power set of a given set."""
    from itertools import chain, combinations
    s_list = list(s)
    return set(frozenset(comb) for comb in chain.from_iterable(combinations(s_list, r) for r in range(len(s_list)+1)))

def unique_subsets(s):
    """Get all unique subsets of a given set."""
    from itertools import combinations
    s_list = list(s)
    unique_subsets_set = set()
    for r in range(len(s_list) + 1):
        for comb in combinations(s_list, r):
            unique_subsets_set.add(frozenset(comb))
    return unique_subsets_set
