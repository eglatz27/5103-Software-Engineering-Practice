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

    print('The twelfth test will make sure no other method of lines is counted')
    sentence = (' There '
                'should be '
                'one line '
                'counted')
    print(sentence)
    LineAmt(sentence)
    
    print('the thirteenth test will test the "replace_word" function with a sentence containing one occurrence of the pattern word')
    sentence = "Garfield ate Lasagna"
    pattern = "ate"
    replacement = "munched"
    expected_output = "Garfield munched Lasagna"
    assert replace_word(sentence, pattern, replacement) == expected_output
    
    print('the fourteenth test will test the "replace_word" function with a sentence containing multiple occurrences of the pattern word.')
    sentence = "How are you you doing?"
    pattern = "you"
    replacement = "yuo"
    expected_output = "How are yuo yuo doing?"
    assert replace_word(sentence, pattern, replacement) == expected_output
    
    print('the fifteenth test will test the "replace_word" function with a sentence containing the pattern word as part of another word.')
    sentence = "I will have an apple"
    pattern = "app"
    replacement = "gra"
    expected_output = "I will have an grale"
    assert replace_word(sentence, pattern, replacement) == expected_output
    
    print('the sixteenth test the main function by inputting a sentence and answering "No" to the word replacement question.')
    sentence = "Hello there"
    answer = "No"
    
    print('the seventeenth test will test the main function by inputting a sentence and answering "Yes" to the word replacement question and replacing a single word.')
    sentence = "Hello there"
    pattern = "Hello"
    replacement = "Hi"
    answer = "Yes"
    
    print('the eighteenth test will test the main function by inputting a sentence and answering with an invalid answer to the word replacement question.')
    sentence = "Hello there"
    answer = "Nope!!!!"
    
