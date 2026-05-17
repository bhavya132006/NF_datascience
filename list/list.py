Write a program to find the largest and smallest elements in a list.  
numbers = [12, 45, 7, 89, 23]
largest = max(numbers)
smallest = min(numbers)
print("Largest element:", largest)
print("Smallest element:", smallest)


Write a program to remove duplicate elements from a list.  
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("List after removing duplicates:", unique_numbers)


Write a program to reverse a list without using built-in reverse functions.  
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print("Reversed list:", reversed_list)


Write a program to count even and odd numbers in a list.  
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = len([x for x in numbers if x % 2 == 0])
odd = len([x for x in numbers if x % 2 != 0])
print("Even numbers:", even)
print("Odd numbers:", odd)

Write a program to merge two lists and sort the final list.  
list1 = [5, 2, 8]
list2 = [1, 9, 3]
merged_list = list1 + list2
merged_list.sort()
print("Sorted merged list:", merged_list)

Write a program to find the second largest element in a list. 
numbers = [12, 45, 7, 89, 23]
numbers.sort()
second_largest = numbers[-2]
print("Second largest element:", second_largest)


Write a program to check whether an element exists in a tuple.  
data = (10, 20, 30, 40, 50)
element = 30
print(element in data)

Write a program to count the occurrence of an element in a tuple.
data = (1, 2, 3, 2, 4, 2, 5)
element = 2
count = data.count(element)
print("Occurrence of", element, "is:", count)


Write a program to sort a list of tuples based on tuple values
students = [("John", 85), ("Alice", 92), ("Bob", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted list of tuples:")
print(sorted_students)


Write a program to convert a tuple into a list and a list into a tuple. 
my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)
print("Tuple converted to list:", my_list)
numbers = [5, 6, 7, 8]
new_tuple = tuple(numbers)
print("List converted to tuple:", new_tuple)
