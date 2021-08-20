# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85


old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'],
  5: ['K'],
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(word):
    word = word.upper()
    letterPoints = ""

    for char in word:
        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(char = char, point_value = point_value)

    return letterPoints

# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

def initial_prompt():
    word_to_score = input("Please enter word to score: ")
    # print("Let's play some Scrabble!\n")
    return word_to_score

def simple_scorer(word):
    word = word.upper()
    # letter_points = {}
    total_count = 0

    
    for char in word:
        # letter_points[char] = 1
        total_count = total_count + 1
    # letter_points = 0
    # for char in word:
    #     letter_points = letter_points + 1
    # return letter_points, total_count

    # wtf_I_am_do
    # print = (f"{letter_points} \n Total points: {total_count}")

    return total_count

def vowel_bonus_scorer(word):
    word = word.lower()
    vowels = "aeiou"
    total_count = 0
    for char in word:
        if char in vowels:
            total_count = total_count + 3
        else:
            total_count = total_count + 1
    # print(total_count)
    return total_count

def scrabble_scorer(word, new_point_structure):
    word = word.upper()
    total_count = 0
    for char in word:
        if char in new_point_structure.keys():
            total_count = total_count + new_point_structure[char]
            # print(f"{char} : {new_point_structure[char]}")

    return total_count

# scoring_algorithms = ()

def scorer_prompt(word):
    score_num = None
    while True:
        try:
            score_num = int(input("\nEnter: 0, 1 or 2: "))
            break
        except ValueError:
            print("Enter: 0, 1 or 2. You dumnass. Star over again!!!")
            run_program()

    if score_num == 0:
        print(f"Score for '{word}': {simple_scorer(word)}")
    elif score_num == 1:
        print(f"Score for '{word}': {vowel_bonus_scorer(word)}")
    elif score_num == 2:
        print(f"Score for '{word}': {scrabble_scorer(word, transform(old_point_structure))}")
    else:
        print("Enter: 0, 1 or 2. You dumnass. Star over again!!!")
        run_program()


def transform(old_point_structure):
    new_point_structure = {}
    for point in old_point_structure.keys():
        # print(point)
        for letter in old_point_structure[point]:
            new_point_structure[letter] = point
            # print(letter)
    # print(new_point_structure)
    return new_point_structure

def run_program():
    word = initial_prompt()
    print("\nWhich scoring algorithm would you like to use?\n\n0 - Simple: One point per character\n1 - Vowel Bonus: Vowels are worth 3 points\n2 - Scrabble: Uses scrabble point system")
    scorer_prompt(word)
    return

