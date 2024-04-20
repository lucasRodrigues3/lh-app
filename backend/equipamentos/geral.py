tipo_equipamento = ['Arma', 'Armadura', 'Defesa']
dado_max = {
    'Arma': 10,
    'Armadura': 20,
    'Defesa': 20
}
tipo_de_dado = ['d6', 'd8', 'd10', 'd12', 'd20']
tipo_raridade = {
    'Épico': ['Épico'],
    'Lendário': ['Épico', 'Lendário'],
    'Mítico': ['Épico', 'Lendário', 'Mítico']
}
raridade_por_dado = {
    'd6': 'Épico',
    'd8': 'Lendário',
    'd10': 'Lendário',
    'd12': 'Mítico',
    'd20': 'Mítico'
}
custo_dado = {
    'Arma': {
            'd6': 500,
            'd8': 800,
            'd10': 1000,
            'd12': 1500,
            'd20': 3000
        },
    'Armadura': {
        'd6': 800,
        'd8': 1000,
        'd10': 1500,
        'd12': 2000,
        'd20': 4000
    },
    'Defesa': {
        'd6': 800,
        'd8': 1000,
        'd10': 1500,
        'd12': 2000,
        'd20': 4000
    }
}
n_efeitos_por_raridade = {
    'Épico': 1,
    'Lendário': 2,
    'Mítico': 3
}
n_cargas = {
    'Épico': 10,
    'Lendário': 15,
    'Mítico': 20
}

