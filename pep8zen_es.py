"""
PEP8 Style Guide Examples
"""

# Introducción
"""
En el ámbito del código,
PEP8 se erige como una sabia guía,
Aportando claridad.

La legibilidad es reina,
La consistencia es clave,
Belleza en el código.
"""

# Una Consistencia Necia es la Plaga de las Mentes Estrechas
"""
La consistencia impera,
Guiándonos a través del laberinto del código,
¡Plaga de hobgoblins, cuidado!

Sé consistente, amigo,
En estilo y espíritu,
La claridad florecerá.
"""

# Estructura del Código

# Sangría
def my_function():
    """
    La danza de la sangría,
    Alineación grácil del código,
    Armonía desplegada.
    """

def another_function():
    """
    Las líneas se inclinan respetuosamente,
    Con sangrías como su coro,
    Una sinfonía se escucha.
    """

# Tabulaciones o Espacios en Blanco
def my_function():
    """
    Los espacios, no las tabulaciones, reinan,
    Alinean el ritmo del código,
    Un deleite visual.
    """

def another_function():
    """
    Espacios, susurros suaves,
    Guiando los ojos por los pasajes del código,
    Orden en el caos.
    """

# Longitud Máxima de Línea
very_long_variable_name = some_function(
    argument1, argument2, argument3, argument4
)

long_string = (
    "Líneas que se extienden lejos,"
    "La narrativa del código se despliega,"
    "Dividido para claridad."
    )

# Líneas en Blanco
def my_function():
    """
    El código toma un respiro,
    Líneas en blanco crean pausas, paz,
    Equilibrio en movimiento.
    """

def another_function():
    """
    Silencio entre líneas,
    Las líneas descansan en los espacios en blanco,
    Una pausa en la sinfonía.
    """

# Codificación del Archivo Fuente
# No hay un ejemplo de código específico, solo una mención a la codificación, asegurando que el archivo hable el mismo idioma que tu código.

# Importaciones
import module1
import module2
import module3
import module4
import module5

# Espacios en Blanco

# Cosas que Irritan
# No hay un ejemplo de código específico, solo menciones de evitar espacios en blanco y líneas en blanco innecesarias al final de los archivos.

# Otras Recomendaciones
x = 5  # Los espacios mantienen el orden,
        Entre tokens, en control,
        Silencio en los huecos.

y = some_function(argument1, argument2)

z = another_function(argument1, argument2)


# Comentarios

# Comentarios en Línea
x = x + 1  # Incrementar x,
            Una anotación de código,
            Susurros de cambio.

y = y - 1  # Decrementar y,
            Una nota para el lector,
            La historia se despliega.

# Comentarios en Bloque
"""
Una historia sin contar,
Secretos susurrados a simple vista,
Guiando a las almas perdidas.
"""
x = 5
y = 10

"""
Una historia interna,
Líneas tejen una obra de arte, código,
Sabiduría oculta.
"""
z = x + y

# Cadenas de Documentación
def my_function():
    """
    Buscadores de conocimiento,
    Cadenas de documentación, tu luz guía,
    Secretos ahora revelados.
    """

def another_function():
    """
    Un enigma de guión,
    Cadenas de documentación, tu voz tan clara,
    Claridad otorgada.
    """

# Convenciones de Nombres

# Principio Fundamental
# No hay un ejemplo de código específico, un recordatorio eterno de elegir nombres que resuenen con claridad y comprensión.

# Descriptivo: Estilos de Nombres
# No hay un ejemplo de código específico, el viaje hacia nombres significativos y descriptivos comienza dentro de tu corazón.

# Prescriptivo: Convenciones de Nombres

## Nombres a Evitar
# No hay un ejemplo de código específico, susurros de precaución, instándote a evitar los nombres prohibidos de oscuridad y ambigüedad.

## Compatibilidad ASCII
# No hay un ejemplo de código específico, recordándote abrazar la antigua lengua ASCII para una armonía universal.

## Nombres de Paquetes y Módulos
# No hay un ejemplo de código específico, la guía para usar minúsculas con guiones bajos, forjando caminos que el código puede recorrer.

## Nombres de Clases
class MiClase:
    pass

class OtraClase:
    pass

## Nombres de Excepciones
try:
    # código que puede generar una excepción
except ValueError as e:
    # capturando valientemente la excepción, dándole un nombre que resuena con su identidad

try:
    # código que puede generar otra excepción
except KeyError as e:
    # conquistando audazmente otra excepción, armados con un nombre que revela su esencia

## Nombres de Variables Globales
CONSTANTE_GLOBAL = 42

VARIABLE_GLOBAL = "Hola, mundo!"

## Nombres de Funciones y Variables
mi_variable = 42

otra_variable = "Hola!"

def mi_funcion():
    pass

def otra_funcion():
    pass

# Argumentos de Funciones y Métodos

# Valores de Argumentos por Defecto
def mi_funcion(arg1, arg2=None):
    """
    Senderos por defecto se despliegan,
    Valores predeterminados brindan libertad,
    Argumentos abrazados.
    """
    if arg2 is None:
        arg2 = []

def otra_funcion(arg1, arg2=True, arg3=10):
    """
    Un reino de opciones,
    Los valores por defecto guían el camino,
    Versatilidad.
    """
    pass

# Argumentos con Palabras Clave y Argumentos Posicionales
def mi_funcion(arg1, arg2, *args, **kwargs):
    """
    Danza de argumentos,
    Posicionales y palabras clave se fusionan,
    Armonía en la llamada.
    """
    pass

def otra_funcion(arg1, arg2, *args, **kwargs):
    """
    Una sinfonía resuena,
    El director, tu función,
    Posicionales y palabras clave se unen.
    """
    pass

# Decoradores de Funciones y Métodos
# No hay un ejemplo de código específico, el reino de los decoradores llama, donde las funciones y métodos adquieren nuevos poderes.

# Intermedio: Estilo de Codificación
# No hay un ejemplo de código específico, un momento de descanso, contemplando el gran tapiz del estilo de código.

## Directrices y Mejores Prácticas

### Uso de la Barra Invertida
mi_cadena = (
    "A través de las líneas fluye,"
    "La barra invertida une como uno solo,"
    "El código se lee como verso."
    )

otra_cadena = (
    "Líneas conectadas,"
    "La barra invertida crea un puente,"
    "Una historia se despliega."
    )

### Cuándo Usar Comas Finales
mi_lista = [
    "item1",
    "item2",
    "item3",  # Coma final, un toque suave,
                Legibilidad en las listas,
                Crecimiento sin dolor.
]

otra_lista = [
    "item1",
    "item2",
    "item3",
]

### Acceso a Miembros Protegidos
class MiClase:
    def __init__(self):
        self._variable_protegida = 42

    def _metodo_protegido(self):
        pass

class OtraClase:
    def __init__(self):
        self._variable_protegida = 10

    def _metodo_protegido(self):
        pass

### Interfaces Públicas e Internas
class MiClase:
    def metodo_publico(self):
        pass

    def _metodo_interno(self):
        pass

class OtraClase:
    def metodo_publico(self):
        pass

    def _metodo_interno(self):
        pass

# Conclusión
"""
Abraza la gracia de PEP8,
Código como obra de arte pura,
Belleza en cada línea.
"""

# Referencias
"""
Busca más sabiduría,
Guías de los sabios y más,
El viaje del código continúa.
"""

