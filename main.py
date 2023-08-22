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
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.Asiento = asientos
        self.marca = marca
        self.Motor = motor
        self.registro = registro
        
    def cantidadAsientos(self):
        numAsientos = 0
    
        if self.asientos != 0:
            for i in self.asientos:
                if isinstance(i, Asiento):
                    numAsientos = numAsientos + 1
                
        return numAsientos
    
    def verificarIntegridad(self):
        
        if (self.registro != self.Motor.registro):
            return ("Las piezas no son originales")
        
        if self.Asiento != 0:
            for i in self.Asiento:
                  if isinstance(i, Asiento):
                      if (self.registro != i.registro):
                          return ("Las piezas no son originales")
       
        return("Auto original")
        