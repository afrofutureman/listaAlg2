salario = float(input("digite o salário: "))

if salario <= 1250.00:
    salario = (salario/100)*15 + salario
else:
    salario = (salario/100)*10 + salario

print(f"Seu novo salário agora é de {salario:.2f}")