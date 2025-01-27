# mkdocs_puml_file

A MkDocs Plugin for embedding PlantUML files.

## Features

This plugin enables you to embed PlantUML diagrams in your documentation. Simple add your files like you would for any other image type:

```
![description](my-file.puml)
```

## Prerequisites

1. Install mkdocs_puml_file via ```pip install mkdocs_puml_file```.
1. For rendering, assure plugin ```mkdocs_plantuml``` is installed via ```pip``` as well.
1. Add plugin ```puml_file```before the entry of plugin ```plantuml``` in ```mkdocs.yml```. This is important, because MkDocs executes plugin events in the order of the plugins occurence in the configuration.