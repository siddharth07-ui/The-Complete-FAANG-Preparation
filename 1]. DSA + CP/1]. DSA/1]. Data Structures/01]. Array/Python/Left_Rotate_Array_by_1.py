"""
Function to rotate the array
"""


# def left_rotate(arr, num):
#     tmp = arr[0]

#     for index in range(1, num):
#         arr[index - 1] = arr[index]

#     arr[num - 1] = tmp

# arr = [1, 2, 3, 4, 5]
# num = 4

# print("Before Left Rotation:", arr)

# left_rotate(arr, num)
# print("After '1' Left Rotation:", arr)


def left_rotate_by_1(arr, index):
    tmp = arr.pop(0)
    arr = arr[:index - 1] + [tmp] + arr[index - 1:]
    return arr

arr = [1, 2, 3, 4, 5]
num = 4

print("Before Left Rotation:", arr)

new_arr = left_rotate_by_1(arr, num)
print("After '1' Left Rotation:", new_arr)
