##Title: Complex Counting 
##Author: James Moody

import itertools
import numpy
import sys
import time
import matplotlib
from itertools import combinations

##for combinations
def combinations():
    counts = 0
    list1 =[]
    sizeofthelist = int(input("number of ojects: "))
    
    for i in range(0,sizeofthelist,1):
        list1.append(i)
        
    choose = int(input("choose: "))

    ##For spacing
    print()
    print()
    
    comb = itertools.combinations(list1,choose)
    for i in comb:
        ##print(i)
        counts= counts+1

    print("ANSWER = ",counts)


##for permutations
def permutations():
    counts = 0
    list1 =[]
    sizeofthelist = int(input("number of ojects: "))
    
    for i in range(0,sizeofthelist,1):
        list1.append(i)
        
    choose = int(input("choose: "))

    ##For spacing
    print()
    print()
    
    comb = itertools.permutations(list1,choose)
    for i in comb:
        ##print(i)
        counts= counts+1

    print("ANSWER = ",counts)

##for stars and bars
def StarBar():
    counts = 0
    boxes = int(input("How many destinquishable?:" ))-1
    balls = int(input("How many indestinguishable?: "))
    list1 = []
    
    for i in range(0,boxes+balls,1):
        list1.append(i)
        
    choose = boxes
    
    total = itertools.combinations(list1,choose)
    for i in total:
        counts = counts+1

    print("ANSWER = ",counts)

    
##for PIE counting
def removal(pos,list1,determiner):
    list2 = list1[:(pos-determiner)]
    
    ##print (list2)
    return list2

def PIE():
    total = 0
    counts = 0
    pos = 0
    setsCounter = 0
    boxes = int(input("How many destinquishable?:" ))-1
    balls = int(input("How many indestinguishable?: "))
    list1 = []
    
    for i in range(0,boxes+balls,1):
        list1.append(i)
        pos = pos+1
        
    choose = boxes
    
    comb = itertools.combinations(list1,choose)
    
    for i in comb:
        total = total+1
        
    sets = []
    
    for c in range(0,boxes+1,1):
        sets.append(c)
        setsCounter = setsCounter+1
        
    determiner = int(input("How many?:"))
    
    for i in range (1,setsCounter,1):
        determining = determiner*i
        total_1 = 0
        total_2 = 0
        ChooseWithinSet = []
        chooseSet = []
        countsprevious = counts
        counts = 0
        
        chooseSets = itertools.combinations(sets,i)
        
        for g in chooseSets:
            total_1 = total_1 + 1

        ChooseWithinSet = itertools.combinations(removal(pos,list1,determining),boxes)
        
        for h in ChooseWithinSet:
            total_2 = total_2 + 1
            
        ##print(total_1)
        ##print(total_2)
            
        counts = ((-1)**(i-1))*(total_1)*(total_2)+ countsprevious
        if(total_1*total_2 ==0):
            break
        
    print(counts)   
    print("ANSWER = " ,total-counts)  
    

def main():
    X = "N"
    
    while(X == "N"):
        choice = int(input(" 1 Combinations \n 2 Permutations \n 3 Stars and Bars \n 4 PIE \n Choice: "))
        sys.stdin.flush()
        
        if(choice == 1):
            combinations()
            
        elif (choice == 2):
            permutations()
            
        elif (choice == 3):
            StarBar()
            
        elif (choice == 4):
            PIE()
            
        else:
            print("that is not an option")

        print("\n")
        X = str(input("Quit? Y or N: "))
        
    if(X == "Y"):
        print("bye")


main()






