==================
$match: seleção
==================

---------
Definição
---------

Para cada documento atual no pipeline, avalia um predicado para determinar se o documento continua no pipeline ou é descartado.

Vários predicados podem ser combinados com os operadores ``$and``, ``$or`` e ``$nor``. Um predicado pode ser negado com ``$not``.

Teoria
------

Equivale ao operador σ (sigma) na álgebra relacional. Por exemplo, dada uma relação **R**, a seguinte operação produz uma relação contendo apenas as tuplas que possuem ``idioma`` ``"pt-br"``:

    π\ :sub:`idioma="pt-br"`\ (*R*)


Comparação com SQL
------------------

Em SQL, a **seleção** é definida pelas cláusulas ``WHERE`` e ``HAVING``. Por exemplo, a consulta a seguir obtém uma relação dos registros de ``livros`` com ``idioma idioma`` igual ``"pt-br"``:

    ``SELECT * FROM tabela WHERE idioma="pt-br"``


Dicas
-----

Tente fazer ``$match`` logo no início ou próximo do início do pipeline, pois isso economiza processamento nos estágios seguites.

Se o primeiro estágio de um pipeline é um ``$match``, o MongoDB pode usar índices para acelerar o processamento.

O operador ``$where`` ()


--------
Exemplos
--------


``200_match_idioma.json``
---------------------------

.. literalinclude:: exemplos/200_match_idioma.json
   :language: json

.. literalinclude:: exemplos/200_SAIDA.json
   :language: json

``210_match_paginas_lt_200.json``
----------------------------------

.. literalinclude:: exemplos/210_match_paginas_lt_200.json
   :language: json

.. literalinclude:: exemplos/210_SAIDA.json
   :language: json

``220_match_idioma_E_paginas_gt.json``
-----------------------------------------

.. literalinclude:: exemplos/220_match_idioma_E_paginas_gt.json
   :language: json

.. literalinclude:: exemplos/220_SAIDA.json
   :language: json


``230_match_idioma_OU_paginas_lt.json``
-----------------------------------------

.. literalinclude:: exemplos/230_match_idioma_OU_paginas_lt.json
   :language: json

.. literalinclude:: exemplos/230_SAIDA.json
   :language: json
