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
        if element > '0' and element < '9':
            temp += element
        elif temp != '':
            lst.append(int(temp))
            temp = ''
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
def getPrime(p):
    prime = []
    lst = []
    for i in range(len(p)):
        if p[i] not in lst:
            prime.append(p[i])
            result = p[i]
            for j in range(len(p)):
                result += p[i]
                if result > 1000:
                    break
                lst.append(result)
    lst = set(lst)
    for element in lst:
        p.remove(element)
    return p
        
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
    lst = []
    for i in range(100):
        lstlst = []
        for j in range(23):
            lstlst.append(random.randint(0,365))
        lst.append(lstlst)
    count = 0
    
    for i in range(len(lst) - 1):

        for j in range(len(lst[i])):
            
            for k in range(len(lst[i+1])):
                if lst[i][j] == lst[i+1][k]:
                    count+=1
                    break

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
            

    

lijst = []
for i in range(2,1001):
    lijst.append(i)

haha = [3,3,4,1,1,6,6,6,2,2]

print(next_las_seq(haha))

print(getPrime(lijst))

print (BirthDayParadox())

