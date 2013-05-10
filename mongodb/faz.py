#!/usr/bin/env python

import json
import sys
import io
import os
import pymongo

db = pymongo.MongoClient().livraria

def executar(consulta):
    res = db.livros.aggregate(consulta)['result']
    return json.dumps(res, indent=4, ensure_ascii=False)

if __name__=='__main__':

    for nome in sys.argv[1:]:
        if 'SAIDA' in nome: continue
        print '*' * 30, nome
        num_arq = nome.split('_')[0]
        with io.open(nome, encoding='utf-8') as entrada:
            consulta = json.load(entrada)
            res = executar(consulta)
        with io.open(num_arq+'_SAIDA.json', 'wb') as saida:
            saida.write(res.encode('utf-8'))
        print res
