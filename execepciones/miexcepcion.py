"""

https://www.delftstack.com/es/howto/python/python-custom-exception/

class DemoException(Exception):
    def __init__(self, message):
        super().__init__(message)
Tenga en cuenta que para que el mensaje se integre con éxito en su excepción, llame a la clase base Exception, método __init__() e incluya el message como argumento.

Llamemos a la clase de excepción nuevamente usando la palabra clave raise, y ahora, pasando un mensaje personalizado con ella:

class DemoException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
message = "Exception Triggered! Something went wrong."
raise DemoException(message)
La salida debería verse así:

Traceback (most recent call last):
  File "/Users/demo/python/helloworld.py", line 6, in <module>
    raise DemoException(message)
__main__.DemoException: Exception Triggered! Something went wrong.
Ahora hemos creado y activado con éxito una clase de excepción con un mensaje de error personalizado.

Para situaciones reales que pueden desencadenar una excepción, ¿cómo manejamos y planteamos estas excepciones? Puede resolver este problema perfectamente implementando el manejo de excepciones usando el bloque try...except.

Ejecute el manejo de excepciones usando el bloque try...except en Python
El bloque try...except es muy parecido al bloque try-catch en otros lenguajes como Java.


El bloque try...except tiene 2 bloques principales y 2 bloques opcionales:

try (obligatorio): el bloque principal responsable de encapsular el bloque de código donde se puede activar la excepción. El bloque try detiene todo el proceso dentro de él cada vez que se activa una excepción.
except (obligatorio): el programa de bloques continúa siempre que se activa una excepción especificada. Este bloque normalmente contiene un mensaje de error descriptivo para la persona que llama o simplemente una simple declaración print(). Puede haber más de un bloque except en un solo bloque try, cada uno detectando excepciones diferentes.
else (opcional): este bloque opcional es donde el programa procederá si el bloque try no desencadenó ninguna excepción.
finally (opcional): este bloque opcional se ejecuta una vez que se ha realizado todo de los 3 bloques anteriores independientemente de si se activa una excepción o no.
Usemos el ejemplo anterior usando la clase DemoException para probar un bloque simple try...except.

Primero, envuelva la palabra clave raise en una función y colóquela dentro del bloque try...except.

La función que crearemos para este ejemplo es una función que acepta un número y lanza una excepción si envía 0. Si envía cualquier otro número, el código procederá según lo previsto. Mira el ejemplo a continuación:

class DemoException(Exception):
    def __init__(self, message):
        super().__init__(message)
        

message = "Exception Triggered! Something went wrong."

def triggerException(num):
    if (num == 0):
        raise DemoException(message)
    else:
        print(num)


try:
    triggerException(0)
    print("Code has successfully been executed.")
except DemoException:
    print("Error: Number should not be 0.")
Dado que triggerException() pasó 0 como argumento, el código debería activar DemoException. Aquí deberíamos esperar que el mensaje de palabra claveraise sea anulado con lo que esté dentro del bloque except como salida.

Observe que la línea print() después de la llamada a la función triggerException() no se emitió. Es porque la función generó una excepción; por lo tanto, detuvo inmediatamente todos los procesos dentro del bloque try y procedió directamente al bloque except.

Producción:

Error: el número no debe ser 0.
Ahora, intentemos pasar un número válido como 20, por ejemplo.

try:
    triggerException(20)
    print("Code has successfully been executed.")
except DemoException:
    print("Error: Number should not be 0.")
Producción:

20
Code has successfully been executed.
Intentemos encadenar los bloques except y creemos otra excepción. Llamemos a la nueva excepción NumberFormatException, que se activa si la entrada dada no es un número. Para esta clase de excepción, declaremos el mensaje dentro de la clase.

class NumberFormatException(Exception, value):
    message = f'{value} is not a number'
    def __init__(self):
        super().__init__(message)
Ahora, modifique el código anterior para manejar la nueva clase de excepción NumberFormatException:

class DemoException(Exception):
    def __init__(self, message):
        super().__init__(message)
        
class NumberFormatException(Exception):
    def __init__(self, message, value):
        message = f'{value} is not a number'
        super().__init__(message)
        
message = "Exception occured."

def triggerException(num):
    if (not num.isdigit()):
        raise NumberFormatException(message, num)
    elif (num == 0):
        raise DemoException(message)
    else:
        print(num)

num = "sample string"
try:
    triggerException(num)
    print("Code has successfully been executed.")
except DemoException:
    print("Error: Number should not be 0.")
except NumberFormatException:
    print(num+" is not a number.")
En este código, el valor de num que se pasó a triggerException() es una cadena 'sample string' por lo que la NumberFormatException debe activarse.

Producción:

sample string is not a number.
En resumen, crear excepciones personalizadas en Python es tan simple como crear una nueva clase, pero con la clase Exception como un argumento adicional en la definición de la clase. La palabra claveraise se utiliza para activar excepciones dada la Clase de excepción. Los bloques try...except se utilizan para envolver una o más excepciones dentro de un bloque de código y modificar lo que hace el código cuando maneja esa excepción y no solo para cerrar el programa por completo.

"""