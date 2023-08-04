# API en Flask para reconocimiento de entidades mencionadas

## Instalación del modelo de NLP

```
python -m spacy download es_core_news_sm
```

## Uso

Ejecutar en terminal con el siguiente comando:
```
python3 app.py
```

Y entrar a la URL:
http://127.0.0.1:5000

Seleccionar el archivo JSON que contiene las oraciones en el formato correspondiente. En este ejemplo, se carga el archivo llamado "sentences.json".

Finalmente se da click en **Procesar** y se muestra el resultado. Adicionalmente, se guarda el archivo en formato JSON con el nombre "resultado.json" en la carpeta raíz.
