#!/bin/bash
~/opt/mongodb/bin/mongoimport --host localhost --port 27017 \
		--db livraria --collection livros \
		--jsonArray --file dados/livros.json \

