def aumento(salario):
  if salario <= 1250.00:
      salario = (salario/100)*15 + salario
  else:
      salario = (salario/100)*10 + salario
  print(f"Seu novo salário agora é de R$ {salario:.2f}")
  return salario

salario = float(input("Digite seu salário atual: "))

aumento(salario)