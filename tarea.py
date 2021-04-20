import datetime

class Tarea:
    proyecto: str
    tarea: str
    fecha: datetime
    tiempo: int

    def __init__(self, *args): 
        if len(args) == 4: 
            self.proyecto= args[0]
            self.tarea= args[1]
            self.fecha= args[2]
            self.tiempo= args[3]

        else:
            self.proyecto= ''
            self.tarea= ''
            self.fecha= datetime.date.today()
            self.tiempo= 0

   
    def imprimir(self):
        #print("Proyecto: %s -- Tarea: %s -- Tiempo: %d ", self.proyecto, self.tarea, self.tiempo)
        #return format("Proyecto: %s" + self.proyecto + " -- Tarea: " + self.tarea + " -- Fecha: " + self.fecha.day + " -- Tiempo: " + self.tiempo
        return "Proyecto: " + self.proyecto + " -- Tarea: " + self.tarea + " -- Fecha: " + str(self.fecha) + " -- Tiempo: " + str(self.tiempo)