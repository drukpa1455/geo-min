import numpy as np  # Importar la biblioteca NumPy

# Estructura del árbol
# ------------------------------------------
árbol = {
    'A': np.array(['B', 'C']),  # El nodo A tiene como hijos a B y C
    'B': np.array(['D', 'E']),  # El nodo B tiene como hijos a D y E
    'C': np.array(['F', 'G']),  # El nodo C tiene como hijos a F y G
    'D': np.array(['H', 'I']),  # El nodo D tiene como hijos a H y I
    'E': np.array([]),  # El nodo E no tiene hijos
    'F': np.array([]),  # El nodo F no tiene hijos
    'G': np.array([]),  # El nodo G no tiene hijos
    'H': np.array([]),  # El nodo H no tiene hijos
    'I': np.array([])   # El nodo I no tiene hijos
}

# Búsqueda en profundidad (DFS)
# ------------------------------------------
def dfs(nodo):
    """
    Realiza una búsqueda en profundidad (DFS) en el árbol a partir del nodo dado.

    Args:
        nodo (str): El nodo inicial para DFS.

    Returns:
        None
    """
    if nodo is None:
        return  # Salir de la recursión actual si el nodo es None
    print("Nodo visitado:", nodo)  # Imprimir el nodo actual que se está visitando
    hijos = árbol.get(nodo, np.array([]))  # Obtener los hijos del nodo actual desde el diccionario árbol
    for hijo in hijos:
        dfs(hijo)

# Búsqueda en anchura (BFS)
# ------------------------------------------
def bfs(raíz):
    """
    Realiza una búsqueda en anchura (BFS) en el árbol a partir del nodo raíz dado.

    Args:
        raíz (str): El nodo raíz para BFS.

    Returns:
        None
    """
    cola = [raíz]  # Inicializar una cola con el nodo raíz

    while cola:
        nodo = cola.pop(0)  # Obtener el nodo del frente de la cola
        print("Nodo visitado:", nodo)  # Imprimir el nodo visitado

        hijos = árbol.get(nodo, np.array([]))  # Obtener los hijos del nodo actual
        cola.extend(hijos)  # Agregar los hijos al final de la cola para su exploración

# Búsqueda de costo uniforme (UCS)
# ------------------------------------------
def ucs(raíz):
    """
    Realiza una búsqueda de costo uniforme (UCS) en el árbol a partir del nodo raíz dado.

    Args:
        raíz (str): El nodo raíz para UCS.

    Returns:
        None
    """
    cola = [(0, raíz)]  # Inicializar una cola de prioridad con el nodo raíz y su costo
    while cola:
        costo, nodo = cola.pop(0)  # Obtener el nodo con el costo mínimo del frente de la cola
        print("Nodo visitado:", nodo)  # Imprimir el nodo visitado
        hijos = árbol.get(nodo, np.array([]))  # Obtener los hijos del nodo actual
        cola.extend([(costo + 1, hijo) for hijo in hijos])  # Agregar los hijos a la cola con los costos actualizados

# Búsqueda en profundidad iterativa (IDDFS)
# ------------------------------------------
def iddfs(raíz, límite_profundidad):
    """
    Realiza una búsqueda en profundidad iterativa (IDDFS) en el árbol a partir del nodo raíz dado.

    Args:
        raíz (str): El nodo raíz para IDDFS.
        límite_profundidad (int): La profundidad máxima a explorar.

    Returns:
        None
    """
    for profundidad in range(límite_profundidad + 1):  # Iterar sobre los límites de profundidad desde 0 hasta el límite especificado
        if dfs_límite(raíz, profundidad):  # Llamar a una función auxiliar para realizar DFS con un límite de profundidad
            return

