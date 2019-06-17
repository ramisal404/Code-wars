"""

Sum of two lowest positive integers

https://www.codewars.com/kata/558fc85d8fd1938afb000014

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

"""

def sum_two_smallest_numbers(numbers):
    def_num = float("inf")
    def_num2= float("inf")
    for number in numbers:
        if number < def_num:
            def_num = number
    for num in numbers:
        if num < def_num2 and num > def_num:
            def_num2 = num
    return def_num + def_num2
