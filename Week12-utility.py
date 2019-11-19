#   METHOD USED
#   Dylan Shapiro
#  ​CSCI 102 – Section A
#   Week 12 - Part A
def PrintOutput(var):
    print("OUTPUT",var)
    
def LoadFile(file):
    lines=[]
    with open(file) as f:
        file_content = f.readlines()
        for i in file_content:
            n=i.rstrip("\n")
            lines.append(str(n))
    return str(lines)

def UpdateString(word, letter, index):
    word=word[0:index]+letter+word[index+1:]
    PrintOutput(word)
    
def FindWordCount(new, word):
    return new.count(word)
    
def ScoreFinder(players, scores, name):
    name1=name.capitalize()
    Names=[]
    mins=[]
    for i in range(len(players)):
        Names.append([scores[i]])
        mins.append([players[i]])
    try:
        man=[mins.index(i) for i in mins if name1 in i]
        print("OUTPUT %s got a score of" %name1,end=" ")
        print(*Names[man[0]],sep='')
    except ValueError:
        print('OUTPUT player not found')
        
def Union( one, two):
    lis=[]
    for i in range(len(one)):
        lis.append(one[i])
    for j in range(len(two)):
        lis.append(two[j])
    return lis

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def NotIn(one, two):
    return (list(set(one) - set(two))) 
