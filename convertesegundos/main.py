def dias_horas_minutos_segunfod(dias, horas, minutos, segundos):
  segundos = segundos + (minutos * 60) + (horas * 3600) + (dias * 86400)
  print(f"em segundos, tudo isso dá: {segundos}")
  return segundos

dias = int(input("digite a quantidade de dias: "))
horas = int(input("digite a quantidade de horas: "))
minutos = int(input("digite a quantidade de minutos: "))
segundos = int(input("digite a quantidade de segundos: "))

dias_horas_minutos_segunfod(dias, horas, minutos, segundos)