def dfs_límite(nodo, profundidad):
    """
    Función auxiliar para IDDFS que realiza DFS con un límite de profundidad.

    Args:
        nodo (str): El nodo actual.
        profundidad (int): El límite de profundidad restante.

    Returns:
        bool: True si se encuentra el nodo objetivo dentro del límite de profundidad, False en caso contrario.
    """
    if profundidad == 0:  # Si se alcanza el límite de profundidad
        print("Nodo visitado:", nodo)  # Imprimir el nodo visitado
        return True
    hijos = árbol.get(nodo, np.array([]))  # Obtener los hijos del nodo actual
    for hijo in hijos:
        if dfs_límite(hijo, profundidad - 1):  # Llamar recursivamente a la función auxiliar con el nodo hijo y el límite de profundidad reducido
            return True
    return False

# Búsqueda A*
# ------------------------------------------
def astar(raíz, heurística):
    """
    Realiza una búsqueda A* en el árbol a partir del nodo raíz dado utilizando la función heurística especificada.

    Args:
        raíz (str): El nodo raíz para la búsqueda A*.
        heurística (dict): La función heurística que estima el costo desde cada nodo hasta el nodo objetivo.

    Returns:
        None
    """
    lista_abierta = [(heurística[raíz], 0, raíz)]  # Inicializar una lista de prioridad con el nodo raíz, su costo y valor heurístico
    lista_cerrada = set()  # Inicializar un conjunto para almacenar los nodos visitados
    while lista_abierta:
        _, costo, nodo = min(lista_abierta)  # Obtener el nodo con el costo combinado mínimo y valor heurístico
        lista_abierta.remove((heurística[nodo], costo, nodo))  # Eliminar el nodo de la lista abierta
        lista_cerrada.add(nodo)  # Agregar el nodo a la lista cerrada
        print("Nodo visitado:", nodo)  # Imprimir el nodo visitado
        if nodo == meta:  # Si se encuentra el nodo objetivo
            return
        hijos = árbol.get(nodo, np.array([]))  # Obtener los hijos del nodo actual
        for hijo in hijos:
            if hijo not in lista_cerrada:  # Si el nodo hijo no ha sido visitado
                g = costo + 1  # Incrementar el costo en 1
                h = heurística[hijo]  # Obtener el valor heurístico para el nodo hijo
                f = g + h  # Calcular el costo combinado y el valor heurístico
                lista_abierta.append((f, g, hijo))  # Agregar el nodo hijo a la lista abierta con los valores actualizados

# Búsqueda del mejor primer nodo
# ------------------------------------------
def best_first(raíz, heurística):
    """
    Realiza una búsqueda del mejor primer nodo en el árbol a partir del nodo raíz dado utilizando la función heurística especificada.

    Args:
        raíz (str): El nodo raíz para la búsqueda del mejor primer nodo.
        heurística (dict): La función heurística que estima la deseabilidad de cada nodo.

    Returns:
        None
    """
    lista_abierta = [(heurística[raíz], raíz)]  # Inicializar una lista de prioridad con el nodo raíz y su valor heurístico
    lista_cerrada = set()  # Inicializar un conjunto para almacenar los nodos visitados
    while lista_abierta:
        _, nodo = min(lista_abierta)  # Obtener el nodo con el valor heurístico mínimo
        lista_abierta.remove((heurística[nodo], nodo))  # Eliminar el nodo de la lista abierta
        lista_cerrada.add(nodo)  # Agregar el nodo a la lista cerrada
        print("Nodo visitado:", nodo)  # Imprimir el nodo visitado
        if nodo == meta:  # Si se encuentra el nodo objetivo
            return
        hijos = árbol.get(nodo, np.array([]))  # Obtener los hijos del nodo actual
        for hijo in hijos:
            if hijo not in lista_cerrada:  # Si el nodo hijo no ha sido visitado
                lista_abierta.append((heurística[hijo], hijo))  # Agregar el nodo hijo a la lista abierta

