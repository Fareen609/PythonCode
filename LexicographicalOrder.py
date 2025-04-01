def rearrange_lexicographically(s):

    return ''.join(sorted(s))


input_string = "programming"
sorted_string = rearrange_lexicographically(input_string)
print("Original String:", input_string)
print("Sorted String:", sorted_string)
