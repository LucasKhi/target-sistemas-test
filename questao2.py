def fibonacci_calc(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def is_in_fibonacci(n):
    fib_sequence = fibonacci_calc(n)
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

try:
    number = int(input("Informe um número: "))
    print(is_in_fibonacci(number))
except ValueError:
    print("Por favor, insira um número inteiro válido.")
