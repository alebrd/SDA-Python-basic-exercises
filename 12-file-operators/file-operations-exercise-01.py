words_dict = {}

with open('data/exercise.txt') as f:
    for i, line in enumerate(f):
        if i == 0:
            continue

        clean_line = line.rstrip()
        clean_line = clean_line.lower()

        if clean_line == '':
            continue

        for char in ('.', ',', '!', '?'):
            clean_line = clean_line.replace(char, '')

        words = clean_line.split(' ')

        for word in words:
            if words_dict.get(word) is not None:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    # with open("data/result.txt", "w+") as f:  # open file in write mode
    #   for word in words_dict:
    #      f.write(f"Word {word} occurred {words_dict[word]} time(s).\n")

    for word in words_dict:
        print(f'Word {word} occurred {words_dict[word]} time(s).')

with open('data/result.txt', 'w') as f:
    for key, value in words_dict.items():
        f.write(f'{key} : {value}\n')
