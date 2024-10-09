class Persona:
    def __init__(self, nombre, año, altura, ColorOjos):   
    
        self.nombre=nombre
        self.año = año
        self.altura = altura
        self.ColorOjos = ColorOjos
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {2024-self.año}." )
    def CursoCarrera(self):
        print(f"Estoy en {2024-(self.año+17)}º año de carrera")
    def Apariencia(self):
        if self.altura>175:
            print(f"Eres una persona alta, con {self.altura}cm. Pero me gusta que tengas los ojos {self.ColorOjos}")
        else: 
            print(f"Eres un retaco, con {self.altura}cm. Pero me gusta que tengas los ojos {self.ColorOjos}")


Persona1 = Persona("Lydia", 2004, 160, "Marrones")
Persona1.saludar()
Persona1.CursoCarrera()
Persona1.Apariencia()

