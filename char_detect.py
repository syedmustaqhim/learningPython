from pprint import pprint
sentence = str(input(
    "Enter a sentence for to count the number of letters in it: "))
char_frequency = {}

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
# pprint(" The letters appearing according to their order of frequency with highest frequency: {}".format(
# sorted(char_frequency.items())), width=1)
# pprint(char_frequency, width=1)
print("letter: {}, number : {}".format(
    char_frequency_sorted[0][0], char_frequency_sorted[0][1]))
