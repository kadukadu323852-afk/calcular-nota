nota1 = -1
while nota1 <0 or nota1 >10:
  nota1 = float(input("informe a primeira nota: "))
nota2 = -1
while nota2 <0 or nota2 >10:
  nota2 = float(input("informe a segunda nota: "))
nota3 = -1
while nota3 <0 or nota3 >10:
  nota3 = float(input("informe a terceira nota: "))
nota = (nota1 + nota2 + nota3) / 3
print(f"nota {nota:.2f}")
if nota <= 3.0:
  print("reprovado")
elif nota > 3.0 and nota <= 5.9:
 print("recuperação")
else:
  print("aprovado")