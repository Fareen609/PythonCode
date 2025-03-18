def get_user_input():
    user_input = input("Enter a dictionary (in format {key1: value1, key2: value2, ...}): ")
    try:
        return eval(user_input)
    except:
        print("Invalid dictionary format. Please enter a valid dictionary.")
        return get_user_input()
def merge_dictionaries(dict1, dict2, dict3):
    merged_dict = {**dict1, **dict2, **dict3}
    return merged_dict

def main():
    print("Enter the first dictionary:")
    dict1 = get_user_input()
    
    print("Enter the second dictionary:")
    dict2 = get_user_input()

    print("Enter the third dictionary:")
    dict3 = get_user_input()

    merged = merge_dictionaries(dict1, dict2, dict3)
    print("Merged Dictionary:", merged)
main()
