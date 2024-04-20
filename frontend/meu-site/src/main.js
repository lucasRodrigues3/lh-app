import geral from './geral.js';
import efeitos_armaduras from './efeitos_armaduras.js';
import efeitos_armas from './efeitos_armas.js';
import efeitos_defesas from './efeitos_defesas.js';
import efeitos_equipamentos from './efeitos_equipamentos.js';
import tipos_armaduras from './tipos_armaduras.js';
import tipos_armas from './tipos_armas.js';
import tipos_defesas from './tipos_defesas.js';
import municao from './municao.js';


export function gerarItem() {
    function choice(array) {
        return array[Math.floor(Math.random() * array.length)];
    }

    function randint(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    let gold = 0;
    const tipoEquipamento = choice(geral.tipoEquipamento);
    const tipoDado = choice(geral.tipoDeDado);
    const quantidadeDado = randint(1, geral.dadoMax[tipoEquipamento]);
    gold += geral.custoDado[tipoEquipamento][tipoDado] * quantidadeDado;
    const raridade = geral.raridadePorDado[tipoDado];
    const nEfeitos = geral.nEfeitosPorRaridade[raridade];
    const efeitosPossiveis = {...efeitos_armaduras.efeitos, ...efeitos_armas.efeitos, ...efeitos_defesas.efeitos, ...efeitos_equipamentos.efeitos};
    const custosEfeitosPossiveis = {...efeitos_armaduras.custos, ...efeitos_armas.custos, ...efeitos_defesas.custos, ...efeitos_equipamentos.custos};
    const efeitosEscolhidos = [];
    let textoEfeitos = "";

    for (let i = 0; i < nEfeitos; i++) {
        const raridadeEfeitoI = choice(geral.tipoRaridade[raridade]);
        const tipoEfeitoI = choice([tipoEquipamento, 'Equipamento']);
        let efeitoI = choice(efeitosPossiveis[tipoEfeitoI][raridadeEfeitoI]);

        while (efeitoI in efeitosEscolhidos) {
            efeitoI = choice(efeitosPossiveis[tipoEfeitoI][raridadeEfeitoI]);
        }

        efeitosEscolhidos.push(efeitoI);
        gold += custosEfeitosPossiveis[efeitoI];
        textoEfeitos += `Eff ${i + 1}: ${efeitoI} - ${tipoEfeitoI} ${raridadeEfeitoI} \n`;
    }

    const carga = geral.nCargas[raridade];
    const tiposEquipamentos = {...tipos_armaduras.tipoArmaduras, ...tipos_armas.tipoArmas, ...tipos_defesas.tipoDefesas};
    const equip = choice(tiposEquipamentos[tipoEquipamento]);
    let textoEquip = "";

    for (const [chave, valor] of Object.entries(equip)) {
        if (chave !== "Gold") {
            textoEquip += `${chave}: ${valor} \n`;
        } else {
            gold += valor;
        }
    }

    let textoMunicao = "";

    if (tipoEquipamento === 'Arma' && equip['MNC'] !== '-') {
        const municaoSorteada = choice(municao.municao[equip['MNC']]);
        textoMunicao += 'Munição sorteada: \n';

        for (const [chave, valor] of Object.entries(municaoSorteada)) {
            textoMunicao += `    ${chave}: ${valor}\n`;
        }
    }

    console.log('Equipamento: ', tipoEquipamento);
    console.log('Dado: ', tipoDado);
    console.log('Quantidade de dados: ', quantidadeDado);
    console.log('Radidade do item: ', raridade);
    console.log('Carga: ', carga, '\n');
    console.log(textoEfeitos);
    console.log(textoEquip);
    console.log(textoMunicao);
    console.log('Gold total do item gerado: ', gold);
}