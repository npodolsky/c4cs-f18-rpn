#!/usr/bin/env python3
import operator


op = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow,
        '//': operator.floordiv
}

def calculate(arg):
    # stack for calculator
    stack = list()

    # process tokens
    for token in arg.split():
        try:
            value = int(token)
            stack.append(value)
        except ValueError:
            if token == 's':
                result = 0
                while stack:
                    val = stack.pop()
                    result = result + val
            else:
                val2 = stack.pop()
                val1 = stack.pop()
            
                if token =='%':
                    val2 = val2 / 100
                    result = val2 * val1
                elif token == '/' and val2 == 0:
                    print("Error: Cannot divide by 0")
                    result = val1
                else:
                    # Look up function in table
                    func = op[token]
                    result = func(val1, val2)
                
            stack.append(result)
    
    if len(stack) != 1:
        raise TypeError("Too many parameters")

    return stack.pop()

def main():
    while True:
        result = calculate(input('rpn calc> '))
        print("Result: ", result)

if __name__ == '__main__':
    main()


