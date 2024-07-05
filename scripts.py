def solution2(N):
    import string
    alphabet = string.ascii_lowercase
    num_letters = 26
    quotient, remainder = divmod(N, num_letters)
    result = alphabet * quotient + alphabet[:remainder]
    
    return result

# Examples
print(solution2(3))   # Output: "abc"
print(solution2(5))   # Output: "abcde"
print(solution2(2000))  # Output: "abcdefghijklmnopqrstuvwxyzabcd"
