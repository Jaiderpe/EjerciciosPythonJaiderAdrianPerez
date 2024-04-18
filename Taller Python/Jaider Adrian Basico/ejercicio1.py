leer = 0
sumatoria = 0

for i in range(0,3,1):
 leer += float(input(f"ingrese numero {1+i}:"))
if leer > 0:
 sumatoria = sumatoria + leer
 print(f"la sumatoria es : ",sumatoria)
  