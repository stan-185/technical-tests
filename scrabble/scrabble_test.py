from random import shuffle

LETTER_SCORES =  {'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'N' : 1,'R' : 1, 'T' : 1, 'L' : 1, 'S' : 1, 'U' : 1, 'D' : 2, 'G' : 2, 'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3, 'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4, 'K': 5, 'J': 8, 'X':8, 'Q':10,'Z':10}

LETTER_DISTRIBUTIONS =  {'A' : 9, 'E' : 12, 'I' : 9, 'O' : 8, 'N' : 6,'R' : 6, 'T' : 6, 'L' : 4, 'S' : 4, 'U' : 4, 'D' : 4, 'G' : 3, 'B' : 2, 'C' : 2, 'M' : 2, 'P' : 2, 'F' : 2, 'H' : 2, 'V' : 2, 'W' : 2, 'Y' : 2, 'K': 1, 'J': 1, 'X':1, 'Q':1,'Z':1}

ALPHABET = list(LETTER_SCORES.keys())

def calculate_word_score(word):
    sum = 0
    for letter in word:
        upper_case_letter = letter.upper()
        sum += LETTER_SCORES[upper_case_letter]

    return sum


def assign_tiles(rack):
    shuffle(ALPHABET)
    rack.extend(ALPHABET[:7])

def create_shuffled_bag():
    bag =[]
    for letter in ALPHABET:
        for i in range(LETTER_DISTRIBUTIONS[letter]):
            bag.append(letter)
    shuffle(bag)
    return bag

def load_dictionary():
    data = open('dictionary.txt','r')
    dictionary = data.read()
    dictionary_list = dictionary.split('\n')
    return dictionary_list

def find_valid_words(rack,dictionary_list):

    valid_words = []

    for word in dictionary_list:
        rack_copy = rack.copy()
        is_valid = True
        if len(word) >= len(rack) or word == '':
            continue

        for letter in word:
            upper_letter = letter.upper()

            if upper_letter in rack_copy:
                rack_copy.remove(upper_letter)
            else:
                is_valid = False
                break
        
        if is_valid:
            valid_words.append(word)
    
    return valid_words

def longest_word(valid_words):

    if len(valid_words) == 0:
        return
    elif len(valid_words) == 1:
        return valid_words[0]

    longest_word = valid_words[0]

    for word in valid_words[1:]:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word








if __name__ == "__main__":

    player_rack = []
    
    assign_tiles(player_rack)

    bag = create_shuffled_bag()
    
    dictionary_list = load_dictionary()

    print(player_rack)
    valid_words = find_valid_words(player_rack,dictionary_list)
    print(valid_words)
    print(longest_word(valid_words))


   

