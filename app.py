import os
import json
import spacy
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Import NLP model.
nlp = spacy.load("es_core_news_sm")


@app.route("/")
def index():
    return render_template("file_form.html")


@app.route("/process", methods = ["POST"])
# Function to get the entities from the sentences.
def get_ents():
    # Read the JSON file containing the sentences.
    file = request.files["file"]
    docs = json.load(file)
    docs = docs.get("oraciones")
    
    # List containing the results.
    results = []
    
    # Process each sentence in the list of sentences.
    for text in docs:
        doc = nlp(text)
        # Main auxiliar dictionary to save sentence and entities.
        entities = {}
        entities["oracion"] = text
        # Auxiliar dictionary to save entities.
        ents_doc = {}

        # Get the entities in each sentence.
        for ent in doc.ents:
            # Save each entitie as key and each label as value in the aux dict.
            ents_doc[ent.text] = ent.label_
        
        # Build main aux dict and append it to results.
        entities["entidades"] = ents_doc
        results.append(entities)

    # Build final dictionary containing all the results.
    export_results = {}
    export_results["resultado"] = results

    # Save the results as a JSON file.
    with open("resultado.json", "w", encoding="utf-8") as f:
        json.dump(export_results, f, ensure_ascii=False, indent=2)

    return jsonify({"Resultados": export_results})

if __name__ == "__main__":
    app.run(debug = True)