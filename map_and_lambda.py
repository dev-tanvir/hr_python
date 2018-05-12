"""
    Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,  being the first number.
    Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

    input 5
    output [0,1,1,8,27]
"""


cube = lambda x: x**3

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        pre_list = fibonacci(n-1)  # recursion , for not needing to do it again during return
        return pre_list +  [pre_list[-1] + pre_list[-2]] # adding just last two of previous fibo list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
