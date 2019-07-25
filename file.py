

f = open("sample.txt", "rt")

def find_lines():
    lines = 0 
    for x in f :
        lines+=1
         
    print(open("sample.txt", "rt").read())
    print("the num of line is",lines)



def find_a():
    num_a = 0
    sample = open("sample.txt", "rt").read()
    
    for x in sample:
        if (x=='a'):
            num_a+=1
    
    print("the number of char a is ",num_a)

def find_str():
    
    sample=open("sample.txt", "rt").read()
    patternFail="Fail"
    patternSuccess="Success"
    
    lastindexFail= sample.rfind(patternFail,0)
    lastindexSuccess=sample.rfind(patternSuccess,0)
    
    if (lastindexFail==-1 and lastindexSuccess==-1):
        print("not found")
    elif (lastindexFail==-1 or lastindexSuccess==-1):
        print(max(lastindexFail,lastindexSuccess))
    else:
        last2indexFail = sample.rfind(patternFail,0,sample.rfind(patternFail))
        last2indexSuccess = sample.rfind(patternSuccess,0,sample.rfind(patternSuccess))
        
        list1=[last2indexFail,last2indexSuccess,lastindexFail,lastindexSuccess]
        list1.remove(max(list1))
        
        resultIndex=max(list1)
        
        if(sample[resultIndex]=='F'):
            print(sample[resultIndex:resultIndex+4],resultIndex)
        else:
            print(sample[resultIndex:resultIndex+7],resultIndex)
            

def find_dic():
    dic ={}
    sample=open("sample.txt", "rt").read()
    
    strings = sample.strip().split(" ")
    for str in strings:
        char = str[0]
        
        if (char in dic ):
            dic[char].append(str)
        else:
            dic[char]=[str]
  
    print(sorted(dic.items()))       
 
#find_lines()
#find_a()   
find_str() 
find_dic() 