# function to perform linear search for element in array
def search(arr, element):
    # Classical approach - Using for loop to check index of element
    # for index in range(0, len(arr)):
    #     if arr[index] == element:
    #         return index
        
    # # if no such number exist in the array return -1
    # return -1

    # Efficient approach - Using list comprehension
    result = next((i for i, x in enumerate(arr) if x == element), -1)
    # Return the result of linear search
    return result


arr = [20, 5, 7, 25]
element = 7

print("Array Searched:", arr)
print("Searching for:", element)
result = search(arr, element)
if result == -1:
    print("Element not found")
else:
    print("Searched index =", result)
