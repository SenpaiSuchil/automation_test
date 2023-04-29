#libreria para abrir aplicaciones
import pyautogui
import subprocess
import cv2
#libreria para tener tiempos de espera
from time import sleep
#archivo que contiene nuestra clase que identifica y clickea botones
#from clicker import *
#libreria para obtener la ventana y maximizarla
import pygetwindow as gw
#libreria para manejar las ventanas que abramos
#la clase clicker es la que reconocerá a que boton queremos darle click para despues darselo
#para esto necesitamos especificar al momento de crear la instancia que boton queremos que presione
#necesitamos tomar una captura de pantalla del boton y revisar su tamaño para especificar cuantos pixeles tiene que moverse
#en este caso mis capturas tienen un tamaño aproximadamente de 80 * 50, por lo tanto mis desplazamientos para situarme a la mitad
#son de 40 y 25 como se ve a continuacion en el metodo navToImage()

def resizeImage(image):
    img = cv2.imread(image)
    newValues=pyautogui.size()
    ancho=(img.shape[1]*newValues[0])//newValues[0]
    alto=(img.shape[0]*newValues[1])//newValues[1]
    newsize=(ancho, alto)
    resized_img = cv2.resize(img, newsize)
    #cv2.imwrite("resized.jpg", resized_img)
    return resized_img

class Clicker:
    def __init__(self, targetImage, speed):
        #los atributos de la clase son 2 mas una variable de control
        self.targetImage=resizeImage(targetImage) #la imagen de referencia
        self.speed=speed #la velocidad del click
        pyautogui.FAILSAFE=True #una variable que nos posiciona en los pixeles (0,0) en caso de fallos para evitar dar clicks donde no
    def navToImage(self):
        #en un bloque try catch ubicamos el boton con nuestra imagen de referencia y le damos un rango de efectividad de 80%
        #entre mas confidence será mas preciso incluso si se obstruye parcialmente la visibilidad del boton
        #esto tambien utiliza mas cpu, asi que entre mas seguros de que no hay nada que obstruya el boton podemos bajar el condifence
        try:
            
            position=pyautogui.locateOnScreen(self.targetImage, confidence=.9) #localizamos el boton
            pyautogui.moveTo(position[0]+150, position[1]+40, duration=self.speed) #dentro del boton nos desplazamos hacia su centro
            pyautogui.click()#hacemos click en el boton una vez pocisionados
            
        except:
            print("no se encontró el botón") #sino se encuentra regresamos un mensaje y 0 para terminar el ciclo
            return 0

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ main \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

if __name__=='__main__':
    #llamamos a la aplicacion que queremos automatizar con subprocess, en este caso la calculadora
    windows=gw.getAllWindows()
    for window in windows:
        title=window.title
        if title!="":
            window.minimize()
    sleep(2)       
    print("iniciando aplicacion")
    subprocess.call("calc.exe")#aqui se llama a la aplicacion
    sleep(2) #le damos un tiempo de espera para que inicie con normalidad
    window=gw.getWindowsWithTitle('Calculadora')[0]#aqui va el nombre de la ventana
    sleep(2)
    window.activate()
    if window.isMaximized:
        pass
    else:
        window.maximize()
    sleep(5)
    print("iniciando clicker")
    boton1=Clicker('C:\\Users\\aleja\\Desktop\\automatizacion\\images\\numero_9_max.jpg', speed=.001)#generamos la instancia que reconoce las imagenes
    #en este caso reconocerá en pantalla el boton del numero 1
    sleep(2)#esperamos otros 2 segundos por seguridad de que todo esté bien
    clicks=10#cantidad de clicks que queremos que de nuestra automatizacion
    while clicks!=0:
        boton1.navToImage()
        clicks-=1#disminuimos la cantidad de clicks
    print ("fin de ejecucion")