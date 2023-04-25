def Frequency(sentence):  # checks the frequency of word per text block
    W = []  # dynamic size
    WordFreq = sentence.split()
    for i in WordFreq:
        if i not in W:
            W.append(i)

    for i in range(0, len(W)):
        print('frequency of "', W[i], '" is', WordFreq.count(W[i]), '\n')


def LineAmt(sentence):  # checks the amount of lines
    LineAmt = 0
    LineAmt = len(sentence.split("\n"))  # Line is considered new when \n is counted
    print('There is', LineAmt, 'line(s)\n')


def CharCount(sentence):
    CharCount = 0
    CharCount = len(sentence)
    print('There are a total of', CharCount, 'Character(s)\n')


def replace_word(sentence, pattern, replacement):
    words = sentence.split()
    for i, word in enumerate(words):
        if word == pattern:
            words[i] = replacement
    return ' '.join(words)


def main():
    while True:
        sentence = input('Please input your desired text.\n')
        Frequency(sentence)
        LineAmt(sentence)
        CharCount(sentence)
        answer = input('Would you like to change any words? Answer "Yes" or "No"\n')
        if answer == "Yes":
            pattern = input('What word would you like to replace? Remember your answer is case sensitive. \n')
            replacement = input('What word would you like to replace the previous word with? Remember your answer is case sensitive.\n')
            sentence = replace_word(sentence, pattern, replacement)
            print(sentence)
        elif answer == "No":
            break
        else:
            print('Please answer Yes or No')


if __name__ == "__main__":
    main()  # call main function
