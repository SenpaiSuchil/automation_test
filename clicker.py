#libreria para manejar las ventanas que abramos
import pyautogui as pt

#la clase clicker es la que reconocerá a que boton queremos darle click para despues darselo
#para esto necesitamos especificar al momento de crea la instancia que boton queremos que presione
#para esto necesitamos tomar una captura de pantalla del boton y revisar su tamaño para especificar cuantos pixeles tiene que moverse
#en este caso mis capturas tienen un tamaño aproximadamente de 80 * 50, por lo tanto mis desplazamientos para situarme a la mitad
#son de 40 y 25 como se ve a continuacion en el metodo navToImage()
class Clicker:
    def __init__(self, targetImage, speed):
        #los atributos de la clase son 2 mas una variable de control
        self.targetImage=targetImage #la imagen de referencia
        self.speed=speed #la velocidad del click
        pt.FAILSAFE=True #una variable que nos posiciona en los pixeles (0,0) en caso de fallos para evitar dar clicks donde no

    def navToImage(self):
        #en un bloque try catch ubicamos el boton con nuestra imagen de referencia y le damos un rango de efectividad de 80%
        #entre mas confidence será mas preciso incluso si se obstruye parcialmente la visibilidad del boton
        #esto tambien utiliza mas cpu, asi que entre mas seguros de que no hay nada que obstruya el boton podemos bajar el condifence
        try:
            position=pt.locateOnScreen(self.targetImage, confidence=.8) #localizamos el boton
            pt.moveTo(position[0]+40, position[1]+25, duration=self.speed) #dentro del boton nos desplazamos hacia su centro
            pt.click()#hacemos click en el boton una vez pocisionados


        except:
            print("no se encontró el botón") #sino se encuentra regresamos un mensaje y 0 para terminar el ciclo
            return 0