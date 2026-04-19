# nested_list = [[4,7,1],
#                [9,12,6],
#                [3,8,5]]

# output = [4,9,5]

# result = []

# for list in nested_list:
#     largest = list[0]
#     second_largest = None
#     for i in list:
#         if i>largest:
#             second_largest = largest
#             largest = i
#         elif second_largest is None or i > second_largest:
#             if i != largest:
#                 second_largest = i
#     result.append(second_largest)

# print(result)

nested_list = [[4,7,1],
               [9,12,6],
               [3,8,5]]
result = []

for list in nested_list:
    largest = list[0]
    second_largest = float("-inf")
    for i in list:
        if i>largest:
            second_largest = largest
            largest = i
        elif i > second_largest or second_largest is None:
            if i != largest:
                second_largest = i
    result.append(second_largest)

print(result)