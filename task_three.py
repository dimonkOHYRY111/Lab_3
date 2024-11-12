sentence = input("Введіть речення: ")

words = sentence.split()
longest_word = max(words, key=len)

if len(longest_word) > 10:
    print(f"найдовше слово має більше 10 символів: {longest_word}")
else:
    print(f"найдовше слово має 10 або менше символів: {longest_word}")