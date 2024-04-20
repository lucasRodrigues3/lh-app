import random

from consumiveis.main import gerar_conjunto_itens
from criaturas.main import dropar_gold
from equipamentos.main import gerar_equipamento

if __name__ == "__main__":
    fixos = {
        'categoria_equipamento': '',  # Arma, Armadura, Defesa
        'tipo_dado': '',  # d6, d8, d10, d12, d20
        'tipo_equipamento': ''
        # Adaga
        # Arco
        # Armas de Fogo
        # Balista
        # Bastão
        # Besta
        # Corrente
        # Espada
        # Foice
        # Lança
        # Machado
        # Maça
        # Manopla
        # Martelo

        # Broquel
        # Heater
        # Micênico
        # Torre

        # Cota
        # Hoplita
        # Couraça
        # Escamas
        # Placas
    }
    gold_dropado = dropar_gold('C', bonus=False) # Rank criatura, Bonus: True / False
    com_equipamento = random.choice([True, False])
    if com_equipamento:
        gold_restante = gerar_equipamento(fixos, gold_dropado)
        gold_restante = gold_dropado - gold_restante
        gerar_conjunto_itens(gold_restante)
    else:
        com_itens = random.choice([True, False])
        if com_itens:
            gerar_conjunto_itens(gold_dropado)
        else:
            print('Gold gerado: ', gold_dropado)
