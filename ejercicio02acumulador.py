# Dados los N días en que esta abierta una tiemda, determinar el total
# recaudado de las ventas diarias. Validar las ventas.
#ENTRADA
Ndias = int(input("Ingrese el total de días a contabilizar: \t"))
#PROCESO
acumuladorVentas = 0
for i in range (Ndias):
    #validar las ventas
    while True:
        try:
            ventas = float(input(f"Ingrese lo recaudado del día {i}: \t"))
            if (ventas < 0):
                print("ERROR... No puede haber una venta negativa.")
            else:
                break
        except:
            print("Formato de venta no válido")
    #Venta validada
    acumuladorVentas += ventas
#SALIDA
print(f"En {Ndias} dias, el total acumulado fue: {acumuladorVentas}")