# Búsqueda codiciosa
# ------------------------------------------
def greedy(raíz, heurística):
    """
    Realiza una búsqueda codiciosa en el árbol a partir del nodo raíz dado utilizando la función heurística especificada.

    Args:
        raíz (str): El nodo raíz para la búsqueda codiciosa.
        heurística (dict): La función heurística que estima la deseabilidad de cada nodo.

    Returns:
        None
    """
    cola = [(heurística[raíz], raíz)]  # Inicializar una cola de prioridad con el nodo raíz y su valor heurístico
    while cola:
        _, nodo = min(cola)  # Obtener el nodo con el valor heurístico mínimo
        cola.remove((heurística[nodo], nodo))  # Eliminar el nodo de la cola
        print("Nodo visitado:", nodo)  # Imprimir el nodo visitado
        if nodo == meta:  # Si se encuentra el nodo objetivo
            return
        hijos = árbol.get(nodo, np.array([]))  # Obtener los hijos del nodo actual
        cola.extend([(heurística[hijo], hijo) for hijo in hijos])  # Agregar los hijos a la cola

# Minimax
# ------------------------------------------
class NodoMinimax:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def minimax(nodo, jugador_maximizador):
    """
    Realiza el algoritmo Minimax en el árbol a partir del nodo dado.

    Args:
        nodo (NodoMinimax): El nodo actual.
        jugador_maximizador (bool): True si el jugador actual es maximizador, False en caso contrario.

    Returns:
        int: El valor óptimo.
    """
    if len(nodo.hijos) == 0:  # Si el nodo actual es un nodo hoja
        return nodo.valor
    if jugador_maximizador:  # Si el jugador actual es maximizador
        valor_max = -np.inf
        for hijo in nodo.hijos:
            valor = minimax(hijo, False)  # Llamar recursivamente al algoritmo con el nodo hijo y establecer el jugador maximizador en False
            valor_max = max(valor_max, valor)  # Actualizar el valor máximo
        return valor_max
    else:  # Si el jugador actual es minimizador
        valor_min = np.inf
        for hijo in nodo.hijos:
            valor = minimax(hijo, True)  # Llamar recursivamente al algoritmo con el nodo hijo y establecer el jugador maximizador en True
            valor_min = min(valor_min, valor)  # Actualizar el valor mínimo
        return valor_min

def construir_árbol_minimax():
    """
    Construye un árbol de muestra para el algoritmo Minimax.

    Returns:
        NodoMinimax: El nodo raíz del árbol.
    """
    raíz = NodoMinimax(3)
    hijo1 = NodoMinimax(5)
    hijo2 = NodoMinimax(2)
    hijo3 = NodoMinimax(9)
    hijo4 = NodoMinimax(8)
    hijo5 = NodoMinimax(1)
    raíz.hijos = [hijo1, hijo2]
    hijo1.hijos = [hijo3, hijo4]
    hijo2.hijos = [hijo5]
    return raíz

# Poda Alfa-Beta
# ------------------------------------------
class NodoAlphaBeta:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def alphabeta(nodo, alfa, beta, jugador_maximizador):
    """
    Realiza el algoritmo de Poda Alfa-Beta en el árbol a partir del nodo dado.

    Args:
        nodo (NodoAlphaBeta): El nodo actual.
        alfa (float): El valor actual de alfa.
        beta (float): El valor actual de beta.
        jugador_maximizador (bool): True si el jugador actual es maximizador, False en caso contrario.

    Returns:
        int: El valor óptimo.
    """
    if len(nodo.hijos) == 0:  # Si el nodo actual es un nodo hoja
        return nodo.valor
    if jugador_maximizador:  # Si el jugador actual es maximizador
        valor = -np.inf
        for hijo in nodo.hijos:
            valor = max(valor, alphabeta(hijo, alfa, beta, False))  # Llamar recursivamente al algoritmo con el nodo hijo y establecer el jugador maximizador en False
            alfa = max(alfa, valor)  # Actualizar el valor de alfa
            if alfa >= beta:  # Realizar la poda alfa-beta
                break
        return valor
    else:  # Si el jugador actual es minimizador
        valor = np.inf
        for hijo in nodo.hijos:
            valor = min(valor, alphabeta(hijo, alfa, beta, True))  # Llamar recursivamente al algoritmo con el nodo hijo y establecer el jugador maximizador en True
            beta = min(beta, valor)  # Actualizar el valor de beta
            if alfa >= beta:  # Realizar la poda alfa-beta
                break
        return valor

