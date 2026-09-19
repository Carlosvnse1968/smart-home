from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


@app.route("/agente")
def agente():
    return render_template("agente.html")


@app.route("/cotizacion")
def cotizacion():
    return render_template("cotizacion.html")


@app.route("/enviar", methods=["POST"])
def enviar():

    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    telefono = request.form.get("telefono")

    print(nombre, correo, telefono)

    return render_template(
        "gracias.html",
        nombre=nombre
    )


if __name__ == "__main__":
    app.run(debug=True)