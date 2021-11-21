cantidad = int(input())
i = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
sumaAcidez = 0
sumaMateria = 0
a = 4  # "sumamente apto"
b = 3  # "moderadamente apto"
c = 2  # "marginalmente apto"
d = 1  # "no apto"
listaSalidaAcidez = []
listaSalidaMateria = []

archivo = open("Prueba de Escritorio.txt", "r")

while i < cantidad:
    acidez = archivo.readline().split()  # input()
    materiaOrganica = archivo.readline().split()  # input()

    for aci, matOrg in zip(acidez, materiaOrganica):
        sumaAcidez += float(aci)
        sumaMateria += float(matOrg)

    promAcidez = sumaAcidez / len(acidez)
    promMateria = sumaMateria / len(materiaOrganica)

    # categoria acidez
    if 5.5 < promAcidez <= 6.5:
        catAcidez = a
    elif (6.5 < promAcidez <= 7.0) or (5.0 < promAcidez <= 5.5):
        catAcidez = b
    elif (7.0 < promAcidez <= 8.0) or (4.5 <= promAcidez <= 5.0):
        catAcidez = c
    elif promAcidez > 8.0 or promAcidez < 4.5:
        catAcidez = d

    # categoria materia organica
    if promMateria < 3:
        catMateria = d
    elif promMateria <= 4:
        catMateria = c
    elif promMateria <= 5:
        catMateria = b
    elif promMateria > 5:
        catMateria = a

    # si son iguales
    if catMateria == catAcidez:
        categoriaDefinitiva = catAcidez
    else:
        # si son diferentes
        if catAcidez < catMateria:
            categoriaDefinitiva = catAcidez
        else:
            categoriaDefinitiva = catMateria

    # conteo por categorias
    if categoriaDefinitiva == 4:
        cont1 += 1
    elif categoriaDefinitiva == 3:
        cont2 += 1
    elif categoriaDefinitiva == 2:
        cont3 += 1
    elif categoriaDefinitiva == 1:
        cont4 += 1

    listaSalidaAcidez.append("{:.2f}".format(promAcidez))
    listaSalidaMateria.append("{:.2f}".format(promMateria))
    # restaura
    sumaAcidez = 0
    sumaMateria = 0

    # incremento
    i += 1
    
archivo.close()
print(" ".join(listaSalidaAcidez))
print(" ".join(listaSalidaMateria))
print(f"sumamente apto {cont1}")
print(f"moderadamente apto {cont2}")
print(f"marginalmente apto {cont3}")
print(f"no apto {cont4}")

# acidez = acidez.split()
# materiaOrganica = materiaOrganica.split()
# un solo for
# for k in acidez:
#     sumaAcidez += float(k)

# for j in materiaOrganica:
#     sumaMateria += float(j)
