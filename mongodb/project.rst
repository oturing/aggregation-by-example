==================
$project: projeção
==================

---------
Definição
---------

Para cada documento atual no pipeline, gera um novo documento formando por um sub-conjunto dos campos do documento atual, opcionalmente efetuando operações nos valores.

Teoria
------

Equivale ao operador π na álgebra relacional. Por exemplo, dada uma relação **R**, a seguinte operação produz uma relação contendo apenas os atributos ``titulo`` e ``idioma`` das tuplas de *R*:

    π\ :sub:`titulo, idioma`\ (*R*)


Comparação com SQL
------------------

Em SQL, a **projeção** é definida pela lista de campos ou expressões logo após a palavra reservada ``SELECT``. Por exemplo, dada uma tabela ``livros``, a consulta a seguir obtém uma relação apenas com os campos ``titulo`` e ``idioma``:

    ``SELECT titulo, idioma FROM tabela``

--------
Exemplos
--------


``100_project_titulo.json``
---------------------------

.. literalinclude:: exemplos/100_project_titulo.json
   :language: json

.. literalinclude:: exemplos/100_SAIDA.json
   :language: json


``110_project_titulo_idioma.json``
----------------------------------

.. literalinclude:: exemplos/110_project_titulo_idioma.json
   :language: json

.. literalinclude:: exemplos/110_SAIDA.json
   :language: json

``120_project_titulo_idioma_sem_id.json``
-----------------------------------------

.. literalinclude:: exemplos/120_project_titulo_idioma_sem_id.json
   :language: json

.. literalinclude:: exemplos/120_SAIDA.json
   :language: json
