import module_ListFunction as lf

# Create lists using Python comprehension
list_1 = [x for x in range(10)]             # A list of numbers from 0 to 9
list_2 = [x**2 for x in range(10)]          # A list of squares of numbers from 0 to 9
list_3 = [x for x in range(10) if x % 2 == 0]  # A list of even numbers from 0 to 9
list_4 = [x for x in range(20) if x % 3 == 0]  # A list of numbers divisible by 3 from 0 to 19
list_5 = [x for x in range(-5, 6)]          # A list of numbers from -5 to 5

# Demonstrate the execution of each function
print("List 1:", list_1)
print("Max of List 1:", lf.find_max(list_1))
print("Min of List 1:", lf.find_min(list_1))
print("Sum of List 1:", lf.calculate_sum(list_1))
print("Average of List 1:", lf.compute_average(list_1))
print("Median of List 1:", lf.determine_median(list_1))

print("\nList 2:", list_2)
print("Max of List 2:", lf.find_max(list_2))
print("Min of List 2:", lf.find_min(list_2))
print("Sum of List 2:", lf.calculate_sum(list_2))
print("Average of List 2:", lf.compute_average(list_2))
print("Median of List 2:", lf.determine_median(list_2))

print("\nList 3:", list_3)
print("Max of List 3:", lf.find_max(list_3))
print("Min of List 3:", lf.find_min(list_3))
print("Sum of List 3:", lf.calculate_sum(list_3))
print("Average of List 3:", lf.compute_average(list_3))
print("Median of List 3:", lf.determine_median(list_3))

print("\nList 4:", list_4)
print("Max of List 4:", lf.find_max(list_4))
print("Min of List 4:", lf.find_min(list_4))
print("Sum of List 4:", lf.calculate_sum(list_4))
print("Average of List 4:", lf.compute_average(list_4))
print("Median of List 4:", lf.determine_median(list_4))

print("\nList 5:", list_5)
print("Max of List 5:", lf.find_max(list_5))
print("Min of List 5:", lf.find_min(list_5))
print("Sum of List 5:", lf.calculate_sum(list_5))
print("Average of List 5:", lf.compute_average(list_5))
print("Median of List 5:", lf.determine_median(list_5))
