from flask import Flask, request, render_template , make_response


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
listado=[]
@app.route("/registro",methods=["GET"])
def ruta_registro(): 
    #listado=[{"nombre" : "Alejandro", "correo" : "alejotier@gmail.com"}]
    return render_template("formulario.html", listado=listado)

@app.route("/registro", methods=["POST"])
def procesar_registro():
    nombre=request.form.get("nombre")
    correo=request.form.get("correo")
    estudiantes={"nombre": nombre, "correo": correo}
    listado.append(estudiantes)
    #print(nombre)

    return f"el estudiente a registrar es {nombre} y el correo a registrar es {correo}"


# parametros en la ruta
@app.route("/estudiantes/<string:area>/<int:grupo>")
def mostrar_estudiantes(grupo, area):
    return f"el programa de formacion consultado es {area} y el grupo consultado es {grupo} "

    
# solicitus tipo 4 / encabezados mensajes
@app.route('/ver-headers')
def ver_headers():
    agente_usuario = request.headers.get('User-Agent')
    return f"Tu navegador es: {agente_usuario}"


# cookis
@app.route('/crear-cookie')
def crear_cookie():
    respuesta = make_response("Cookie creada!")
    respuesta.set_cookie('usuario_logueado', 'true', max_age=60*60*24,httponly=True)
    return respuesta

@app.route('/leer-cookie')
def leer_cookie():
    valor = request.cookies.get('usuario_logueado')
    return f"Valor de la cookie: {valor}"






if __name__ == "__main__":
    app.run (debug=True)
    
