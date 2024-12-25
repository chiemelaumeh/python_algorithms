# def split_string(s, is_valid):
#     def backtrack(start, path):
#         if start == len(s):
#             result.append(path[:])
#             return

#         for end in range(start + 1, len(s) + 1):
#             word = s[start:end]
#             if is_valid(word):
#                 path.append(word)
#                 backtrack(end, path)
#                 path.pop()

#     result = []
#     backtrack(0, [])
#     return result

# # Example usage:
# def is_valid(word):
#     # Example isValid function, you should replace it with your own implementation
#     valid_words = {'trees', 'are', 'good', 'cat', 'smell'}
#     return word in valid_words

# s1 = "treesaregood"
# s2 = "catsmell"

# print(split_string(s1, is_valid))  # Output: [['trees', 'are', 'good']]
# print(split_string(s2, is_valid))


