import networkx as nx  # Importar librería NetworkX para trabajar con grafos
import matplotlib.pyplot as plt  # Importar librería Matplotlib para crear visualizaciones

def create_city_graph(num_cities, num_connections):  # Función para crear un grafo de ciudades y encontrar el camino más corto
    """
    Esta función crea un grafo no dirigido que representa ciudades y sus conexiones,
    solicita al usuario los nombres y números de las ciudades de inicio y destino,
    calcula el camino más corto entre ellas utilizando el algoritmo de Dijkstra,
    y visualiza el grafo con el camino resaltado.

    Parámetros:
        num_cities (int): Número de ciudades en el grafo.
        num_connections (int): Número de conexiones (aristas) entre las ciudades.

    Retorno:
        None: La función no retorna un valor, solo crea y visualiza el grafo con el camino más corto.
    """

    # Crear un grafo vacío no dirigido utilizando la clase Graph de NetworkX
    G = nx.Graph()

    # Agregar ciudades como nodos al grafo
    for i in range(1, num_cities + 1):
        city_name = input(f"Ingrese el nombre de la ciudad {i}: ")  # Solicitar nombre de la ciudad
        G.add_node(i, name=city_name)  # Agregar nodo con nombre y número

    # Agregar conexiones (aristas) entre ciudades
    for _ in range(num_connections):
        try:
            city1 = int(input("Ingrese el número de la primera ciudad conectada: "))  # Solicitar número de ciudad 1
            city2 = int(input("Ingrese el número de la segunda ciudad conectada: "))  # Solicitar número de ciudad 2
            G.add_edge(city1, city2)  # Agregar arista entre los nodos indicados
        except ValueError:
            print("Por favor, ingrese números válidos.")  # Manejar error de entrada inválida

    # Solicitar al usuario los números de las ciudades de inicio y destino
    try:
        start_city = int(input("Ingrese el número de la ciudad de inicio: "))  # Solicitar número de ciudad de inicio
        end_city = int(input("Ingrese el número de la ciudad de destino: "))  # Solicitar número de ciudad de destino
    except ValueError:
        print("Por favor, ingrese números válidos.")  # Manejar error de entrada inválida
        return  # Salir de la función si la entrada no es válida

    # Calcular el camino más corto utilizando el algoritmo de Dijkstra de NetworkX
    shortest_path = nx.shortest_path(G, source=start_city, target=end_city)  # Encontrar el camino más corto

    # Visualizar el grafo con el camino más corto resaltado
    pos = nx.spring_layout(G)  # Calcular la posición de los nodos para la visualización

    # Dibujar el grafo con etiquetas, color de nodos y tamaño
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=10, node_size=800)

    # Resaltar los nodos del camino más corto en color rojo y tamaño más grande
    nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='red', node_size=800)

    # Resaltar las aristas del camino más corto en color rojo y grosor mayor
    nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)], edge_color='red', width=2)

    # Agregar un título a la visualización del grafo
    plt.title("Grafo de Ciudades con Camino Más Corto")
    plt.show()  # Mostrar la figura generada

    # Obtener los nombres de las ciudades del camino más corto
    city_names = [G.nodes[node]['name'] for node in shortest_path]

    # Imprimir el camino más corto con los nombres de las ciudades
    print(f"Camino más corto entre {city_names[0]} y {city_names[-1]}: {city_names}")


# Solicitar al usuario la cantidad de ciudades y conexiones
try:
    num_cities = int(input("Ingrese la cantidad de ciudades: "))
    num_connections = int(input("Ingrese la cantidad de conexiones entre ciudades: "))
    create_city_graph(num_cities, num_connections)
except ValueError:
    print("Por favor, ingrese números válidos.")

