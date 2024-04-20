import random
from collections import defaultdict

contagem_itens = defaultdict(int)

def gerar_conjunto_itens(gold_max):
    pocoes = [
        {"Nome": "Vital Potion", "Efeito": "Recupera 50 pontos de Vitalidade", "Gold": 1000},
        {"Nome": "Varied Vital Potion", "Efeito": "Recupera 50% dos pontos de Vitalidade", "Gold": 2000},
        {"Nome": "Powered Vital Potion", "Efeito": "Recupera 75% dos pontos de Vitalidade", "Gold": 2500},
        {"Nome": "Mana Potion", "Efeito": "Recupera 50 pontos de Mana", "Gold": 1500},
        {"Nome": "Super Mana Potion", "Efeito": "Recupera 100 pontos de Mana", "Gold": 2800},
        {"Nome": "Stamina Potion", "Efeito": "Recupera 50 pontos de Stamina", "Gold": 1500},
        {"Nome": "Super Stamina Potion", "Efeito": "Recupera 100 pontos de Stamina", "Gold": 2800},
        {"Nome": "Will Potion", "Efeito": "Recupera 3 pontos de FDV", "Gold": 2000},
        {"Nome": "Restoration Potion", "Efeito": "Recupera 10 pontos de FDV", "Gold": 5000}
    ]

    capsulas = [
        {"Nome": "Anti-Status Capsule", "Efeito": "Remove ou previne um Status que seria causado a você", "Gold": 2000},
        {"Nome": "Anesthesia Capsule", "Efeito": "Ignora todas as suas penalidades até o final da rodada", "Gold": 1000},
        {"Nome": "Immunity [DF] Capsule", "Efeito": "Previne o próximo [DF] que seria causado a você", "Gold": 3000},
        {"Nome": "Immunity [DM] Capsule", "Efeito": "Previne o próximo [DM] que seria causado a você", "Gold": 4000},
        {"Nome": "Immunity [DC] Capsule", "Efeito": "Previne o próximo [DC] que seria causado a você", "Gold": 5000},
        {"Nome": "Repellent Capsule", "Efeito": "Você não poderá ser alvo de criaturas (fauna ou flora) até o final da rodada", "Gold": 3000}
    ]

    runas = [
        {"Nome": "Emerald Rune", "Atributo": "FOR", "Efeito": "Modificador de +100% em seus pontos de stamina igual ao seu valor original de stamina.", "Gold": 5000},
        {"Nome": "Amethyst Rune", "Atributo": "DES", "Efeito": "Durante o final da rodada, você poderá reduzir o TDR de um de seus poderes (exceto Ultimate) em 1.", "Gold": 5000},
        {"Nome": "Ruby Rune", "Atributo": "VIG", "Efeito": "Modificador de +100% em seus pontos de vitalidade igual ao seu valor original de vitalidade.", "Gold": 5000},
        {"Nome": "Hematite Rune", "Atributo": "AGI", "Efeito": "Durante a sua fase de resolução, você terá +20% de chance de receber um turno extra.", "Gold": 5000},
        {"Nome": "Lazili Rune", "Atributo": "PER", "Efeito": "Uma vez por rodada, você pode anular um poder que tenha você como alvo.", "Gold": 5000},
        {"Nome": "Opal Rune", "Atributo": "INT", "Efeito": "Uma vez por rodada, você poderá utilizar um de seus poderes (exceto Ultimate) sem pagar seus custos.", "Gold": 5000},
        {"Nome": "Topaz Rune", "Atributo": "RAC", "Efeito": "Durante a fase de iniciativa, você receberá +1D20 e você receberá uma ação especial adicional.", "Gold": 5000},
        {"Nome": "Sapphire Rune", "Atributo": "MAG", "Efeito": "Modificador de +100% em seus pontos de mana igual ao seu valor original de mana.", "Gold": 5000}
    ]
    todos_itens = pocoes + capsulas + runas
    conjunto_itens = []
    total_gold = 0

    while total_gold < gold_max:
        escolha = random.choice([pocoes, capsulas, runas])
        item = random.choice(escolha)
        if total_gold + item['Gold'] <= gold_max:
            conjunto_itens.append(item)
            total_gold += item['Gold']
        else:
            break

    troco = gold_max - total_gold

    for item in conjunto_itens:
        nome = item['Nome']
        contagem_itens[nome] += 1

    for nome, quantidade in contagem_itens.items():
        print(f'{nome}: {quantidade}')
        item = [i for i in todos_itens if i['Nome'] == nome][0]
        print(item['Efeito'])
        if 'Atributo' in item:
            print(item['Atributo'])
            for i in range(quantidade):
                print(f'Runa {i+1}: Slot ({random.randint(1, 5)})')
                print(f'Dados adicionais: {random.randint(1, 3)}')
        print(item['Gold'])
        print()

    print('-------------------------------------------------------------------------------')
    print()
    print("Gold restante:", troco)

if __name__ == "__main__":
    gerar_conjunto_itens(100000)

