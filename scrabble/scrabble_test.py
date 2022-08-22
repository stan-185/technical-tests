from random import shuffle

LETTER_SCORES =  {'A' : 1, 'E' : 1, 'I' : 1, 'O' : 1, 'N' : 1,'R' : 1, 'T' : 1, 'L' : 1, 'S' : 1, 'U' : 1, 'D' : 2, 'G' : 2, 'B' : 3, 'C' : 3, 'M' : 3, 'P' : 3, 'F' : 4, 'H' : 4, 'V' : 4, 'W' : 4, 'Y' : 4, 'K': 5, 'J': 8, 'X':8, 'Q':10,'Z':10}

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
     









if __name__ == "__main__":

    player_rack = []

    print(calculate_word_score('Guardian'))
    
    assign_tiles(player_rack)
    print(player_rack)

