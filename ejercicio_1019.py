horas=int
minutos=int
segundos=int
N=int(input())
horas=round(N/3600)
minutos=round(N/60)
segundos=N%60
print(f"{horas}:{minutos}:{segundos}")