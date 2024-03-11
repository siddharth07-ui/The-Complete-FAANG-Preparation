"""
Function to delete an element in an array

Takes in an array and an element to delete

Returns an new Array
"""


def delete(arr, element):
    # Classical approach - Using for loop
    # if element not in arr:
    #     return "no such element exist in array"

    # new_arr = []

    # for index in range(len(arr)):
    #     if arr[index] != element:
    #         new_arr.append(arr[index])

    # return new_arr

    # Faster approach - Using list comprehension
    return [x for x in arr if x != element]


arr = [1, 2, 3, 5]
element = 4

print("Before deletion:", arr)
print("Deleting:", element)

new_arr = delete(arr, element)
print("After deletion:", new_arr)
