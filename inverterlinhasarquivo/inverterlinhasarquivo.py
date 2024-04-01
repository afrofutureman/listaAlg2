with open("/home/runner/arquivos/pares.txt", "r+") as arquivo_pares:
  linhas = arquivo_pares.readlines()
  linhas = linhas[::-1]
  arquivo_pares = linhas
  print(arquivo_pares)