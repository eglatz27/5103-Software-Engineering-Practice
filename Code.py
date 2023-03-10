def Frequency(sentence): #checks the frequency of word per text block
    W = [] #dynamic size 
    sentence = sentence.split()
    
    for i in sentence:
        if i not in W:
            W.append(i)
    
    for i in range (0, len(W)):
        print ('frequency of', W[i], 'is', sentence.count(W[i]))


def main():
    sentence = input('Please input your desired text.\n')
    Frequency(sentence)






    print ('The first test case will test that the program works with normal english letters, and that a space and newline are identified as white space. \n')
    sentence = ('This is the first test. \n Test Test')
    Frequency(sentence)
    
    print ('The second test case will test that the program works with numbers.')
    sentence = ('123 123 345 345 345')
    Frequency(sentence)
    
    print ('The third test case will test that the program works with numbers and letters.')
    sentence = ('h311o')
    Frequency (sentence)
    
    print ('The fourth test case will test that the program works with only symbols.')
    sentence = ('!?! !?! ???')
    Frequency(sentence)
    
    print ('The fifth test case will test that the program works with only symbols and letters.')
    sentence = ('!hellp !!!leope !@$#LOL')
    Frequency(sentence)
    
    print ('The sixth test case will test that the program works with only numbers and symbols.')
    sentence = ('2&& 23&& 2&&')
    Frequency(sentence)
    
    print ('The seventh test case will test that the program works with letters, numbers and symbols. This test will also test if tab is identified as white space.')
    sentence = ('Hel!0   Hel!0     80!s')
    Frequency(sentence)
    
    
    

    
if __name__=="__main__":
    main()             # call main function
