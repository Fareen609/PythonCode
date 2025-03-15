def get_dict_input(prompt):
    print(prompt)
    dictionary = {}
    num_items = int(input("Enter the number of items you want to add to the dictionary: "))
    
    for _ in range(num_items):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        dictionary[key] = value
    
    return dictionary
dict1 = get_dict_input("Enter first dictionary")
dict2 = get_dict_input("Enter second dictionary")
merged_dict = {**dict1, **dict2}
print("\nMerged Dictionary:", merged_dict)
