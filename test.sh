#!/bin/bash

cd /workspaces/mkdocs_puml_include
pip install .
mkdocs serve -a 0.0.0.0:8001 -f example/mkdocs.yml