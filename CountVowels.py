def count_vow(str):
    vowels = 'aeiouAEIOU'
    count =0
    vow_list =[]
    for char in str:
        if char in vowels:
            count +=1
            vow_list.append(char)
    return count, vow_list
str = input("Enter string:")
vow_count, vow_found= count_vow(str)
print("number of vowels: ", vow_count)
print("Vowels found: ", vow_found)
