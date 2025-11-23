# Input list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Dictionary with odd numbers as keys and their cubes as values
odd_cube_dict = {n: n**3 for n in nums if n % 2 != 0}

print(odd_cube_dict)
