#Write a program to create a dictionary from two lists: one of keys and one of values.
keys = ['name', 'age', 'city']
values = ['John', 25, 'New York']
dictionary = dict(zip(keys, values))
print("Dictionary:", dictionary)


#Merge two dictionaries into one.
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = dict1 | dict2
print("Merged Dictionary:", merged_dict)

#Write a program to sort a dictionary by its values. 
my_dict = {'apple': 50, 'banana': 20, 'orange': 40}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted Dictionary:", sorted_dict)


#Given two sets, check if one set is a subset of another. 
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")


#Write a program to check whether two lists have at least one common element using sets. 
list1 = [1, 2, 3, 4]
list2 = [3, 5, 7, 9]
common = set(list1) & set(list2)
if common:
    print("Common element(s):", common)
else:
    print("No common elements")

