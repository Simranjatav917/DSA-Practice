class Solution(object):
        def minimumOperations(self, A):
            return len(set(A) - {0})
        
        
# import numpy as np

# original_array = np.array([10, 20, 30, 40])
# number_to_subtract = 5
# result_array = np.subtract(original_array, number_to_subtract)
# print(result_array)

# import numpy as np

# original_array = np.array([10, 20, 30, 40])
# number_to_subtract = 5
# result_array = original_array - number_to_subtract
# print(result_array)
        

# original_list = [10, 20, 30, 40]
# number_to_subtract = 5
# result_list = []
# for x in original_list:
#     result_list.append(x - number_to_subtract)
# print(result_list)

# original_list = [10, 20, 30, 40]
# number_to_subtract = 5
# result_list = [x - number_to_subtract for x in original_list]
# print(result_list)

my_array = [10, 5, 20, 2, 15]

# if not my_array:  # Handle empty array case
#     minimum_element = None
# else:
#     minimum_element = my_array[0]  # Initialize with the first element
#     for element in my_array:
#         if element < minimum_element:
#             minimum_element = element

# print(f"The minimum element is: {minimum_element}")