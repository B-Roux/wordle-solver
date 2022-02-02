def print_wordle_matches (word_builder, in_word, not_in_word):
    with open('wordle_words.txt', 'r') as dictionary:
        for word in dictionary:
            word = word.strip('\n')
            if    any([char not in word for char in in_word]): continue
            elif  any([char in word for char in not_in_word]): continue
            elif  any([pair[0] != '_' and pair[0] != pair[1] for pair in zip(word_builder, word)]): continue
            else: print(word.upper())

if __name__ == '__main__':
    print_wordle_matches ('_____', '', '')
