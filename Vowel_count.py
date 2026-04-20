def count_vowels(array):
    count = 0
    vowels = "aeiouAEIOU"

    for char in array:
        if char in vowels:
            count += 1

    return count

text = "Hello World"
print(count_vowels(text))