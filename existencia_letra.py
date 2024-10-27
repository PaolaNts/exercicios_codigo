palavra = input("Digite uma palavra: ")
cont = 0

letras = list(palavra)

for i in letras:
    if i == "a" or i == "A":
        cont += 1

if cont > 0:
    print(f"Na palavra '{palavra}' tem {cont} letra(s) 'A'.")
else:
    print("Não tem letra 'A' nessa palavra.")
