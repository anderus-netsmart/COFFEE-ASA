from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contacto", methods=["POST"])
def contacto():
    nombre = request.form.get("nombre")
    correo = request.form.get("correo")
    mensaje = request.form.get("mensaje")
    print(f"Mensaje recibido de {nombre} ({correo}): {mensaje}")
    return "Gracias por tu mensaje. Te responderemos pronto."

if __name__ == "__main__":
    app.run(debug=True)
