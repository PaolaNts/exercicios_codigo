def sequencia_fibonacci(n):
    sequencia_fib = [0, 1]
    while True:
        proximo_fib = sequencia_fib[-1] + sequencia_fib[-2]
        if proximo_fib > n:
            break
        sequencia_fib.append(proximo_fib)
    return sequencia_fib

def verificar_fibonacci(n):
    if n < 0:
        return False
    sequencia_fib = sequencia_fibonacci(n)
    return n in sequencia_fib

try:
    numero = int(input("Digite um número: "))
    if verificar_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número válido.")
