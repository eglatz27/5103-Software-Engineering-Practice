def Frequency(sentence): #checks the frequency of word per text block
    W = [] #dynamic size 
    sentence = sentence.split()
    
    for i in sentence:
        if i not in W:
            W.append(i)
    
    for i in range (0, len(W)):
        print ('frequency of', W[i], 'is', sentence.count(W[i]), '\n')


def main():
    sentence = input('Please input your desired text.\n')
    Frequency(sentence)
    
if __name__=="__main__":
    main()             # call main function


        

        