def construir_árbol_alphabeta():
    """
    Construye un árbol de muestra para el algoritmo de Poda Alfa-Beta.

    Returns:
        NodoAlphaBeta: El nodo raíz del árbol.
    """
    raíz = NodoAlphaBeta(3)
    hijo1 = NodoAlphaBeta(5)
    hijo2 = NodoAlphaBeta(2)
    hijo3 = NodoAlphaBeta(9)
    hijo4 = NodoAlphaBeta(8)
    hijo5 = NodoAlphaBeta(1)
    raíz.hijos = [hijo1, hijo2]
    hijo1.hijos = [hijo3, hijo4]
    hijo2.hijos = [hijo5]
    return raíz

# Búsqueda en el árbol de Monte Carlo (MCTS)
# ------------------------------------------
class NodoMCTS:
    def __init__(self, nombre):
        self.nombre = nombre
        self.visitas = 0
        self.recompensa = 0
        self.hijos = []

def mcts(nodo, simulaciones):
    """
    Realiza el algoritmo de Búsqueda en el árbol de Monte Carlo (MCTS) a partir del nodo dado.

    Args:
        nodo (NodoMCTS): El nodo raíz del árbol.
        simulaciones (int): El número de simulaciones a realizar.

    Returns:
        None
    """
    for _ in range(simulaciones):
        nodo_actual = seleccionar_nodo(nodo)
        recompensa = simular(nodo_actual)
        retroceder(nodo_actual, recompensa)

def seleccionar_nodo(nodo):
    """
    Selecciona el siguiente nodo para explorar en el algoritmo MCTS utilizando la política UCB1.

    Args:
        nodo (NodoMCTS): El nodo actual.

    Returns:
        NodoMCTS: El siguiente nodo a explorar.
    """
    while nodo.hijos:
        if all(hijo.visitas > 0 for hijo in nodo.hijos):
            c = 1.4  # Parámetro de exploración
            ucb1_values = [hijo.recompensa / hijo.visitas + c * np.sqrt(np.log(nodo.visitas) / hijo.visitas) for hijo in nodo.hijos]
            índice = np.argmax(ucb1_values)
            nodo = nodo.hijos[índice]
        else:
            return expandir_nodo(nodo)
    return nodo

def expandir_nodo(nodo):
    """
    Expande un nodo seleccionando un hijo no visitado al azar.

    Args:
        nodo (NodoMCTS): El nodo actual.

    Returns:
        NodoMCTS: El nodo hijo seleccionado.
    """
    hijos_no_visitados = [hijo for hijo in nodo.hijos if hijo.visitas == 0]
    hijo_seleccionado = np.random.choice(hijos_no_visitados)
    return hijo_seleccionado

def simular(nodo):
    """
    Simula un juego aleatorio a partir del nodo dado y devuelve la recompensa obtenida.

    Args:
        nodo (NodoMCTS): El nodo actual.

    Returns:
        int: La recompensa obtenida en la simulación.
    """
    recompensa = jugar_juego(nodo)
    return recompensa

def jugar_juego(nodo):
    """
    Juega un juego aleatorio a partir del nodo dado y devuelve la recompensa obtenida.

    Args:
        nodo (NodoMCTS): El nodo actual.

    Returns:
        int: La recompensa obtenida en el juego.
    """
    # Lógica del juego
    return np.random.randint(0, 10)  # Seleccionar una recompensa aleatoria entre 0 y 9

def retroceder(nodo, recompensa):
    """
    Retrocede a lo largo del camino tomado y actualiza las estadísticas de visitas y recompensas.

    Args:
        nodo (NodoMCTS): El nodo actual.
        recompensa (int): La recompensa obtenida en la simulación.

    Returns:
        None
    """
    while nodo:
        nodo.visitas += 1
        nodo.recompensa += recompensa
        nodo = nodo.padre

