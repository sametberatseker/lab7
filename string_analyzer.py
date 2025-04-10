from string_package import reverse_string, capitalize_words, remove_punctuation, count_characters, count_words, \
    average_word_length

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    reversed_sentence = reverse_string(sentence)
    capitalized_sentence = capitalize_words(sentence)
    no_punctuation_sentence = remove_punctuation(sentence)
    char_count = count_characters(no_punctuation_sentence)
    word_count = count_words(no_punctuation_sentence)
    avg_word_length = average_word_length(no_punctuation_sentence)

    print(f"Reversed: {reversed_sentence}")
    print(f"Capitalized: {capitalized_sentence}")
    print(f"Without punctuation: {no_punctuation_sentence}")
    print(f"Character count (no punctuation): {char_count}")
    print(f"Word count: {word_count}")
    print(f"Average word length: {avg_word_length:.2f}")
