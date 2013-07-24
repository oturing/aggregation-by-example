==================
$unwind: explosão
==================

---------
Definição
---------

Para cada documento atual no pipeline que contem um campo *array*, gera N documentos na saída, um para cada item do *array*. A estrutura dos documentos de saída é igual a do documento de entrada, apenas o valor do campo *array* é substituído pelo valor escalar.

--------
Exemplos
--------


``600_unwind_assuntos.json``
----------------------------

.. literalinclude:: exemplos/600_unwind_assuntos.json
   :language: json

.. literalinclude:: exemplos/600_SAIDA.json
   :language: json

``610_unwind_assuntos.json``
----------------------------------

.. literalinclude:: exemplos/610_unwind_assuntos.json
   :language: json

.. literalinclude:: exemplos/610_SAIDA.json
   :language: json

``620_unwind_assuntos_count.json``
-----------------------------------------

.. literalinclude:: exemplos/620_unwind_assuntos_count.json
   :language: json

.. literalinclude:: exemplos/620_SAIDA.json
   :language: json


``630_unwind_assuntos_titulos.json``
-----------------------------------------

.. literalinclude:: exemplos/630_unwind_assuntos_titulos.json
   :language: json

.. literalinclude:: exemplos/630_SAIDA.json
   :language: json
