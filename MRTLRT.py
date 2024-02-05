import networkx as nx
LRTMRT = {
    'Baclaran': {'EDSA'},
    'EDSA': {'Baclaran', 'Libertad', 'Taft Avenue'},
    'Libertad': {'EDSA', 'Gil Puyat'},
    'Gil Puyat': {'Libertad', 'Vito Cruz'},
    'Vito Cruz': {'Gil Puyat', 'Quirino'},
    'Quirino': {'Vito Cruz', 'Pedro Gil'},
    'Pedro Gil': {'Quirino', 'UN Avenue'},
    'UN Avenue': {'Pedro Gil', 'Central Terminal'},
    'Central Terminal': {'UN Avenue', 'Carriedo'},
    'Carriedo': {'Central Terminal', 'Doroteo Jose'},
    'Doroteo Jose': {'Carriedo', 'Bambang', 'Recto'},
    'Bambang': {'Doroteo Jose', 'Tayuman'},
    'Tayuman': {'Bambang', 'Blumentritt'},
    'Blumentritt': {'Tayuman', 'Abad Santos'},
    'Abad Santos': {'Blumentritt', 'R. Papa'},
    'R. Papa': {'Abad Santos', '5th Avenue'},
    '5th Avenue': {'R. Papa', 'Monumento'},
    'Monumento': {'5th Avenue', 'Balintawak'},
    'Balintawak': {'Monumento', 'Fernando Poe Jr.'},
    'Fernando Poe Jr.': {'Balintawak', 'North Avenue'},
    
    'Recto': {'Legarda', 'Doroteo Jose'},
    'Legarda': {'Recto', 'Pureza'},
    'Pureza': {'Legarda', 'V. Mapa'},
    'V. Mapa': {'Pureza', 'J. Ruiz'},
    'J. Ruiz': {'V. Mapa', 'Gilmore'},
    'Gilmore': {'J. Ruiz', 'Betty Go-Belmonte'},
    'Betty Go-Belmonte': {'Gilmore', 'Araneta Center-Cubao'},
    'Anonas': {'Araneta Center-Cubao', 'Katipunan'},
    'Katipunan': {'Anonas', 'Santolan'},
    'Santolan': {'Katipunan', 'Marikina-Pasig'},
    'Marikina-Pasig': {'Santolan', 'Antipolo'},
    'Antipolo': {'Marikina-Pasig'},

    'North Avenue': {'Quezon Avenue', 'Fernando Poe Jr.'},
    'Quezon Avenue': {'North Avenue', 'GMA Kamuning'},
    'GMA Kamuning': {'Quezon Avenue', 'Araneta Center-Cubao'},
    'Araneta Center-Cubao': {'GMA Kamuning', 'Santolan-Annapolis', 'Betty Go-Belmonte', 'Anonas'},
    'Santolan-Annapolis': {'Araneta Center-Cubao', 'Ortigas Avenue'},
    'Ortigas Avenue': {'Santolan-Annapolis', 'Shaw Boulevard'},
    'Shaw Boulevard': {'Ortigas Avenue', 'Boni Avenue'},
    'Boni Avenue': {'Shaw Boulevard', 'Guadalupe'},
    'Guadalupe': {'Boni Avenue', 'Buendia'},
    'Buendia': {'Guadalupe', 'Ayala'},
    'Ayala': {'Buendia', 'Magallanes'},
    'Magallanes': {'Ayala', 'Taft Avenue'},
    'Taft Avenue': {'Magallanes', 'EDSA'}
}

stations = sorted(list(set(LRTMRT.keys())))

def find_shortest_path(graph, source, target):
    G = nx.Graph(graph)
    try:
        shortest_path = nx.shortest_path(G, source=source, target=target)
        return shortest_path
    except nx.NetworkXNoPath:
        return None