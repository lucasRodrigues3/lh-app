import random
from backend import (efeitos_armaduras, efeitos_armas, efeitos_defesas, efeitos_equipamentos,
                     geral, municao, tipos_armas, tipos_armaduras, tipos_defesas)

def gerar_item():
    gold = 0
    tipo_equipamento = random.choice(geral.tipo_equipamento)
    tipo_dado = random.choice(geral.tipo_de_dado)
    quantidade_dado = random.randint(1, geral.dado_max[tipo_equipamento])
    gold += geral.custo_dado[tipo_equipamento][tipo_dado] * quantidade_dado
    raridade = geral.raridade_por_dado[tipo_dado]
    n_efeitos = geral.n_efeitos_por_raridade[raridade]
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
    equip = random.choice(tipos_equipamentos[tipo_equipamento])
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

    print('Equipamento: ', tipo_equipamento)
    print('Dado: ', tipo_dado)
    print('Quantidade de dados: ', quantidade_dado)
    print('Radidade do item: ', raridade)
    print('Carga: ', carga, '\n')
    print(texto_efeitos)
    print(texto_equip)
    print(texto_municao)
    print('Gold total do item gerado: ', gold)

if __name__ == "__main__":
    gerar_item()
