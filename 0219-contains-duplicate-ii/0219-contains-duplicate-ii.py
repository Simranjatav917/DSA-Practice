class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
      
        seen = {}  # A hash map to store numbers and their indices
        
        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i
            
        return False

#   fruits = ['apple', 'banana', 'cherry']

# # Using enumerate() to get both index and value
# for index, fruit in enumerate(fruits):
#     print(f"Index: {index}, Fruit: {fruit}")

# Output:
# Index: 0, Fruit: apple
# Index: 1, Fruit: banana
# Index: 2, Fruit: cherry

# fruits = ['apple', 'banana', 'cherry']
# index = 0

# for fruit in fruits:
#     print(f"Index: {index}, Fruit: {fruit}")
#     index += 1