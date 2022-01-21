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
            if d['producto']['precion'] != 'Error':
                precioNormal += float(str(d['producto']['precion']).replace(',', ""))

        return str(precioNormal)

    def getCashPrice(self):
        precioEfectivo = 0;
        for d in self.data:
            if d['producto']['precioe'] != 'Error':
                precioEfectivo += float(str(d['producto']['precioe']).replace(',', ""))
        return str(precioEfectivo)

    def getDiscount(self):
        precioDescuento = 0
        for d in self.data:
            if d['producto']['descuento'] != 'Error':
                precioDescuento += float(str(d['producto']['descuento']).replace(',', ""))
        return str(precioDescuento)





#testLinks=['https://www.intelaf.com/precios_stock_detallado.aspx?codigo=CAM-NXT-SMW4U2','https://www.imeqmo.com/shop/product/bx8070110400-procesador-intel-core-i5-10400-2-9ghz-10th-gen-12373','https://www.macrosistemas.com/productos/proyectores/epson,-proyector-power-lite-e10-,-h975a,-hdmi,-3lcd,-3600-lumenes-detail','https://www.intelaf.com/precios_stock_detallado.aspx?codigo=CAM-NXT-SMW4U2']
#testLinks=['https://www.imeqmo.com/shop/product/bx8070110100f-procesador-intel-core-i3-10100f-3-6ghz-10th-gen-13250?category=11',
#            'https://www.imeqmo.com/shop/product/h410m-h-motherboard-gigabyte-h410m-h-socket-lga1200-10th-gen-2xddr4-micro-atx-venta-con-equipo-12522?category=10',
#            'https://www.imeqmo.com/shop/product/sa400s37-960g-unidad-ssd-2-5-960gb-kingston-a400-500mbs-8735?category=144',
#            'https://www.imeqmo.com/shop/product/st2000dm008-disco-duro-3-5-2tb-seagate-barracuda-7200rpm-10818?category=23',
#            'https://www.imeqmo.com/shop/product/ct4g4dfs8266-memoria-ddr4-dimm-4gb-crucial-2666mhz-10805?category=12',
#            'https://www.imeqmo.com/shop/product/31ve060-0004p-fuente-de-poder-600w-cougar-vte600-80-plus-bronce-10683?category=28',
#            'https://www.imeqmo.com/shop/product/lcaz-120r-argb-enfriador-liquido-120mm-azza-blizzard-argb-13359?category=150',
#            'https://www.imeqmo.com/shop/product/3mfcb120-0001-ventilador-cougar-vortex-fcb-rgb-120mm-15573?category=150',
#            'https://www.imeqmo.com/shop/product/tuf-rtx3080ti-12g-gaming-tarjeta-de-video-12gb-gddr6x-asus-geforce-rtx-3080-ti-lhr-tuf-gaming-hdmi-dp-pcie-4-0-14853?category=19',
#            'https://www.imeqmo.com/shop/product/106amt0003-03-case-gaming-cougar-panzer-evo-rgb-full-torre-vidrio-templado-e-atx-sin-fuente-9785?category=9'
#            ]
#c = Recolector(testLinks)
#data = c.getData()

#for c in data:
#    print(c['tienda'],"|", c['producto']['nombre'])