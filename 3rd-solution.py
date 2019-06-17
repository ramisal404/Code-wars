"""

IQ Test

https://www.codewars.com/kata/552c028c030765286c00007d

Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

"""

def iq_test(numbers):
    odd_count = 0
    even_count = 0
    lst = [int(s) for s in numbers.split(' ')]
    even_num = None
    odd_num = None
    for number in lst:
       if number % 2 == 0:
           even_count += 1
           even_num = number
       elif number % 2 == 1:
           odd_count += 1
           odd_num = number
    if even_count < odd_count:
        return lst.index(even_num)+1
    elif even_count > odd_count:
        return lst.index(odd_num)+1
