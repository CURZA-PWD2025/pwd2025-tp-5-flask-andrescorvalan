from flask import Flask
from data.data_productos import categorias,productos

app = Flask(__name__)

@app.route("/")

def home():
    return  "<h1>Hola ... bienvenido!!!, soy Andrés Leandro Corvalan, \
            vivo en Maquinchao - Río Negro, \
            y estoy intentando recibirme de Técnico Universitario en Desarrollo Web!!!<h1>"

@app.route("/productos")
def listar_productos():
    html="<h1>Listad de productos</h1>"
    html='<table border="1">'
    html= html+'<caption>Listado de productos</caption>'
    html= html+'<thead>\
                    <tr>\
                    <th>Id</th>\
                    <th>Descripción</th>\
                    <th>Categoría</th>\
                    </tr>\
                </thead>'
    html= html+'<tbody>'
    for un_producto in productos:
        html=html+'<tr>'
        html=html+'<td>'+f"{un_producto['id']}"+'</p>'
        html=html+'<td>'+f"{un_producto['descripcion']}"+'</p>'
        html=html+'<td>'+f"{un_producto['categoria_id']}"+'</p>'
        html=html+'</tr>'
    html=html+'</tbody>'
    html=html+'</table>'
    return html

@app.route("/categorias")
def listar_categorias():
    html='<table border="1">'
    html= html+'<caption>Listado de categorías</caption>'
    html= html+'<thead>\
                    <tr>\
                    <th>Id</th>\
                    <th>Descripción</th>\
                    </tr>\
                </thead>'
    html= html+'<tbody>'
    for un_categoria in categorias:
        html=html+'<tr>'
        html=html+'<td>'+f"{un_categoria['id']}"+'</p>'
        html=html+'<td>'+f"{un_categoria['descripcion']}"+'</p>'
        html=html+'</tr>'
    html=html+'</tbody>'
    html=html+'</table>'
    return html

if __name__ == "__main__":
    app.run(debug=True)