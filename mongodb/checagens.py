
import json

livros = json.load(open('dados/livros.json'))

def f540_group_valor_estoque():
    moedas = {}
    for livro in livros:
        moeda = livro['preco']['moeda']
        moedas[moeda] = moedas.get(moeda, 0) + livro['estoque'] * livro['preco']['valor']
    return moedas

def main():
    for nome in sorted(globals()):
        if nome[0] == 'f' and nome[1].isdigit():
            print nome
            print '\t', globals()[nome]()


main()

