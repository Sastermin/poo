class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        #El signo de "=" es de asignación
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        print(self.nombre)
        print("Fuerza: ", self.fuerza)
        print("Inteligencia: ", self.inteligencia)
        print("Defensa: ", self.defensa)
        print("Vida: ", self.vida)
    
    def subir_nivel(self,fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa if self.fuerza >= self.defensa else 0
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre) 
        if not enemigo.esta_vivo():
            enemigo.morir()
        print("Vida de ", enemigo.nombre, "es", enemigo.vida)
        
    def get_fuerza(self): 
        return self.fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0: 
            print("ERROR, haz puesto un valor negativo")        
        self.fuerza = fuerza
        
class Guerrero(Personaje):
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #Llamar clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
    #Pedirle al usuario escoger un arma
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Espada de plata, daño 10. (2) Espada de bronce, daño 8\n")) 
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else: 
            print("Valor incorrecto")
    
    #Sobreescribir método
    def atributos(self):
        super().atributos()
        print("Espada:",self.espada)
        
    #Sobreescribir el cálculo de daño    
    def dañar(self,enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
class Mago(Personaje):
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        #Llamar clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
        
    #Sobreescribir método
    def atributos(self):
        super().atributos()
        print("Libro:",self.libro)
        
    #Sobreescribir el cálculo de daño    
    def dañar(self,enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

Trakalosa = Personaje("La Trakalosa de Monterrey", 20, 15, 10, 100)            
Hercules = Guerrero("Hércules", 20, 15, 10, 100, 5)
Diosito = Mago("Diosito", 20, 15, 10, 100, 5)
#Imprimir atributos antes del ataque
Trakalosa.atributos()
print("**************")
Hercules.atributos()
print("**************")
Diosito.atributos()
#Ataques
Trakalosa.atacar(Hercules)
Hercules.atacar(Diosito)
Diosito.atacar(Trakalosa)
#Imprimir atributos después del atque
Trakalosa.atributos()
print("**************")
Hercules.atributos()
print("**************")
Diosito.atributos()


        
    
    
        
#variable de constructor de la clase
#mi_personaje = Personaje("Trakalosa de monterrey", 8000, 90, 50, 100)
#mi_enemigo = Personaje("La Arrolladora", 60, 90, 40, 100)
#print(mi_personaje.dañar(mi_enemigo))
#print(mi_personaje.esta_vivo())
#mi_personaje.atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()

#Prueba 4. ¿Acceso a morir?
#mi_personaje.atacar(mi_enemigo)

#Prueba 7. Getters and setters
#print(mi_personaje.get_fuerza())
#mi_personaje.set_fuerza(-100)
#print(mi_personaje.get_fuerza())
