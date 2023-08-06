from itertools import permutations

numbers = list(map(int, input().split()))
new_numbers = set(list(permutations(numbers)))
print(list(map(list, new_numbers)))