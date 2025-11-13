from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def soma():
    valor1 = float(request.args.get("valor1", 0))
    valor2 = float(request.args.get("valor2", 0))
    resultado = valor1 + valor2
    return f"<h1>O resultado da soma é: {resultado}</h1>"

@app.route("/subtracao")
def subtracao():
    valor1 = float(request.args.get("valor1", 0))
    valor2 = float(request.args.get("valor2", 0))
    resultado = valor1 - valor2
    return f"<h1>O resultado da subtração é: {resultado}</h1>"

@app.route("/multiplicacao")
def multiplicacao():
    valor1 = float(request.args.get("valor1", 0))
    valor2 = float(request.args.get("valor2", 0))
    resultado = valor1 * valor2
    return f"<h1>O resultado da multiplicação é: {resultado}</h1>"

@app.route("/divisao")
def divisao():
    valor1 = float(request.args.get("valor1", 0))
    valor2 = float(request.args.get("valor2, 1"))
    if valor2 == 0:
        return "<h1>0 resuktado da divisao e: {resultado}</h1>"
    
if __name__ == "__main":
    app.run(debug=True)