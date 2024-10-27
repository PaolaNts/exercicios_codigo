def a():
    sequencia = [1, 3, 5, 7]
    return sequencia[-1] + 2

def b():
    sequencia = [2, 4, 8, 16, 32, 64]
    return sequencia[-1] * 2

def c():
    sequencia = [0, 1, 4, 9, 16, 25, 36]
    proximo_numero = int(len(sequencia)) ** 2
    return proximo_numero

def d():
    sequencia = [4, 16, 36, 64]
    proximo_numero = ((len(sequencia) + 1) * 2) ** 2
    return proximo_numero

def e():
    sequencia = [1, 1, 2, 3, 5, 8]
    return sequencia[-1] + sequencia[-2]

def f():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    return sequencia[-1] + 1

print("a) Próximo elemento:", a())
print("b) Próximo elemento:", b())
print("c) Próximo elemento:", c())
print("d) Próximo elemento:", d())
print("e) Próximo elemento:", e())
print("f) Próximo elemento:", f())
