import csv

from flask import Flask, render_template, request, redirect, send_file

app = Flask(__name__)


itens = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        numero_item = request.form["numero_item"]
        quantidade = request.form["quantidade"]

        if numero_item and quantidade:
            quantidade = int(quantidade)

            if numero_item in itens:
                itens[numero_item] += quantidade
            else:
                itens[numero_item] = quantidade

        return redirect("/")

    return render_template("index.html", itens=itens)

@app.route("/download")
def download():
    filename = "relatorio_itens.csv"

    with open(filename, "w", newline="") as arquivo:
        writer = csv.writer(arquivo, delimiter=";")
        writer.writerow(["Número do Item", "Quantidade Total"])
        for item, qtd in itens.items():
            writer.writerow([item, qtd])

    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run()

