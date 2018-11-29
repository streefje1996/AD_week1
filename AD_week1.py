"""
Stefan van der Ham
1717534
V2C
Frits Dannenberg
"""



import random

"""
description
----------
gets maximum value of an element from a list

Parameters
----------
a : list
list of numeric value

Return
------
high: float, int, double
depending on value in list
"""
def mymax(a):
    assert len(a) != 0
    high = a[0]
    for element in a:
        if element > high:
            high = element
    return high

"""
description
----------
gets all the numbers from a string

Parameters
----------
s : string
string

Return
------
lst: list
list containing all the numbers in the string
"""
def getnumbers(s):
    lst = []
    temp = ''
    for element in s:
        if element >= '0' and element <= '9':
            temp += element
        elif temp != '':
            lst.append(int(temp))
            temp = ''

    if temp != '':
        lst.append(int(temp))
    return lst

"""
description
----------
finds prime numbers in a list using the sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Parameters
----------
p : list
list containing numbers in wich prime numbers need to be found

Return
------
p: list
containing all the prime numbers
"""
def getPrime(N):
    primeNums = []

    numbers = {}
    for i in range(2,N+1):
        numbers[i] = True

    for i in numbers:
        for j in range(2, N+1):
            if(i * j < N+1):
                numbers[i*j] = False
            else:
                break

    for x, y in numbers.items():
        if(y):
            primeNums.append(x)

    return primeNums
        
"""
description
----------
gets the number of matching lists form randomly genereated values
https://en.wikipedia.org/wiki/Birthday_problem

Parameters
----------
-

Return
------
count: int
amount of times the list is matching
"""
def BirthDayParadox():
    klassen = []
    for i in range(100):
        studenten = []
        for j in range(23):
            studenten.append(random.randint(0,364))
        klassen.append(studenten)
    count = 0

    
    for klas in klassen:
        dagen = [0] * 365
        for student in klas:
            if dagen[student] > 1:
                count += 1
                break
            else:
                dagen[student] += 1

    return count

"""
description
----------
Gets the next iteration of the Look-and-say sequence

Parameters
----------
a : list
list of numeric values

Return
------
result: list
contains the next iteration of the sequence
"""
def next_las_seq(x):
    result = []
    first = 0
    last = 0
    current = x[0]
    for i in range(len(x)):
        if x[i] == current:
            last = i;
        else:
            result.append(last - first + 1)
            result.append(current)
            first = i
            last = i;
            current = x[i]
    result.append(last - first + 1)
    result.append(current)
    return result
            

    

getallen = list(range(2,1001))

haha = [3,3,4,1,1,6,6,6,2,2]

print(next_las_seq(haha))

print(getPrime(10001))

print (BirthDayParadox())

print(getnumbers("77ga8a9ga7")) 

