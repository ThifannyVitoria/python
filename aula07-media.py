# elaborar um algoritimo que solicita 4 notas de usaário
# o programa deve calcular a média a
# verificar sse a média é maior o igual a 80
# se a média for maio ou igual a 80, o programa
# deve exibir a mensagem "Aprovado" e se a média for menor que
# 80, o programa deve exibir a mensagem "Reprovado".
 
nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))
nota3 = float(input("digite a nota 3: "))
nota4 = float(input("digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) /4
print(f"A média final obtida = {media}")