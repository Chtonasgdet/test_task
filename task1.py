number = list(map(int, input().split()))
number.sort()
new_number = int(''.join(map(str, number))) + 1
print(list(map(int, str(new_number))))


    
