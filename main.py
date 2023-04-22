#libreria para abrir aplicaciones
import subprocess
#libreria para tener tiempos de espera
from time import sleep
#archivo que contiene nuestra clase que identifica y clickea botones
from clicker import *


if __name__=='__main__':
    #llamamos a la aplicacion que queremos automatizar con subprocess, en este caso la calculadora
    print("iniciando calculadora")
    subprocess.call("calc.exe")
    sleep(5) #le damos un tiempo de espera para que inicie con normalidad
    print("iniciando clicker")
    boton1=Clicker('images/numero_1.jpg', speed=.001)#generamos la instancia que reconoce las imagenes
    #en este caso reconocerá en pantalla el boton del numero 1
    sleep(2)#esperamos otros 2 segundos por seguridad de que todo esté bien

    # boton2=Clicker('images/simbolo_mas.jpg')
    # sleep(2)
    # boton3=Clicker('images/numero_9.jpg')
    # sleep(2)
    # boton4=Clicker('images/simbolo_igual.jpg')

    clicks=10#cantidad de clicks que queremos que de nuestra automatizacion
    while clicks!=0:
        if boton1.navToImage()!=0:#si encuentra el boton en pantalla:
            clicks-=1#disminuimos la cantidad de clicks

    print ("fin de ejecucion")