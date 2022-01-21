
import os
from unittest import result
from flask import Flask, render_template, jsonify, request, send_from_directory
from markupsafe import re
from numpy import require
from sqlalchemy import true

from WebScraper.recolector import Recolector as rec

from flask_sqlalchemy import SQLAlchemy






  
app = Flask(__name__, template_folder='templates') #creating the Flask class object   
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tienda = db.Column(db.String(64), index = True)
    producto = db.Column(db.String(256), index = True )
    imagen = db.Column(db.String(512), index = True)
    cantidad = db.Column(db.String(64), index = True)
    precion = db.Column(db.String(64), index = True)
    subtotaln = db.Column(db.String(65), index = True)
    precioe = db.Column(db.String(64), index = True)
    subtotale = db.Column(db.String(65), index = True)
    descuento = db.Column(db.String(64), index = True)
    link = db.Column(db.String(512), index = True)
    

db.create_all()
try:
    #home endpoint
    @app.route('/') #decorator drfines the   
    def home():  
        return render_template('index.html')
        
    
    #endpoints
    @app.route('/cotiza')
    def cotiza():
        return render_template('cotiza.html')

    @app.route('/procesar', methods=['POST'])
    def procesar():
        listaLinks = []
        listaLinks.append([str(request.form.get("procesador")),'1'])
        listaLinks.append([str(request.form.get("motherboard")),'1'])

        if( request.form.get('ssdCantidad') == '' or request.form.get('ssdCantidad') == 0 ):
            listaLinks.append([str(request.form.get("ssd")),"1"])
        else:
            listaLinks.append([str(request.form.get("ssd")),str(request.form.get("ssdCantidad"))])

        if( request.form.get("discoCantidad") == '' or request.form.get("discoCantidad") == '0'):
            listaLinks.append([str(request.form.get("disco")),"1"])
        else:
            listaLinks.append([str(request.form.get("disco")),str(request.form.get("discoCantidad"))])

        if (request.form.get("ramCantidad")=='' or request.form.get("ramCantidad")==0):
            listaLinks.append([str(request.form.get("ram")),"1"])
        else:
            listaLinks.append([str(request.form.get("ram")),str(request.form.get("ramCantidad"))])

        listaLinks.append([str(request.form.get("power")),'1'])
        listaLinks.append([str(request.form.get("disipador")),'1'])

        if (request.form.get("ventiladorCantidad") == '' or request.form.get("ventiladorCantidad")==0):
            listaLinks.append([str(request.form.get("ventilador")),"1"])
        else:
            listaLinks.append([str(request.form.get("ventilador")),str(request.form.get("ventiladorCantidad"))])


        listaLinks.append([str(request.form.get("video")),'1'])
        listaLinks.append([str(request.form.get("case")),'1'])
        
        
        c = rec(listaLinks)
        data = c.getData()

        db.session.query(Producto).delete()
        db.session.commit


        resultado = ''
        for d in data:
            
            elemento = Producto(tienda=d['tienda'],
                                producto=d['producto']['nombre'],
                                imagen=d['producto']['imagen'],
                                cantidad=d['producto']['cantidad'],
                                precion=d['producto']['precion'],
                                subtotaln=d['producto']['subtotaln'],
                                precioe=d['producto']['precioe'],
                                subtotale=d['producto']['subtotale'],
                                descuento=d['producto']['descuento'],
                                link =d['producto']['link']
                                )

            db.session.add(elemento)
        db.session.commit()
        productos = Producto.query
        precioNormal = c.getNormalPrice()
        precioEfectivo = c.getCashPrice()
        precioDescuento = c.getDiscount()
        return render_template('table.html', productos=productos, precioNormal=precioNormal, precioEfectivo=precioEfectivo, precioDescuento=precioDescuento)

    #arranque de app
    if __name__ =='__main__':  
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0',port=port)
        app.run(debug=True)

except Exception as err:
    print('Error: {0} >'.format(err))