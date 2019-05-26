print("¿CUANTOS CUADRADOS PUEDEN HABER DENTRO DE UNO MAS GRANDE?")
print("")
print("¿Cual es la dimension de su cuadrado? (Ingrese solo un lado)")
lado = input()
i = 1
total=0
while True:
    print("Los cuadrados que tiene dentro son:")
    print("Cuadrados de ", i,"x",i, "---->", int(lado)*int(lado))
    total=int(total)+int(lado)*int(lado)
    i=int(i)+1
    lado=int(lado)-1
    if(lado < 1):
        break
print("Total de cuadrados: ", total)
