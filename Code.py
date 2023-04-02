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


def main():
    sentence = input(' Please input your desired text.\n')
    Frequency(sentence)
    LineAmt(sentence)
    CharCount(sentence)


if __name__ == "__main__":
    main()  # call main function






    print ('The first test case will test that the program works with normal english letters, and that a space and newline are identified as white space. \n')
    sentence = ('This is the first test. \n Test Test')
    print(sentence)
    Frequency(sentence)
    
    print ('The second test case will test that the program works with numbers.')
    sentence = ('123 123 345 345 345')
    print(sentence)
    Frequency(sentence)
    
    print ('The third test case will test that the program works with numbers and letters.')
    sentence = ('h311o')
    print(sentence)
    Frequency (sentence)
    
    print ('The fourth test case will test that the program works with only symbols.')
    sentence = ('!?! !?! ???')
    print(sentence)
    Frequency(sentence)
    
    print ('The fifth test case will test that the program works with only symbols and letters.')
    sentence = ('!hellp !!!leope !@$#LOL')
    print(sentence)
    Frequency(sentence)
    
    print ('The sixth test case will test that the program works with only numbers and symbols.')
    sentence = ('2&& 23&& 2&&')
    print(sentence)
    Frequency(sentence)
    
    print ('The seventh test case will test that the program works with letters, numbers and symbols. This test will also test if tab is identified as white space.')
    sentence = ('Hel!0   Hel!0     80!s')
    print(sentence)
    Frequency(sentence)
    
    print ('The eighth test case will test that the code works with all white space (newline, tab and space)\n')
    sentence = ('hello hello    hello \n')
    print(sentence)
    Frequency(sentence)

    print ('The ninth test will test the longest word in the english dictionary to ensure long characters will be counted. It will also test just a letter seperated by white space to verify the shortest possible word will still be counted.\n')
    sentence =('Pneumonoultramicroscopicsilicovolcanoconiosis A ')
    print(sentence)
    Frequency(sentence)

    print('The tenth test will make sure the total amount of characters within the string is correct')
    sentence = ("There will be 27 characters")
    print(sentence)
    CharCount(sentence)

    print('The eleventh test will count the number of lines')
    sentence = ('There \n are \n 5 \n lines \n here')
    print(sentence)
    LineAmt(sentence)

    print('The eleventh test will make sure no other method of lines is counted')
    sentence = (' There '
                'should be '
                'one line '
                'counted')
    print(sentence)
    LineAmt(sentence)
    
if __name__=="__main__":
    main()             # call main function
