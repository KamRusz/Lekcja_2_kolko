import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

p1,p2,p3,p4,p5,p6,p7,p8,p9 = "-","-","-","-","X","-","-","-","-"
cls()
print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
#print ("podaj numer pola")
#pole = int(input())
while p1=="-" or p2=="-" or p3=="-" or p4=="-" or p6=="-" or p7=="-" or p8=="-" or p9=="-":
    if p1!="-" and p2!="-" and p3!="-" and p4!="-" and p6!="-" and p7!="-" and p8!="-" and p9!="-":
        break
    print ("podaj numer pola")
    pole = int(input())    
    if pole == 1:
        if p1 == "-":
            p1 = "O"
            cls()
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
           # print ("podaj numer pola")
           # pole = int(input())
            #cls()
            continue
        else:
            cls()
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            print ("błąd")
            #pole = int(input())
    elif pole == 2:
        if p2 == "-":
            p2 = "O"
            cls()
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            #print ("podaj numer pola")
            #pole = int(input())
        else:
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            print ("błąd\npodaj numer pola")
            pole = int(input())
            cls()
    elif pole == 3:
        if p3 == "-":
            p3 = "O"
            cls()
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            #print ("podaj numer pola")
            #pole = int(input())
        else:
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            print ("błąd\npodaj numer pola")
            pole = int(input())
            cls()
    elif pole == 4:
        if p4 == "-":
            p4 = "O"
            cls()
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
           # print ("podaj numer pola")
            #pole = int(input())
        else:
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            print ("błąd\npodaj numer pola")
            pole = int(input())
            cls()
    elif pole == 5:
        print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
        print ("błąd\npodaj numer pola")
        #pole = int(input())
        continue            
    elif pole == 6:
        if p6 == "-":
            p6 = "O"
            cls()
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
           # print ("podaj numer pola")
           # pole = int(input())
        else:
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            print ("błąd\npodaj numer pola")
            pole = int(input())
            cls()
    elif pole == 7:
        if p7 == "-":
            p7 = "O"
            cls()
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
           # print ("podaj numer pola")
            #pole = int(input())
        else:
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            print ("błąd\npodaj numer pola")
            pole = int(input())
            cls()
    elif pole == 8:
        if p8 == "-":
            p8 = "O"
            cls()
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
           # print ("podaj numer pola")
           # pole = int(input())
        else:
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            print ("błąd\npodaj numer pola")
            pole = int(input())
            cls()           
    elif pole == 9:
        if p9 == "-":
            p9 = "O"
            cls()
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
           # print ("podaj numer pola")
           # pole = int(input())
        else:
            print (f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}")
            print ("błąd\npodaj numer pola")
            pole = int(input())
            cls()           
    
print ('REMIS')