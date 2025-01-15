class Personaje:
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        #El signo de "=" es de asignación
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        
    def atributos(self):
        print(self.__nombre)
        print("Fuerza: ", self.__fuerza)
        print("Inteligencia: ", self.__inteligencia)
        print("Defensa: ", self.__defensa)
        print("Vida: ", self.__vida)
    
    def subir_nivel(self,fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa
        
    def esta_vivo(self):
        return self.__vida > 0
    
    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
        
    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa if self.__fuerza >= self.__defensa else 0
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre) 
        if not enemigo.esta_vivo():
            enemigo.morir()
        print("Vida de ", enemigo.__nombre, "es", enemigo.__vida)
        
    def get_fuerza(self): 
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza < 0: 
            print("ERROR, haz puesto un valor negativo")        
        self.__fuerza = fuerza
        
class Guerrero(Personaje):
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #Llamar clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
Hercules = Guerrero("Hércules", 80, 50, 100, 100, 5)
Hercules.atributos()
print(Hercules.espada)

        
    
    
        
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
