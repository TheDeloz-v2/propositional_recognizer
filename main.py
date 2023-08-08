from lexer import lexer
from syntax import parser

# Importe de Matplotlib y Networkx para realizar el gráfico de un grafo dirigido de la expresión
# que reconozca en YACC
import matplotlib.pyplot as plt
import networkx as nx

# Lista de expresiones a evaluar
expressions = [
    '(p=>q)^p',
    'p',
    '~~~q',
    '(p^q)',
    '(0=>(ros))',
    '~(p^q)',
    '(p<=>~p)',
    '((p=>q)^p)',
    '(~(p^(qor))os)'
]

# Lista de resultado
results = []

# Evaluar cada expresion
for expression in expressions:
    lexer.input(expression)
    result = parser.parse(expression, lexer=lexer)
    results.append(result)
    
# Imprimir resultados
for i in range(len(expressions)):
    print('Expresion '+str(i+1)+':')
    print(f'{expressions[i]} =\n {results[i]}')
    print()
    
# Resultados esperados de separacion de expresiones
# (p=>q)^p = ('^', ('=>', 'p', 'q'), 'p')
# p = 'p'
# ~~~q = ('~', ('~', ('~', 'q')))
# (p^q) = ('^', 'p', 'q')
# (0=>(ros)) = ('=>', '0', ('o', 'r', 's'))
# ~(p^q) = ('~', ('^', 'p', 'q'))
# (p<=>~p) = ('<=>', 'p', ('~', 'p'))
# ((p=>q)^p) = ('^', ('=>', 'p', 'q'), 'p')
# (~(p^(qor))os) = ('~', ('o', ('^', 'p', ('o', 'q', 'r')), 's'))


# Generacion de grafo dirigido en base a nodos de Syntax.py
# Se utiliza la libreria networkx para la generacion del grafo
# Se utiliza la libreria matplotlib para la visualizacion del grafo

# Funcion para generar el grafo dirigido
def graph_tree(tree):
    G = nx.DiGraph()
    G.add_node(tree.id, label=tree.label)
    for child in tree.children:
        child_G = graph_tree(child)
        G = nx.compose(G, child_G)
        G.add_edge(tree.id, child.id)
    return G

# Generar grafo dirigido para cada expresion
for i, result in enumerate(results):
    G = graph_tree(result)
    labels = nx.get_node_attributes(G, 'label')
    
    # Asignar capas a los nodos
    for layer, nodes in enumerate(reversed(tuple(nx.topological_generations(G)))):
        for node in nodes:
            G.nodes[node]["layer"] = layer

    pos = nx.multipartite_layout(G, subset_key="layer", align='horizontal')

    fig, ax = plt.subplots(figsize=(4, 6))
    nx.draw_networkx_nodes(G, pos, node_size=1200, node_color='white', edgecolors='black')
    nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=35, edge_color='black')
    nx.draw_networkx_labels(G, pos, labels, font_size=15)
    ax.set_title(expressions[i], fontsize=20)
    fig.tight_layout()
    
    # Guardar grafo dirigido en carpeta graphs
    dir = 'grafos/'
    plt.savefig(f'{dir}grafo-{i}.png')
    plt.close()