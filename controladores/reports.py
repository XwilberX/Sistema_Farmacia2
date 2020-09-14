from reportlab.lib.pagesizes import A4, letter
from reportlab.platypus import (BaseDocTemplate, PageTemplate,
                                NextPageTemplate, PageBreak, Frame, FrameBreak, Flowable, Paragraph,
                                Image, Spacer, TableStyle)
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.tables import Table
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus.flowables import TopPadder
from reportlab.lib.units import mm, cm, inch
from datetime import datetime
import os
from functools import partial

class Report():
    def __init__(self, *args):
        create(*args)



def header(canvas, doc, content):
    logo_image = '../imagenes/descarga.png'
    logo_image2 = '../imagenes/logo2.png'
    canvas.saveState()
    content.wrap(doc.width, doc.topMargin)
    canvas.drawImage(logo_image, 45, 750, width=100, preserveAspectRatio=True)
    canvas.drawImage(logo_image2, 420, 770, width=150, height= 50 ,mask='auto')
    content.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin + 10)
    #canvas.drawString(inch, 0.75 * inch, "Page %d" % doc.page)
    canvas.restoreState()

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Roman', 9)
    canvas.dradrawString(inch, 0.75 * inch, "Nombre y frima del entregador")
    canvas.restoreState()

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
        self.setFont('Vera', 9)
        self.setLineWidth(0.1)
        self.line(cm, 1.5 * cm, A4[0] - cm, 1.5 * cm)
        self.drawRightString(A4[0] - cm, 1 * cm, "Pg. %d de %d" % (self._pageNumber, page_count))

def foot1(canvas, doc):
    page_num = canvas.getPageNumber()
    text = "Pages #%s" % page_num
    canvas.drawRightString(200 * mm, 20 * mm, text)

def create(*args):
    print("llegoo")
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleH = styles['Heading1']

    pdfmetrics.registerFont(TTFont('Vera', '../Fuentes/Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraB', '../Fuentes/VeraBd.ttf'))
    pdfmetrics.registerFontFamily('Vera', normal='Vera', bold='VeraB')

    # Estilos parrafos del header en medio de las imagenes
    headstyle = ParagraphStyle(name='MyHeader', fontName='VeraB', fontSize=14, alignment=TA_CENTER)

    # Estilo de los parrafos que estan debajo de las imagenes
    prostyle = ParagraphStyle(name='MyDoctorHeader', fontName='Vera', fontSize=10, spaceAfter=4, alignment=TA_LEFT)
    prostyle2 = ParagraphStyle(name='MyDoctorHeader', fontName='Vera', fontSize=10, spaceAfter=4, alignment=TA_RIGHT)
    prostyleJ = ParagraphStyle(name='MyDoctorHeader', fontName='Vera', fontSize=10, spaceAfter=4, alignment=TA_JUSTIFY)
    styleT = ParagraphStyle(name='table', fontName='Vera', fontSize=8,alignment=TA_CENTER)

    footerstyle = ParagraphStyle(name='MyDoctorHeader', fontName='Vera',alignment=TA_CENTER ,fontSize=10, spaceAfter=4)

    now = datetime.now()
    outfilename = 'ReporteSal-{0}-{1}-{2}-{3}-{4}.pdf'.format(now.year, now.month, now.day, now.hour, now.second)
    outfilepath = os.path.join(os.path.expanduser("~"), "Documents/Reportes", outfilename)

    doc = BaseDocTemplate(outfilepath, pagesize=A4, rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=60)

    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height-2*cm, id='normal')
    header_content = Paragraph("<b>Instituto de salud</b>" + "<br/>" + "<b>Salida de almacen</b>" , headstyle)

    template = PageTemplate(id='test', frames=frame, onPage=partial(header, content=header_content))
    doc.addPageTemplates([template])

    colOne = [[Paragraph("<b>Salida de almacén con destino a:</b> " + args[1], style=prostyle)],
                      [Paragraph("<b>Numero de salida:</b> Preguntar", style=prostyle)],
                      [Paragraph("<b>Numero pedido:</b> " + str(args[2]), style=prostyle)]
                    ]

    colThree = [[Paragraph("<b>Fecha de solicitud:</b> " + args[3], style=prostyle2)],
                [Paragraph("<b>Fecha de surtimiento:</b> " + args[4], style=prostyle2)]
                ]

    tblrow2 = Table([[colOne, colThree]])
    tblrow2.setStyle(
        TableStyle([
            ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
            ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
            ('BOX', (0,0), (-1,-1), 0.25, colors.black),
            ('SPAN', (0,3), (1,3)),
        ]))


    text = []
    text.append(tblrow2)
    text.append(Spacer(1, 10))
    if not len(args[5]) > 0:
        text.append(Paragraph("<b>Observaciones:</b> No hay observaciones", style=prostyleJ))
    else:
        text.append(Paragraph("<b>Observaciones:</b> " + args[5], style=prostyleJ))

    data = args[0]
    newdata = []
    temp = []
    for i in range(len(data)):
        for j in range(len(data[1])):
            if j == 2:
                if i > 0:
                    desc = data[i][j]
                    temp.append(Paragraph(desc[:50] + "...", styleT))
                else:
                    temp.append(Paragraph(data[i][j], styleT))
            if j != 2:
                t = Paragraph(data[i][j], styleT)
                temp.append(t)
        newdata.append(temp)
        temp = []


    tableData = Table(newdata, repeatRows=1)
    tableData.setStyle(
        TableStyle([
            ('VALIGN',(0,0),(-1,-1), 'TOP'),
            ('TEXTCOLOR',(0,0),(-1,0),colors.white),
            ('BACKGROUND', (0, 0), (-1, 0), '#0097e6'),
            ('GRID',(0,1),(-1,-1), 0.5, '#CFEAD4'),
        ]))
    text.append(Spacer(1, 10))
    text.append(tableData)

    Fcol1 = [[Paragraph("Nombre y firma de entregado", style=footerstyle)]]
    Fcol2 = [[Paragraph("", style=footerstyle)]]
    Fcol3 = [[Paragraph("Nombre y firma de recicido", style=footerstyle)]]

    tblrow = Table([[Fcol1, Fcol2 ,Fcol3]])

    tblrow.setStyle(
        TableStyle([
            ('LINEABOVE', (0,0), (0,0), 0.25, colors.black),
            ('LINEABOVE', (2,0), (2,0), 0.25, colors.black),
        ])
    )


    text.append(TopPadder(tblrow))

    doc.build(text, canvasmaker=NumberedCanvas)

    os.startfile(outfilepath)