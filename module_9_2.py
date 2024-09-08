first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(a) for a in first_strings if len(a) >= 5]

second_result = []
for word in first_strings:
    for word1 in second_strings:
        if len(word) == len(word1):
            second_result.append((word, word1))

third_result = {}
for s in first_strings + second_strings:
    if len(s) % 2 == 0:
        third_result[s] = len(s)

print(first_result)
print(second_result)
print(third_result)