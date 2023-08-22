class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        
    def cambiarColor(self, color):
        if (color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco"):
            self.color = str(color)

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        self.registro = int(registro)
        
    def asignarTipo(self,tipo):
        if (tipo == "electrico" or tipo == "gasolina"):
            self.tipo = str(tipo)
        
class Auto:
    cantidadCreados = "0"
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.Asiento = asientos [""]
        self.marca = marca
        self.Motor = motor
        self.registro = registro
        
    def cantidadAsientos(self):
        numAsientos = 0
        asientos = [Asiento(self)]
        for i in range(len(asientos)):
            
             if asientos[i] != 0 or asientos[i] != None:
                 count =+1
                 
        return count
    
    def verificarIntegridad(self):
        
        if (Auto(self).registro == Motor(self).registro):
            asientos = [Asiento(self)]
            for i in range(len(asientos)):
            
             if asientos[i] != 0 or asientos[i] != None:
                 if asientos[i] != Auto(self).registro:
                     return ("Las piezas no son originales")
        else:
            return("Las piezas no son originales")
        
        return("Auto original")
        