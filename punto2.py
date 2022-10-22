numero1=int(input("Digite el primer numero: "))

numero2=int(input("Digite El segundo numero: "))

calcularnumeromayor=lambda numero1, numero2 : 1 if numero1>numero2 else -1

mostrarResultado=lambda numero : print("El primer número es mayor") if numero == 1 else print("El segundo número es mayor")

mostrarResultado(calcularnumeromayor(numero1, numero2))