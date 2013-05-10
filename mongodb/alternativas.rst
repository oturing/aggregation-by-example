===========================================
Formas alternativas de agregação em MongoDB
===========================================


Funções count, distinct e group
-------------------------------

::

    > db.livros.count()
    9

    > db.livros.distinct("idioma")
    [ "en", "pt-br" ]


    > db.livros.group(
    ...     {
    ...         key: "idioma",
    ...         initial: {total: 0},
    ...         reduce: function(item, res) { res.total++ }
    ...     }
    ... )
    [ { "total" : 9 } ]

    > db.livros.group(
    ...     {
    ...         key: "idioma",
    ...         initial: {total: 0},
    ...         reduce: function(item, res) { res.total+=item.estoque }
    ...     }
    ... )
    [ { "total" : 53 } ]


Map-reduce
----------

::

    > var valorItem = function() {
    ...   emit(this.preco.moeda, this.preco.valor * this.estoque)
    ... }

    > var somaMoeda = function(moeda, valores) {
    ...   return Array.sum(valores)
    ... }

    > db.livros.mapReduce(valorItem, somaMoeda, {out: "valor_estoque"})
    {
      "result" : "valor_estoque",
      "timeMillis" : 22,
      "counts" : {
        "input" : 9,
        "emit" : 9,
        "reduce" : 2,
        "output" : 2
      },
      "ok" : 1,
    }

    > db.valor_estoque.find()
    { "_id" : "BRL", "value" : 570.7 }
    { "_id" : "USD", "value" : 1038.8999999999999 }

