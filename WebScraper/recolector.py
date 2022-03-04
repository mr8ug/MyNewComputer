import WebScraper.scrapers as s
#import scrapers as s
class Recolector():
    def __init__(self, linkList):
        self.links = linkList
        self.data = []

    def analizeLinks(self):
        
        for l in self.links:
            error={
            'nombre':str(l[0]), 
            'precion':'Error', 
            'precioe':'Error',
            'descuento':'Error',
            'cantidad':'Error',
            'imagen':'Error',
            'subtotaln':'Error',
            'subtotale':'Error',
            'link': str(l[0])
            }

            if 'intelaf' in str(l[0]):
                #Determina que el link es de intelaf
                try:
                    intelaf = s.intelaf_Scraper(str(l[0]),str(l[1]) )

                    self.data.append({'tienda':'INTELAF', 'producto':intelaf.getProducto()})
                except:
                    self.data.append({'tienda':'INTELAF', 'producto':error})

            if 'imeqmo' in str(l[0]):
                try:
                    imeqmo = s.imeqmo_Scraper(str(l[0]),str(l[1]))
                    self.data.append({'tienda':'IMEQMO', 'producto':imeqmo.getProducto()})
                except:
                    self.data.append({'tienda':'IMEQMO', 'producto':error})

            if 'macrosistemas' in str(l[0]):
                try:
                    macro = s.macrosistemas_Scraper(str(l[0]),str(l[1]))
                    self.data.append({'tienda':'MACROSISTEMAS', 'producto':macro.getProducto()})
                except:
                    self.data.append({'tienda':'MACROSISTEMAS', 'producto':error})

    def getData(self):
        self.analizeLinks()
        return self.data

    def getNormalPrice(self):
        precioNormal=0;
        for d in self.data:
            if d['producto']['subtotaln'] != 'Error':
                precioNormal += float(str(d['producto']['subtotaln']).replace(',', ""))

        return str(precioNormal)

    def getCashPrice(self):
        precioEfectivo = 0;
        for d in self.data:
            if d['producto']['subtotale'] != 'Error':
                precioEfectivo += float(str(d['producto']['subtotale']).replace(',', ""))
        return str(precioEfectivo)

    def getDiscount(self):
        precioDescuento = 0
        for d in self.data:
            if d['producto']['descuento'] != 'Error':
                precioDescuento += float(str(d['producto']['descuento']).replace(',', ""))
        return str(precioDescuento)





#testLinks=['https://www.intelaf.com/precios_stock_detallado.aspx?codigo=CAM-NXT-SMW4U2','https://www.imeqmo.com/shop/product/bx8070110400-procesador-intel-core-i5-10400-2-9ghz-10th-gen-12373','https://www.macrosistemas.com/productos/proyectores/epson,-proyector-power-lite-e10-,-h975a,-hdmi,-3lcd,-3600-lumenes-detail','https://www.intelaf.com/precios_stock_detallado.aspx?codigo=CAM-NXT-SMW4U2']
#testLinks=[['https://www.intelaf.com/precios_stock_detallado.aspx?codigo=DDR4-16G-CR32RG','1'],
 #           ['https://www.intelaf.com/precios_stock_detallado.aspx?codigo=VENTASUS-RSL24R','2']
  #          ]
#c = Recolector(testLinks)
#data = c.getData()
#for c in data:
#    print(c['tienda'],"|", c['producto']['nombre'])

#cash = c.getCashPrice()
#print(cash)
#print(c.getNormalPrice())