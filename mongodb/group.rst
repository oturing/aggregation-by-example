===================
$group: agrupamento
===================

---------
Definição
---------

Gera um documento para cada valor distinto de uma chave selecionada.

O documento gerado tem sempre um campo ``_id`` que contém o valor da chave de agrupamento, e pode ter campos adicionais calculados através de funções de agrupamento (``$sum``, ``$avg``, ``$min``, ``$max``, ``$first``, ``$last``, ``$push``, ``$addToSet``).

Comparação com SQL
------------------

Em SQL, o **agrupamento** é definido pela clausula ``GROUP BY``. Por exemplo, dada uma tabela ``livros``, a consulta a seguir obtém uma relação com a contagem de livros por idioma:

    ``SELECT idioma, count(*) FROM livros``

--------
Exemplos
--------

``500_group_contagem.json``
---------------------------

.. literalinclude:: exemplos/500_group_contagem.json
   :language: json

.. literalinclude:: exemplos/500_SAIDA.json
   :language: json


``510_group_sum_estoque.json``
----------------------------------

.. literalinclude:: exemplos/510_group_sum_estoque.json
   :language: json

.. literalinclude:: exemplos/510_SAIDA.json
   :language: json

``520_group_contagem_por_idioma.json``
-----------------------------------------

.. literalinclude:: exemplos/520_group_contagem_por_idioma.json
   :language: json

.. literalinclude:: exemplos/520_SAIDA.json
   :language: json

``530_group_count_moeda.json``
-----------------------------------------

.. literalinclude:: exemplos/530_group_count_moeda.json
   :language: json

.. literalinclude:: exemplos/530_SAIDA.json
   :language: json


``540_group_valor_estoque.json``
-----------------------------------------

.. literalinclude:: exemplos/540_group_valor_estoque.json
   :language: json

.. literalinclude:: exemplos/540_SAIDA.json
   :language: json

