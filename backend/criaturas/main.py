import random

def dropar_gold(rank, bonus):
    ranks = [
        {'rank': 'E', 'gold_min': 1000, 'gold_max': 5000},
        {'rank': 'D', 'gold_min': 5000, 'gold_max': 10000},
        {'rank': 'C', 'gold_min': 10000, 'gold_max': 30000},
        {'rank': 'B', 'gold_min': 30000, 'gold_max': 60000},
        {'rank': 'A', 'gold_min': 60000, 'gold_max': 100000},
        {'rank': 'S', 'gold_min': 100000, 'gold_max': 250000},
        {'rank': 'SS', 'gold_min': 250000, 'gold_max': 500000},
        {'rank': 'SSS', 'gold_min': 500000, 'gold_max': 1000000},
    ]

    rank_escolhido = [r for r in ranks if r['rank'] == rank][0]
    valor_min = rank_escolhido['gold_min'] // 1000
    valor_max = rank_escolhido['gold_max'] // 1000

    gold_dropado = random.randint(valor_min, valor_max) * 1000
    if bonus:
        gold_dropado *= 2

    print()
    print('Gold Dropado', gold_dropado)
    print()
    print('-------------------------------------------------------------------------------')
    print()
    return gold_dropado

# if __name__ == "__main__":
#     # BOSS, Desvantagem numérica, Elemental
#     dropar_gold('D', bonus=False)
