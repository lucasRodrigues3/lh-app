import random
from backend.equipamentos import tipos_defesas, efeitos_defesas, efeitos_armaduras, tipos_armaduras, \
    efeitos_equipamentos, municao, efeitos_armas, geral, tipos_armas


def gerar_equipamento(fixos, gold_max):
    gold_item = 1000000000
    tentativa = 0
    while gold_item > gold_max:
        gold = 0
        tipo_equipamento = random.choice(geral.tipo_equipamento) if fixos['categoria_equipamento'] == ''\
            else fixos['categoria_equipamento']
        tipo_dado = random.choice(geral.tipo_de_dado) if fixos['tipo_dado'] == '' else fixos['tipo_dado']
        quantidade_dado = random.randint(1, geral.dado_max[tipo_equipamento])
        gold += geral.custo_dado[tipo_equipamento][tipo_dado] * quantidade_dado
        raridade = geral.raridade_por_dado[tipo_dado]
        n_efeitos = geral.n_efeitos_por_raridade[raridade]
        n_efeitos = random.randint(0, n_efeitos)
        efeitos_possiveis = {}
        efeitos_possiveis.update(efeitos_armaduras.efeitos)
        efeitos_possiveis.update(efeitos_armas.efeitos)
        efeitos_possiveis.update(efeitos_defesas.efeitos)
        efeitos_possiveis.update(efeitos_equipamentos.efeitos)
        custos_efeitos_possiveis = {}
        custos_efeitos_possiveis.update(efeitos_armaduras.custos)
        custos_efeitos_possiveis.update(efeitos_armas.custos)
        custos_efeitos_possiveis.update(efeitos_defesas.custos)
        custos_efeitos_possiveis.update(efeitos_equipamentos.custos)
        efeitos_escolhidos = []
        texto_efeitos = ""
        for i in range(n_efeitos):
            raridade_efeito_i = random.choice(geral.tipo_raridade[raridade])
            tipo_efeito_i = random.choice([tipo_equipamento, 'Equipamento'])
            efeito_i = random.choice(efeitos_possiveis[tipo_efeito_i][raridade_efeito_i])
            while efeito_i in efeitos_escolhidos:
                efeito_i = random.choice(efeitos_possiveis[tipo_efeito_i][raridade_efeito_i])
            efeitos_escolhidos.append(efeito_i)
            gold += custos_efeitos_possiveis[efeito_i]
            texto_efeitos += f'Eff {i+1}: {efeito_i} - {tipo_efeito_i} {raridade_efeito_i} \n'
        carga = geral.n_cargas[raridade]
        tipos_equipamentos = {}
        tipos_equipamentos.update(tipos_armaduras.tipo_armaduras)
        tipos_equipamentos.update(tipos_armas.tipos_armas)
        tipos_equipamentos.update(tipos_defesas.tipo_defesas)
        tipos_equipamentos = tipos_equipamentos[tipo_equipamento]
        tipos_equipamentos = [t for t in tipos_equipamentos if t['Tipo'] == fixos['tipo_equipamento']]\
            if fixos['tipo_equipamento'] != '' else tipos_equipamentos
        equip = random.choice(tipos_equipamentos)
        texto_equip = ""
        for chave, valor in equip.items():
            if chave != "Gold":
                texto_equip += f"{chave}: {valor} \n"
            else:
                gold += valor
        texto_municao = ""
        if tipo_equipamento == 'Arma':
            if equip['MNC'] != '-':
                municao_sorteada = random.choice(municao.municao[equip['MNC']])
                texto_municao += 'Munição sorteada: \n'
                for chave, valor in municao_sorteada.items():
                    texto_municao += f"    {chave}: {valor}\n"
        gold_item = gold
        tentativa += 1
        if tentativa == 1000:
            print('Gold insuficiente para gerar um equipamento')
            break
    if tentativa != 1000:
        print('Equipamento: ', tipo_equipamento)
        print('Dado: ', tipo_dado)
        print('Quantidade de dados: ', quantidade_dado)
        print('Radidade do item: ', raridade)
        print('Carga: ', carga, '\n')
        print(texto_efeitos)
        print(texto_equip)
        print(texto_municao)
        print('Gold total do item gerado: ', gold)
        print()
        print('-------------------------------------------------------------------------------')
        print()
        return gold
    return gold_max

if __name__ == "__main__":
    fixos = {
        'categoria_equipamento': '', # Arma, Armadura, Defesa
        'tipo_dado': '', # d6, d8, d10, d12, d20
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
    gerar_equipamento(fixos, 1000)
