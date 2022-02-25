
import requests

from bs4 import BeautifulSoup


############INTELAF##################################################################################################
class intelaf_Scraper():
    def __init__(self,url,cantidad):
        self.url = url
        self.nombre = ''
        self.precion = ''
        self.precioe = ''
        self.descuento = ''
        self.cantidad=str(cantidad)
        self.subtotaln=''
        self.subtotale=''
        self.imagen=''
        


    def getData(self):

        response = requests.get(self.url)

        html  = BeautifulSoup(response.text, 'html5lib')

        nombre = html.find('h1', class_='descripcion_p')
        #self.nombre = nombre.text
        self.nombre=nombre.string
        
        precion = html.find('div', class_="col-xs-12 col-md-7 detalle_venta")
        self.precion = str(precion.contents[3].text).replace('Precio normal Q','')

        precioe = html.find('p',class_="beneficio_efectivo")
        precioe = str(precioe).replace("<p class=\"beneficio_efectivo\" style=\"color: darkorange; font-weight: bold;\"> Beneficio Efectivo","").replace("</p>","").strip()
        precioe = str(precioe).split("Q")
        self.precioe = str(precion.contents[6].text).replace('Beneficio Efectivo Q','')


        self.subtotaln = str( float(str(self.precion).replace(",","")) * float(self.cantidad) )

        self.subtotale = str( float(str(self.precioe).replace(",","")) * float(self.cantidad) )

        img = html.find('div',class_="col-xs-12 col-md-5")
        img = img.attrs['style'].split("url(\"")
        img = img[1].split(".jpg\");")
        self.imagen = str(img[0]+'.jpg')

    def getProducto(self):
        self.getData()
        self.descuento = float(str(self.precion).replace(",","")) - float(str(self.precioe).replace(",","")) * float(self.cantidad)
        producto={
            'nombre':self.nombre, 
            'precion':self.precion, 
            'precioe':self.precioe,
            'descuento':str(self.descuento),
            'cantidad':self.cantidad,
            'imagen':self.imagen,
            'subtotaln':self.subtotaln,
            'subtotale':self.subtotale,
            'link':self.url
        }
        return producto

    

############IMEQMO##################################################################################################

class imeqmo_Scraper():
    def __init__(self,url, cantidad):
        self.url = url
        self.nombre = ''
        self.precion = ''
        self.precioe = ''
        self.descuento = ''
        self.cantidad=str(cantidad)
        self.subtotaln=''
        self.subtotale=''
        self.imagen=''

    def getData(self):

        response = requests.get(self.url)

        html  = BeautifulSoup(response.text, 'html.parser')

        nombre = html.find('h1', class_='te_product_name')
        self.nombre = nombre.text
        #self.nombre=str(nombre).replace("<h1 class=\"te_product_name\" itemprop=\"name\">","").replace("</h1>","").rstrip("\n")
        
        

        precioe = html.find('b',class_="oe_price")
        precioe = str(precioe).split("<span class=\"oe_currency_value\">")
        self.precioe = str(precioe[1]).replace("</span></b>","")

        try:
            precion = html.find('span',class_="text-danger oe_default_price")
            precion = str(precion).split("class=\"oe_currency_value\">")
            self.precion = str(precion[1]).replace("</span>","")
        except:
            self.precion = self.precioe

        self.subtotaln = str( float(str(self.precion).replace(",","")) * float(self.cantidad) )

        self.subtotale = str( float(str(self.precioe).replace(",","")) * float(self.cantidad) )

        img = html.find('img', class_="img img-fluid product_detail_img")
        img = img.attrs['src'].replace("\"","")
        self.imagen = str("https://www.imeqmo.com" + str(img))


        

    def getProducto(self):
        self.getData()
        self.descuento = float(str(self.precion).replace(",","")) - float(str(self.precioe).replace(",","")) * float(self.cantidad)
        producto={
            'nombre':self.nombre, 
            'precion':self.precion, 
            'precioe':self.precioe,
            'descuento':str(self.descuento),
            'cantidad':self.cantidad,
            'imagen':self.imagen,
            'subtotaln':self.subtotaln,
            'subtotale':self.subtotale,
            'link':self.url
        }
        return producto

############MACROSISTEMAS##################################################################################################


class macrosistemas_Scraper():
    def __init__(self,url,cantidad):
        self.url = url
        self.nombre = ''
        self.precion = ''
        self.precioe = ''
        self.descuento = ''
        self.cantidad=str(cantidad)
        self.subtotaln=''
        self.subtotale=''
        self.imagen=''
        

    def getData(self):

        response = requests.get(self.url)

        html  = BeautifulSoup(response.text, 'html.parser')

        nombre = html.find('h1', class_='title-product')
        self.nombre = nombre.text
        #self.nombre=str(nombre).replace("<h1 class=\"title-product\">\n","").replace("</h1>","").rstrip("\n")
        
        precion = html.find('span',class_="PricesalesPrice")
        self.precion = str(precion).replace("</span>","").replace("<span class=\"PricesalesPrice\">Q","").strip()

        precioe = html.find('div',class_="cash")
        self.precioe = str(precioe).replace("<div class=\"cash\"><i class=\"far fa-money-bill-alt\"></i> En efectivo: Q","").replace("</div>","").strip()

        self.subtotaln = str( float(str(self.precion).replace(",","")) * float(self.cantidad) )

        self.subtotale = str( float(str(self.precioe).replace(",","")) * float(self.cantidad) )


        img = html.find('a', class_="cloud-zoom")
        img = img.attrs['href'].replace(" ","%20")

        self.imagen =str(img)

    def getProducto(self):
        self.getData()
        self.descuento = float(str(self.precion).replace(",","")) - float(str(self.precioe).replace(",","")) * float(self.cantidad)
        producto={
            'nombre':self.nombre, 
            'precion':self.precion, 
            'precioe':self.precioe,
            'descuento':str(self.descuento),
            'cantidad':self.cantidad,
            'imagen':self.imagen,
            'subtotaln':self.subtotaln,
            'subtotale':self.subtotale,
            'link':self.url
        }
        return producto



#print("\nINTELAF")
#intelaf = intelaf_Scraper("https://www.intelaf.com/precios_stock_detallado.aspx?codigo=CAM-NXT-SMW4U2", "2")
#dataIntelaf = intelaf.getProducto()
#print(dataIntelaf['nombre'], dataIntelaf['precion'], dataIntelaf['precioe'], dataIntelaf['imagen'])


#print("\nIMEQMO")
#imeqmo = imeqmo_Scraper("https://www.imeqmo.com/shop/product/bx8070110100f-procesador-intel-core-i3-10100f-3-6ghz-10th-gen-13250?category=11", "2")
#dataImeqmo = imeqmo.getProducto()
#print(dataImeqmo['nombre'], dataImeqmo['precion'], dataImeqmo['precioe'], dataImeqmo['imagen'], dataImeqmo['subtotale'])

#print("\nMACROSISTEMAS")
#macrosistemas = macrosistemas_Scraper("https://www.macrosistemas.com/productos/memorias/memorias-ram/brocs,-memoria-ddr4-de-8gb-para-pc,-bus-pc3200,-3-a%C3%B1os-de-garantia-detail", "2")
#dataMacro = macrosistemas.getProducto()
#print(dataMacro['nombre'], dataMacro['precion'], dataMacro['precioe'], dataMacro['imagen'], dataMacro['subtotale'])