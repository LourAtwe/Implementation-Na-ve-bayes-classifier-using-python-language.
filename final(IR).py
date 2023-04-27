
labels=[]
Count=[]
CountNo=[]
Unique=[]
Yesresult=[]
Noresult=[]
forno=[]
foryes=[]

print("Note!!!!!!!!!")
print("if you want enter (yes) please enter it like that--> Yes")
print("if you want enter (no) please enter it like that--> No")
print("-------------------------------------------------")
n=int(input("Enter num of train doc:"))
count=0
count1=0
for i in range(0,n):
    doc=str(input("Enter the doc:"))
    labeldoc=input("Enter the label:")
    labels.append(labeldoc)
    d1=doc.split()
    if labeldoc=="Yes":
        
        foryes.extend(d1)
        count=count +len(d1)
    else:
        forno.extend(d1) 
        count1=count1 +len(d1)
 
   

    unique_wordsD1 = set(d1)
    Unique.extend(unique_wordsD1)
  
  

#print(unique_wordsD1)

#print(Ccountd1)


Test=str(input("Enter the Test Doc:"))


result = dict((i, labels.count(i)/len(labels)) for i in labels)

#print(result)

pYes=result["Yes"]
pNo=result["No"]
print("p(yes):",pYes)
print("p(No):",pNo)
print("---------------------------------------")

#print(Count)
VocabYes=count
print("Vocab(Yes):",VocabYes)

VocabNo=count1
print("Vocab(No):",VocabNo)
print("---------------------------------------")

print("Num of Unique value:", len(set(Unique)))
#print("---------------------------------------")
Lour = dict((i, foryes.count(i)) for i in foryes)   

Lour2 = dict((i, forno.count(i)) for i in forno)   
def multiplyList(Yesresult):
    result = 1
    for x in Yesresult:
        result = result * x
    return result
sum=0
#when the class ==Yes
e=Test.split()
s=set(e)
#print(e)
pr=1
for i in e:
    
    if i in Lour:
        #print("probability for",i,"to be Yes:")
        p=Lour[i]
        x=(p+1)/(VocabYes+len(set(Unique)))
        #print(x)
        pr=pr*x
    else:
        p=0
       
        #print("probability for",i,"to be Yes:")
        x=(p+1)/(VocabYes+len(set(Unique)))
        #print(x)   
        pr=pr*x

print("---------------------------------------")
for i in e:    
    if i in Lour2:
        #print("probability for",i,"to be No:")
        p=Lour2[i]
        x=(p+1)/(VocabNo+len(set(Unique)))
        #print(x)
        pr=pr*1
        
    else:
        p=0
        
        #print("probability for",i,"to be No:")
        x=(p+1)/(VocabNo+len(set(Unique)))
        #print(x) 
        pr=pr*x
print("probability to be No",pr*pNo )
print("probability to be Yes",pr*pYes )
if pr*pNo>pr*pYes:
    print("The label for :",Test, "is:",("(No)"))
else:
    print("The label for :","[",Test,"]", "is:",("(Yes)"))


print("---------------------------------------")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    