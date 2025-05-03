from flask import Flask, request, render_template


app = Flask (__name__)

@app.route("/")
def home():
    return "Pagina de inicio"

# ruta para parametros url
@app.route("/consulta")
def ruta_cosulta():
    producto=request.args.get("product")
    talla=request.args.get("talla")
    if producto and talla is None:
        return f"se esta consultando solo el producto {producto}"
    if talla  is None and producto :
        return f"por favor ingrese el producto a consultar{talla}"
    if talla  is None and producto is None:
        return f"Bienvenido a la pagina de ropa"
    
    return f"Se esta consultando el producto{producto} y la talla{talla}"

# ruta para capturar datos por el body = cuerpo de la solicitud
@app.route("/registro",methods=["GET"])
def ruta_registro():
    return render_template("formulario.html")

@app.route("/registro", methods=["POST"])
def procesar_registro():
    nombre=request.form.get("nombre")
    correo=request.form.get("correo")

    return f"el estudiente a registrar es {nombre} y el correo a registrar es {correo}"





    




if __name__ == "__main__":
    app.run (debug=True)
    
