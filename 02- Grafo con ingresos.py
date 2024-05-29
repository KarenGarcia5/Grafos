import networkx as nx  # Importar librería NetworkX para trabajar con grafos
import matplotlib.pyplot as plt  # Importar librería Matplotlib para crear visualizaciones

def create_custom_graph(num_nodes, num_edges):  # Función para crear un grafo personalizado
    """
    Esta función crea un grafo no dirigido con la cantidad especificada de nodos y aristas.

    Parámetros:
        num_nodes (int): Número de nodos en el grafo.
        num_edges (int): Número de aristas en el grafo.

    Retorno:
        None: La función no retorna un valor, solo crea y visualiza el grafo.
    """

    # Crear un grafo vacío utilizando la clase Graph de NetworkX
    G = nx.Graph()

    # Agregar nodos al grafo utilizando la función add_nodes_from
    G.add_nodes_from(range(1, num_nodes + 1))  # Agregar nodos numerados del 1 al num_nodes

    # Verificar si el número de aristas es válido
    if num_edges > num_nodes * (num_nodes - 1) / 2:
        print("El número de aristas no puede ser mayor que el máximo posible.")
        return  # Salir de la función si el número de aristas es inválido

    # Contador de aristas agregadas
    edges_added = 0

    # Recorrer los nodos para agregar aristas
    for i in range(1, num_nodes + 1):
        for j in range(i + 1, num_nodes + 1):
            if edges_added < num_edges:  # Agregar arista si no se ha alcanzado el límite
                G.add_edge(i, j)
                edges_added += 1
            else:  # Si se alcanza el límite de aristas, detener el bucle interno
                break

    # Visualizar el grafo utilizando la función draw de NetworkX
    nx.draw(G, with_labels=True, node_color='skyblue', font_size=10, node_size=800)
    plt.title("Grafo Personalizado")  # Establecer el título de la visualización
    plt.show()  # Mostrar la figura generada

    # Calcular y mostrar algunas métricas del grafo (opcional)
    print(f"Número de nodos: {G.number_of_nodes()}")
    print(f"Número de aristas: {G.number_of_edges()}")


# Solicitar al usuario la cantidad de nodos y aristas
try:
    num_nodes = int(input("Ingresa la cantidad de nodos en el grafo: "))
    num_edges = int(input("Ingresa la cantidad de aristas en el grafo: "))
    create_custom_graph(num_nodes, num_edges)  # Llamar la función para crear el grafo
except ValueError:
    print("Por favor, ingresa números válidos.")  # Manejar el error de entrada inválida
