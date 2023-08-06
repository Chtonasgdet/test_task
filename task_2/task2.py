from typing import List

def reverse_string(s: List[str]) -> List[str]:
    if len(s) > 1:
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return s

s = list(input())
print(s)
print(reverse_string(s))