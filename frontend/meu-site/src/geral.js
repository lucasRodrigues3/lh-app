export default {
    tipoEquipamento : ['Arma', 'Armadura', 'Defesa'],
    dadoMax : {
        'Arma': 10,
        'Armadura': 20,
        'Defesa': 20
    },
    tipoDeDado : ['d6', 'd8', 'd10', 'd12', 'd20'],
    tipoRaridade : {
        'Épico': ['Épico'],
        'Lendário': ['Épico', 'Lendário'],
        'Mítico': ['Épico', 'Lendário', 'Mítico']
    },
    raridadePorDado : {
        'd6': 'Épico',
        'd8': 'Lendário',
        'd10': 'Lendário',
        'd12': 'Mítico',
        'd20': 'Mítico'
    },
    custoDado : {
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
    },
    nEfeitosPorRaridade : {
        'Épico': 1,
        'Lendário': 2,
        'Mítico': 3
    },
    nCargas : {
        'Épico': 10,
        'Lendário': 15,
        'Mítico': 20
    },
};