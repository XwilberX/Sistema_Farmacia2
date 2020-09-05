def colr(x, y, z):
    return (x/255, y/255, z/255)
import reportlab
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from reportlab.platypus import SimpleDocTemplate, TableStyle, Paragraph, Image, Spacer, Frame, Paragraph
from reportlab.platypus.tables import Table
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib.units import mm, cm

headstyle = ParagraphStyle(
    name='MyHeader',
    fontName='Helvetica-Bold',
    fontSize=14,
    leading =10,
    spaceAfter = 4
)
doctorstyle = ParagraphStyle(
    name='MyDoctorHeader',
    fontName='Helvetica',
    fontSize=10,
    #leading =10,
    spaceAfter = 4
)

styles = getSampleStyleSheet()
styleN = styles["Normal"]
styleN.alignment = TA_LEFT
width, height = A4
logo = 'loog.jpg'
lg2 = 'descarga.png'

elements = []

imgw = imgh = 50

im = Image(logo, width=imgw+60, height=imgh)
im.hAlign = 'LEFT'

lg = Image(lg2, width=imgw+60, height=imgh)
lg.hAlign = 'RIGHT'
col1 = Table([[im]])

title = [[Paragraph("INSTITUTO DE SALUD", style = headstyle)], [Paragraph("SALIDA DE ALMACEN", style = headstyle)]]

col2 = Table([[lg]], repeatRows=1)

tblrow1 = Table([[col1, title ,col2]])
tblrow1.setStyle(
    TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTRE'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
    ]))
elements.append(tblrow1)

colOne = [[Paragraph("Almacen: SIAL VIII", style = doctorstyle)], [Paragraph("Programa: COMPRA DIRECTA 2020", style = doctorstyle)],
           [Paragraph("Num Referencia: B445770", style = doctorstyle)], [Paragraph("Observaciones: N° DE S. 167", style = doctorstyle)],
          [Paragraph("Proveedor: VENDOGAS S.A DE C.V", style = doctorstyle)]
           ]

colTwo = [[], [], [Paragraph("Fecha Referencia: 30-may-2020", style = doctorstyle)], [], []]

colThree = [[Paragraph("Num Salida: Ed-60420040", style = doctorstyle)], [Paragraph("Pelido: 167", style = doctorstyle)],
           [Paragraph("Fecha Salida: 5-jun-2020", style = doctorstyle)], [],
          [Paragraph("RFC: VEN930917QT2", style = doctorstyle)]
           ]

tblrow2 = Table([[colOne, colTwo, colThree]])
tblrow2.setStyle(
    TableStyle([
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
        ('ALIGN',(2,0),(2,3),'RIGHT'),
        ('VALIGN', (2,0),(2,2), 'TOP'),
        ('VALIGN', (2,3),(2,3), 'BOTTOM'),
        #('BOX',(0,0),(-1,-1),2,colors.black),
        ('LINEBELOW', (0,-1), (-1,-1), 0.25, colors.black),
        # ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        # ('ALIGN', (2, 0), (2, 0), 'RIGHT'),
    ]))

elements.append(tblrow2)

# data = [[Paragraph("Dr John Doe's ENT Clinic", style = headstyle)], [Paragraph("Dr John Doe", style = doctorstyle)], [Paragraph("ENT Specialist", style = doctorstyle)], [Paragraph("Registration No. ", style = doctorstyle)]]
# elements.append(Table(data, repeatRows=1))
elements.append(Spacer(1, 20))




# We use paragraph style because we need to wrap text. We cant directly wrap cells otherwise
line1 = ["Sl.", "Medicine" , "Dose", "Freq", "Durn", "Note"]
drug1 = Paragraph('AUGMED Syrup 30ml (AMOXICILLIN 200MG + CLAVULANATE(CLAVULANIC ACID) 28.5MG)', styleN)
line2 = ["1", drug1, "1 Tab", "1-0-1", "5 days", ""]
line3 = ["2", drug1, "1 Tab", "1-0-1", "5 days", ""]
data=[line1,line2, line3]
for i in range(3,50):
    temp = [str(i), "Some Drug here", "5 ml", "1-0-1", "10 days", "No comments"]
    data.append(temp)

medstable = Table(data, repeatRows=1)
medstable.setStyle(TableStyle([
    ('VALIGN',(0,0),(-1,-1), 'TOP'),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('BACKGROUND', (0, 0), (-1, 0), colr(40, 196, 15)),
    ('GRID',(0,1),(-1,-1), 0.5, '#CFEAD4'),
                            ]))
elements.append(medstable)
doc = SimpleDocTemplate('output.pdf', pagesize=A4, rightMargin=20, leftMargin=20, \
    topMargin=20, bottomMargin=20, allowSplitting=1,\
    title="Prescription", author="MyOPIP.com")
doc.build(elements)