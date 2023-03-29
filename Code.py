def Frequency(sentence): #checks the frequency of word per text block
    W = [] #dynamic size 
    WordFreq = sentence.split()
    for i in WordFreq:
        if i not in W:
            W.append(i)
            
    for i in range (0, len(W)):
        print ('frequency of "', W[i], '" is', WordFreq.count(W[i]), '\n')


def LineAmt(sentence): #checks the amount of lines
    LineAmt = 0
    LineAmt = len(sentence.split("\n")) #Line is considered new when \n is counted
    print ('There is', LineAmt, 'line(s)')
    
def CharCount(sentence):
    CharCount = 0
    CharCount = len(sentence)
    print ('There are a total of', CharCount, 'Character(s)')


def main():
    sentence = input(' Please input your desired text.\n')
    Frequency(sentence)
    LineAmt(sentence)
    CharCount(sentence)
    
    
if __name__=="__main__":
    main()             # call main function


        

 
