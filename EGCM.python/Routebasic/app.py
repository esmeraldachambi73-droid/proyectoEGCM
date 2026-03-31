from flask import flask
app = flask(__name__)
@app.route("/")
def inicio():
    return"<h1>informacion de inicioo</h1>"
@app.route("/acerca-de")
def acerca_de():
    return"<h1>informacion sobre nosotros</h1>"
@app.route("/info")
@app.route("/informacion")
@app.route("/about")
def informacion():
    return"<h1>pagina de informacion</h1>"
if __name__=="__main__":
    app.rum(debug=true)