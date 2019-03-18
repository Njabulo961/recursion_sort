def sum_array(array):

    """
    sum_array takes in a list of numbers,
    returns the sum.

    Parameters
    ----------
    items : list
        list of unordered numbers

    Returns
    -------
    sum: number
        sum of elements in array
    """

    # Base case
    if len(array) == 0:
        return 0

    # Summing recursively
    else:
        return array[0] + sum_array(array[1:]) 

def fibonacci(n):

    """
    Fibonacci takes in an integer,
    returns nth term in fibonacci sequence.

    Parameters
    ----------
    n : integer
        non-negative integer

    Returns
    -------
    n! : integer
        sum of elements in array
    """

    # Accounting for incorrect input
    if n<=0: 
        print("Input should be greater than zero") 

    # First Fibonacci number is 0 
    elif n==1: 
        return 0

    # Second Fibonacci number is 1 
    elif n==2: 
        return 1

    # Recursive formula for finding nth fibonacci sequence term
    else: 
        return fibonacci(n-1) + fibonacci(n-2) 



def factorial(n):

    """
    factorial takes in a non-negative integer n.
    returns n!

    Parameters
    ----------
    n : integer
        non-negative integer

    Returns
    -------
    n! : integer
        n!
    """"     
    # Define 0! and 1!
    if n == 0 or n == 1:
        return 1

    # Recursive formula for finding factorial
    else:
        return n * factorial(n-1)

def reverse(word):

    """
    reverse takes in a string.
    returns string in reverse

    Parameters
    ----------
    word : string
        word as a string

    Returns
    -------
    String
        reversed word
    """"

    # Base Case: Account for empty string
    if len(word) == 0:
        return word


    # Recursively reverse string
    else:
        return reverse(word[1:]) + word[0]