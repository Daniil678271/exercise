def generate_anagrams(word: str) -> list[str]:
    if len(word) <=1:
        return[word]
    anagrams = []
    for i in range(len(word)):
        current_char = word[i]
        remaining_chars = word[:i] + word[i+1:]
        sub_anagrams = generate_anagrams(remaining_chars)
        for sub in sub_anagrams:
            anagrams.append(current_char + sub)
    return anagrams
if __name__ == "__main__":
    word = input("Введите слово:")
    result = generate_anagrams(word)
    print(f"Анаграммы слова '{word}': {result}")
    print(f"Количество анаграмм: {len(result)}")
    