def construir_árbol_mcts():
    """
    Construye un árbol de muestra para el algoritmo de Búsqueda en el árbol de Monte Carlo (MCTS).

    Returns:
        NodoMCTS: El nodo raíz del árbol.
    """
    raíz = NodoMCTS('A')
    hijo1 = NodoMCTS('B')
    hijo2 = NodoMCTS('C')
    hijo3 = NodoMCTS('D')
    hijo4 = NodoMCTS('E')
    hijo5 = NodoMCTS('F')
    hijo6 = NodoMCTS('G')
    hijo7 = NodoMCTS('H')
    hijo8 = NodoMCTS('I')
    raíz.hijos = [hijo1, hijo2, hijo3]
    hijo1.hijos = [hijo4, hijo5]
    hijo2.hijos = [hijo6]
    hijo3.hijos = [hijo7, hijo8]
    return raíz

# Ejemplo de uso
# ------------------------------------------
raíz = 'A'  # El nodo de inicio
meta = 'I'  # El nodo objetivo

print("Búsqueda en profundidad (DFS):")
dfs(raíz)  # Realizar DFS a partir del nodo raíz

print("\nBúsqueda en anchura (BFS):")
bfs(raíz)  # Realizar BFS a partir del nodo raíz

print("\nBúsqueda de costo uniforme (UCS):")
ucs(raíz)  # Realizar UCS a partir del nodo raíz

print("\nBúsqueda en profundidad iterativa (IDDFS):")
iddfs(raíz, 3)  # Realizar IDDFS a partir del nodo raíz con un límite de profundidad de 3

print("\nBúsqueda A*:")
heurística = {
    'A': 6,
    'B': 5,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 3,
    'G': 4,
    'H': 1,
    'I': 0
}  # Función heurística que estima el costo desde cada nodo hasta el nodo objetivo
astar(raíz, heurística)  # Realizar búsqueda A* a partir del nodo raíz con la función heurística especificada

print("\nBúsqueda del mejor primer nodo:")
best_first(raíz, heurística)  # Realizar búsqueda del mejor primer nodo a partir del nodo raíz con la función heurística especificada

print("\nBúsqueda codiciosa:")
greedy(raíz, heurística)  # Realizar búsqueda codiciosa a partir del nodo raíz con la función heurística especificada

print("\nMinimax:")
árbol_minimax = construir_árbol_minimax()  # Construir un árbol de muestra para el algoritmo Minimax
resultado = minimax(árbol_minimax, True)  # Realizar Minimax a partir del nodo raíz con el jugador maximizador establecido en True
print("Valor óptimo:", resultado)  # Imprimir el valor óptimo determinado por el algoritmo Minimax

print("\nPoda Alfa-Beta:")
árbol_alphabeta = construir_árbol_alphabeta()  # Construir un árbol de muestra para el algoritmo de poda Alfa-Beta
resultado = alphabeta(árbol_alphabeta, -np.inf, np.inf, True)  # Realizar poda Alfa-Beta a partir del nodo raíz con los valores alfa y beta iniciales
print("Valor óptimo:", resultado)  # Imprimir el valor óptimo determinado por el algoritmo de poda Alfa-Beta

print("\nBúsqueda en el árbol de Monte Carlo (MCTS):")
árbol_mcts = construir_árbol_mcts()  # Construir un árbol de muestra para el algoritmo de búsqueda en el árbol de Monte Carlo (MCTS)
mcts(árbol_mcts, 1000)  # Realizar MCTS a partir del nodo raíz con 1000 simulaciones
mejor_hijo = max(árbol_mcts.hijos, key=lambda hijo: hijo.visitas)  # Seleccionar el nodo hijo con el máximo número de visitas
print("Mejor nodo hijo:", mejor_hijo.nombre)  # Imprimir el nombre del mejor nodo hijo según el algoritmo MCTS
