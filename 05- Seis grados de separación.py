import networkx as nx
import matplotlib.pyplot as plt
import random

def create_social_network(num_users, random_connections=True):
    # Crear un grafo no dirigido para la red social
    G = nx.Graph()

    # Agregar usuarios como nodos
    for i in range(1, num_users + 1):
        G.add_node(i)

    # Generar conexiones aleatorias entre usuarios
    if random_connections:
        for _ in range(num_users * 2):
            user1 = random.randint(1, num_users)
            user2 = random.randint(1, num_users)
            if user1 != user2:
                G.add_edge(user1, user2)

    # Permitir al usuario ingresar manualmente las conexiones (opcional)
    manual_input = input("¿Deseas ingresar manualmente las conexiones entre usuarios? (s/n): ")
    if manual_input.lower() == 's':
        try:
            while True:
                user1 = int(input("Ingresa el número del primer usuario (0 para finalizar): "))
                if user1 == 0:
                    break
                user2 = int(input("Ingresa el número del segundo usuario: "))
                G.add_edge(user1, user2)
        except ValueError:
            print("Por favor, ingresa números válidos.")

    return G

def simulate_experiment(G, num_pairs):
    shortest_paths = []
    for _ in range(num_pairs):
        user_origin = random.choice(list(G.nodes))
        user_dest = random.choice(list(G.nodes))
        shortest_path = nx.shortest_path(G, source=user_origin, target=user_dest)
        shortest_paths.append(len(shortest_path) - 1)  # Restamos 1 para obtener la longitud en saltos

    return shortest_paths

def visualize_social_network(G, shortest_path=None):
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_size=10, node_size=800)
    if shortest_path:
        nx.draw_networkx_edges(G, pos, edgelist=[(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)], edge_color='red', width=2)
    plt.title("Red Social")
    plt.show()

# Solicitar al usuario el número de usuarios y pares de usuarios a simular
try:
    num_users = int(input("Ingresa el número de usuarios en la red social: "))
    num_pairs = int(input("Ingresa el número de pares de usuarios a simular: "))
    social_network = create_social_network(num_users)
    shortest_paths = simulate_experiment(social_network, num_pairs)
    print(f"Distribución de longitudes de caminos más cortos: {shortest_paths}")
    visualize_social_network(social_network)
except ValueError:
    print("Por favor, ingresa números válidos.")
