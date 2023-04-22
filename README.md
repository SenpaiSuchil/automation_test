# test de automatizacion para ventanas

El codigo tiene como intención identificar botones dentro de una interfaz para despues hacer click en ellos.
de manera general podemos ver dos archivos y una carpeta:
- _main.py_ que es el archivo principal que ejecuta el codigo
- _clicker.py_ que contiene la clase que nos ayudará a identificar botones y clickearlos que será llamada en el main
- _images_ que es un directorio donde se encuentran las imagenes de referencia

## clicker.py
la clase clicker es la que reconocerá a que boton queremos darle click para despues darselo,
para esto necesitamos 
- especificar al momento de crear la instancia que boton queremos que presione
- necesitamos tomar una captura de pantalla del boton y revisar su tamaño para especificar cuantos pixeles tiene que moverse

en este caso mis capturas tienen un tamaño aproximadamente de 80 * 50, por lo tanto mis desplazamientos para situarme a la mitad
son de 40 y 25 como se ve a continuacion en el metodo navToImage()

para explicar mas a detalle veamos el codigo:

- Inclusión de liberias:
  en este archivo necesitamos solo pyautogui para manejar los clicks en las ventanas.  
  mencionar que tambien es requerido instalar opencv.
  
    - ```python
        import pyautogui as pt
      ```

- Declaración de la clase y constructor:   
    En esta parte delaramos la clase, le damos parametros de entrada y los igualamos a atributos de la clase misma para que sean reconocidos por sus metodos.  
    tambien tenemos una variable de control que nos ayudará a posicionarnos en la coordenada (0,0) de neustra pantalla en caso de errores durante la ejecución.
    todo esto para no clickear en alguna aprte sin querer.  
  - ```python
    class Clicker:
    def __init__(self, targetImage, speed):
        self.targetImage=targetImage 
        self.speed=speed
        pt.FAILSAFE=True
    ```
- Metodo navToImage( ):
    en un bloque try catch ubicamos el boton con nuestra imagen de referencia y le damos un rango de efectividad de 80%.  
    entre mas confidence será mas preciso incluso si se obstruye parcialmente la visibilidad del boton.  
    esto tambien utiliza mas cpu, asi que entre mas seguros de que no hay nada que obstruya el boton podemos bajar el condifence.  
    
  - ```python
        def navToImage(self):
        try:
            position=pt.locateOnScreen(self.targetImage, confidence=.8)
            pt.moveTo(position[0]+40, position[1]+25, duration=self.speed)
            pt.click()
        except:
            print("no se encontró el botón")
            return 0
    ```  
    en esta parte del codigo localizamos el boton con la funcion locateOnScreen( ), a la cual le proporcionamos una imagen de referencia.  
    una vez encontrada el boton con respecto a la imagen de refencia, hacemos un desplazamiento con moveTo( ) dependiendo del tamaño de la imagen como se menciona arriba.  
    despues de esto damos click con la funcion click( ).  
    todo esto dentro del bloque try catch.  
## main.py
main.py es el archivo que ejecuta toda la secuencia de automatización, para ello necesitamos de dos librerias e incluir el archivo clicker.py.  
  - ```python
        import subprocess
        from time import sleep
        from clicker import *
    ```
    
- Ejecución del codigo  
  esto es relativamente sencillo:
  - lo primero que tenemos que hacer es llamar con _subprocess_ a la aplicación que queremos abrir.
  - despues necesitamos inicializar el objeto clicker pasandole una imagen de nuestro directorio _images_ y una velocidad de click
  - establecemos una cantidad de clicks que queremos que nuestro programa dé durante la ejecución
  todo esto siempre con la funcion sleep() de por medio para que las aplicaciones e instancias tengan tiempo suficiente de abrirse
   - ```python
        if __name__=='__main__':
            print("iniciando calculadora")
            subprocess.call("calc.exe")
            sleep(5)
            print("iniciando clicker")
            boton1=Clicker('images/numero_1.jpg', speed=.001)
            sleep(2)
     ```
  despues de esto necesitamos generar un ciclo controlado por la cantidad de clicks y con un if que llamará al metodo navToImage( ) para saber si se encontró la imagen o no dentro de la pantalla.  
  para esto dentro de nuestro bloque try catch en nuestro metodo navToImage tenemos declarado que regrese 0 en caso de no encontrar el boton en la pantalla.  
  y para finalizar un simple mensaje a manera de notificación sobre el final de nuestra ejecución.
    - ```python
         clicks=10
         while clicks!=0:
            if boton1.navToImage()!=0:
              clicks-=1
         print ("fin de ejecucion")
      ``` 
  
