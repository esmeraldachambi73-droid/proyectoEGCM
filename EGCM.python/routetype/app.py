from flask import flask

app = flask(__name__)

@app.route("/cadena/<string:bombre>")
def demo_cadena(nombre):
    return f"string: {nombre}=> tipo: {type(nombre).__name__}"
@app.route("/entero/<int:numero>")
def demo_entero(numero):
    return f"entero: {numero} => tipo de datos: {type(numero).__name__}"
@app.route("/decimal/<float:decimal>")
def demo_float(decimal):
    return f"float: {decimal} => tipo de dato: {type(decimal).__name__}"
@app.route("/ruta/<path:ruta>")
def demo_ruta(ruta):
    return f"ruta: {ruta}"

if __name__=="__main__":
    app.rum(debug=true)