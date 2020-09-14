from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, TableStyle, Paragraph, Image, Spacer, Frame, Paragraph, BaseDocTemplate, PageTemplate, NextPageTemplate
from reportlab.platypus.tables import Table
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus.flowables import TopPadder
from reportlab.lib.units import mm, cm, inch
from faker import Faker
import pandas as pd
import os
from functools import partial

class Report():
    def __init__(self, **kwargs):
        """ Constructor """
        print('llego')
        # Lista donde se agregaran todos los elementos, parrafos tables etc
        self.elements = []
        self.styles = getSampleStyleSheet()

    def create(self):
        def footer(canvas, doc, content):
            canvas.saveState()
            w, h = content.wrap(doc.width, doc.topMargin)
            content.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)
            canvas.restoreState()

        self.doc = BaseDocTemplate('output.pdf', pagesize=A4, rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20,)
        frame = Frame(self.doc.leftMargin, self.doc.bottomMargin, self.doc.width, self.doc.height-2*cm, id='normal')
        footer_content = Paragraph("This is a multi-line header.  It goes on every page.  " * 6)
        template = PageTemplate(id='test', frames=frame, onPageEnd =partial(footer, content=footer_content))
        self.doc.addPageTemplates([template])
        self.createDocument()
        self.doc.build(self.elements, canvasmaker=NumberedCanvas)
        os.startfile('output.pdf')

    def createDocument(self):
        # Estilos parrafos del header en medio de las imagenes
        headstyle = ParagraphStyle(name='MyHeader', fontName='Helvetica-Bold', fontSize=14, leading=10, spaceAfter=4)

        # Estilo de los parrafos que estan debajo de las imagenes
        doctorstyle = ParagraphStyle(name='MyDoctorHeader', fontName='Helvetica', fontSize=10, spaceAfter=4)

        width, height = A4
        logo = 'loog.jpg'
        lg2 = 'descarga.png'

        # tamaños de las imagenes
        imgw = imgh = 50

        im = Image(logo, width=imgw+60, height=imgh, hAlign='LEFT')
        im2 = Image(lg2, width=imgw+60, height=imgh, hAlign='RIGHT')

        HeaderI1 = Table([[im]])
        HeaderTitle = [[Paragraph("INSTITUTO DE SALUD", style = headstyle)], [Paragraph("SALIDA DE ALMACEN", style = headstyle)]]
        HeaderI2 =  Table([[im2]])

        Header = Table([[HeaderI1, HeaderTitle ,HeaderI2]])
        Header.setStyle(
            TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('ALIGN', (0, 0), (0, 0), 'LEFT'),
                ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
            ])
        )
        
        self.elements.append(Header)

        colOne = [[Paragraph("Almacen: SIAL VIII", style=doctorstyle)],
                  [Paragraph("Programa: COMPRA DIRECTA 2020", style=doctorstyle)],
                  [Paragraph("Num Referencia: B445770", style=doctorstyle)],
                  [Paragraph("Observaciones: N° DE S. 167", style=doctorstyle)],
                  [Paragraph("Proveedor: VENDOGAS S.A DE C.V", style=doctorstyle)]
                ]

        colTwo = [[Paragraph("Fecha Referencia: 30-may-2020", style=doctorstyle)]]

        colThree = [[Paragraph("Num Salida: Ed-60420040", style=doctorstyle)],
                    [Paragraph("Pelido: 167", style=doctorstyle)],
                    [Paragraph("Fecha Salida: 5-jun-2020", style=doctorstyle)],
                    [Paragraph("RFC: VEN930917QT2", style=doctorstyle)]
                    ]

        tblrow2 = Table([[colOne, colTwo, colThree]])
        tblrow2.setStyle(
            TableStyle([
                ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
                ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
                ('ALIGN', (2, 0), (2, 3), 'RIGHT'),
                ('VALIGN', (2, 0), (2, 2), 'TOP'),
                ('VALIGN', (2, 3), (2, 3), 'BOTTOM'),
                ('LINEBELOW', (0, -1), (-1, -1), 0.25, colors.black)
            ]))

        self.elements.append(tblrow2)

        self.elements.append(Spacer(1, 10))

        faker = Faker()
        df = []
        for n in range(80):
            df.append({'Lat': faker.coordinate(center=74.0, radius=0.10),
                       'Lon': faker.coordinate(center=40.8, radius=0.10)
                       })

        df = pd.DataFrame(df)

        LisReport = [df.columns[:, ].values.astype(str).tolist()] + df.values.tolist()

        tableData = Table(LisReport, repeatRows=1)
        tableData.setStyle(
            TableStyle([
                ('VALIGN',(0,0),(-1,-1), 'TOP'),
                ('TEXTCOLOR',(0,0),(-1,0),colors.white),
                ('BACKGROUND', (0, 0), (-1, 0), '#0097e6'),
                ('GRID',(0,1),(-1,-1), 0.5, '#CFEAD4'),
            ]))
        tableData.split(10,40)
        self.elements.append(tableData)

        self.elements.append(TopPadder(tblrow2))


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(
                196 * mm,
                8 * mm,
                "Pag. %d de %d" % (self._pageNumber, page_count)
            )


if __name__ == "__main__":
    t = Report()
    t.create()