import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

p1,p2,p3,p4,p5,p6,p7,p8,p9 = "-","-","-","-","X","-","-","-","-"

print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
#print ("podaj numer pola")
#pole = int(input())
while p1=="-" or p2=="-" or p3=="-" or p4=="-" or p6=="-" or p7=="-" or p8=="-" or p9=="-":
    cls()
    print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
    if p1!="-" and p2!="-" and p3!="-" and p4!="-" and p6!="-" and p7!="-" and p8!="-" and p9!="-":
        break
    if p1=="X" and p2=="X" and p3=="X":
        break
    if p1=="X" and p4=="X" and p7=="X":
        break
    if p3=="X" and p6=="X" and p9=="X":
        break
    if p7=="X" and p8=="X" and p9=="X":
        break 
    if p2=="X" and p8=="X":
        break           
    if p4=="X" and p6=="X":
        break
    if p1=="X" and p9=="X":
        break        
    if p3=="X" and p7=="X":
        break
    print ("podaj numer pola")
    pole = int(input())    
    if pole == 1:
        if p1 == "-":
            p1 = "O"
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
           # print ("podaj numer pola")
           # pole = int(input())
            #cls()
            #continue
        else:
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            print ("błąd")
            continue
            #pole = int(input())
    elif pole == 2:
        if p2 == "-":
            p2 = "O"
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            #print ("podaj numer pola")
            #pole = int(input())
        else:
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            print ("błąd")
            #pole = int(input())
            continue
    elif pole == 3:
        if p3 == "-":
            p3 = "O"
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            #print ("podaj numer pola")
            #pole = int(input())
        else:
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            print ("błąd")
            continue
            #pole = int(input())
    elif pole == 4:
        if p4 == "-":
            p4 = "O"
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
           # print ("podaj numer pola")
            #pole = int(input())
        else:
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            print ("błąd")
            #pole = int(input())
            continue
    elif pole == 5:
        cls()
        print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
        print ("błąd")
        #pole = int(input())
        continue            
    elif pole == 6:
        if p6 == "-":
            p6 = "O"
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
           # print ("podaj numer pola")
           # pole = int(input())
        else:
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            print ("błąd")
            #pole = int(input())
            continue
    elif pole == 7:
        if p7 == "-":
            p7 = "O"
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
           # print ("podaj numer pola")
            #pole = int(input())
        else:
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            print ("błąd")
            #pole = int(input())
            continue
    elif pole == 8:
        if p8 == "-":
            p8 = "O"
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
           # print ("podaj numer pola")
           # pole = int(input())
        else:
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            print ("błąd")
            #pole = int(input()) 
            continue         
    elif pole == 9:
        if p9 == "-":
            p9 = "O"
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
           # print ("podaj numer pola")
           # pole = int(input())
        else:
            cls()
            print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")
            print ("błąd")
            #pole = int(input())     
            continue      
    if p1=="O":
        if p3=="-":
            p3="X"
        elif p2=="-":
            p2="X"
        elif p4=="-":
            p4="X"
        elif p6=="-":
            p6="X"   
        elif p7=="-":
            p7="X" 
        elif p8=="-":
            p8="X"
        elif p9=="-":
            p9="X"   
    if p2=="O":
        if p1=="-":
            p1="X"
        elif p3=="-":
            p3="X"
        elif p4=="-":
            p4="X"
        elif p6=="-":
            p6="X"   
        elif p7=="-":
            p7="X" 
        elif p8=="-":
            p8="X"
        elif p9=="-":
            p9="X"   
    if p3=="O":
        if p2=="-":
            p2="X"
        elif p1=="-":
            p1="X"
        elif p4=="-":
            p4="X"
        elif p6=="-":
            p6="X"   
        elif p7=="-":
            p7="X" 
        elif p8=="-":
            p8="X"
        elif p9=="-":
            p9="X"   
    if p4=="O":
        if p9=="-":
            p9="X"
        elif p1=="-":
            p1="X"
        elif p2=="-":
            p2="X"                                        
        elif p4=="-":
            p4="X"
        elif p6=="-":
            p6="X"   
        elif p7=="-":
            p7="X" 
        elif p8=="-":
            p8="X"
    if p6=="O":
        if p7=="-":
            p7="X"
        elif p3=="-":
            p3="X" 
        elif p1=="-":
            p1="X"
        elif p4=="-":
            p4="X"
        elif p6=="-":
            p6="X"   
        elif p8=="-":
            p8="X"
        elif p9=="-":
            p9="X" 
    if p7=="O":
        if p4=="-":
            p4="X"
            continue
        elif p2=="-":
            p2="X" 
        elif p1=="-":
            p1="X"
        elif p4=="-":
            p4="X"
        elif p6=="-":
            p6="X"   
        elif p8=="-":
            p8="X"
        elif p9=="-":
            p9="X"  
    if p8=="O":
        if p6=="-":
            p6="X" 
            continue  
        elif p1=="-":
            p1="X"
        elif p2=="-":
            p2="X"
        elif p3=="-":
            p3="X"
        elif p4=="-":
            p4="X"
        elif p7=="-":
            p7="X" 
        elif p9=="-":
            p9="X" 
    if p9=="O":
        if p8=="-":
            p8="X"
            continue
        elif p1=="-":
            p1="X"
            continue
        elif p2=="-":
            p2="X"
            continue
        elif p3=="-":
            p3="X"  
            continue                                              
        elif p4=="-":
            p4="X"
            continue
        elif p6=="-":
            p6="X"  
            continue 
        elif p7=="-":
            p7="X" 
            continue

    cls()    
    print (f"|{p1}{p2}{p3}|\n|{p4}{p5}{p6}|\n|{p7}{p8}{p9}|")    
if p1!="-" and p2!="-" and p3!="-" and p4!="-" and p6!="-" and p7!="-" and p8!="-" and p9!="-":
    print ('REMIS')
else:
    print ('PRZEGRAŁEŚ')