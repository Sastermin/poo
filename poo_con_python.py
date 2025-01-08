class Personaje:
    #atributos de la clase
    nombre = 'default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

#variable de constructor vacío de la clase
mi_personaje = Personaje()
#modificando los valores de los atributos
mi_personaje.nombre = "Dom"
mi_personaje.fuerza = 100
print("El nombre del personaje es ",mi_personaje.nombre)
print("La fuerza del personaje es ",mi_personaje.fuerza)