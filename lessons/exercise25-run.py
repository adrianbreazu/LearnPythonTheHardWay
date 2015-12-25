import exercise25

sentence = "All good things come to those who wait."
words = exercise25.break_words(sentence)
print(words)
sorted_words = exercise25.sort_words(words)
print(sorted_words)
exercise25.print_first_word(words)
exercise25.print_last_word(words)
print(words)
exercise25.print_first_word(sorted_words)
exercise25.print_last_word(sorted_words)
print(sorted_words)
sorted_words = exercise25.sort_sentence(sentence)
print(sorted_words)
exercise25.print_first_and_last(sentence)
exercise25.print_first_and_last_sorted(sentence)