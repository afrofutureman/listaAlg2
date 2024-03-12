def preco_passagem(km):
  if km <= 200:
      preco = km*0.5
  else:
      preco = km*0.45

  print(f"O preço da sua passagem é de R$ {preco:.2f}")
  return preco
km = int(input("Digite a distância da sua viagem: "))

preco_passagem(km)