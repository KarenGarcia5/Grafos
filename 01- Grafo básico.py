import networkx as nx  # Importar librería NetworkX para trabajar con grafos
import matplotlib.pyplot as plt  # Importar librería Matplotlib para crear visualizaciones

def create_shortest_path_graph(num_nodes, num_edges):  # Función para crear un grafo, encontrar y visualizar el camino más corto
    """
    Esta función crea un grafo no dirigido con la cantidad especificada de nodos y aristas,
    solicita al usuario los nodos de inicio y destino, calcula el camino más corto entre ellos
    y visualiza el grafo con el camino resaltado.

    Parámetros:
        num_nodes (int): Número de nodos en el grafo.
        num_edges (int): Número de aristas en el grafo.

    Retorno:
        None: La función no retorna un valor, solo crea y visualiza el grafo con el camino más corto.
    """

    # Crear un grafo vacío utilizando la clase Graph de NetworkX
    G = nx.Graph()

    # Agregar nodos al grafo utilizando la función add_nodes_from
    G.add_nodes_from(range(1, num_nodes + 1))  # Agregar nodos numerados del 1 al num_nodes

    # Verificar si el número de aristas es válido (no mayor que el máximo posible)
    if num_edges > num_nodes * (num_nodes - 1) / 2:
        print("El número de aristas no puede ser mayor que el máximo posible.")
        return  # Salir de la función si el número de aristas es inválido

    # Contador de aristas agregadas
    edges_added = 0

    # Recorrer los nodos para agregar aristas aleatoriamente
    for i in range(1, num_nodes + 1):
        for j in range(i + 1, num_nodes + 1):
            if edges_added < num_edges:  # Agregar arista si no se ha alcanzado el límite
                G.add_edge(i, j)
                edges_added += 1
            else:  # Si se alcanza el límite de aristas, detener el bucle interno
                break

    # Solicitar al usuario los nodos de inicio y destino
    try:
        start_node = int(input("Ingresa el nodo de inicio (1 a {}): ".format(num_nodes)))
        end_node = int(input("Ingresa el nodo de destino (1 a {}): ".format(num_nodes)))
    except ValueError:
        print("Por favor, ingresa números válidos.")
        return  # Salir de la función si la entrada no es válida

    # Calcular el camino más corto utilizando la función shortest_path de NetworkX
    shortest_path = nx.shortest_path(G, source=start_node, target=end_node)

    # Visualizar el grafo con el camino más corto resaltado
    pos = nx.spring_layout(G)  # Calcular la posición de los nodos para la visualización

    # Dibujar el grafo con etiquetas, color de nodos y tamaño
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=10, node_size=800)

    # Resaltar los nodos del camino más corto en color rojo y tamaño más grande
    nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='red', node_size=800)

    # Resaltar las aristas del camino más corto en color rojo y grosor mayor
    nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)], edge_color='red', width=2)

    # Agregar un título a la visualización del grafo
    plt.title("Grafo con Camino Más Corto")
    plt.show()  # Mostrar la figura generada

    # Imprimir el camino más corto encontrado
    print(f"Camino más corto entre nodos {start_node} y {end_node}: {shortest_path}")

# Solicitar al usuario la cantidad de nodos y aristas
try:
    num_nodes = int(input("Ingresa la cantidad de nodos en el grafo: "))
    num_edges = int(input("Ingresa la cantidad de aristas en el grafo: "))
    create_shortest_path_graph(num_nodes, num_edges)  # Llamar la función para crear el grafo y encontrar el camino más corto
except ValueError:
    print("Por favor, ingresa números válidos.")  # Manejar el error de entrada inválida

