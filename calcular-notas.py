

def perguntar_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

nota1 = perguntar_nota("informe a primeira nota: ")
nota2 = perguntar_nota("informe a segunda nota: ")
nota3 = perguntar_nota("informe a terceira nota: ")

nota = (nota1 + nota2 + nota3) / 3
print(f"nota {nota:.2f}")
if nota <= 3.0:
  print("reprovado")
elif nota > 3.0 and nota <6:
 print("recuperação")
else:
  print("aprovado")