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
styles = getSampleStyleSheet()
styleN = styles["BodyText"]
styleN.alignment = TA_LEFT
width, height = A4
logo = 'C:\\Users\\infrabyte\\Pictures\\github\\Sistema_FarmaciaInfra\\imagenes\\salud_logo.png'
elements = []
print(f'Height={height}')
imgw = imgh = 100
im = Image(logo, width=imgw, height=imgh)
im.hAlign = 'LEFT'
elements.append(im)

headstyle = ParagraphStyle(
    name='MyHeader',
    fontName='Helvetica-Bold',
    fontSize=16,
    leading =10
)
doctorstyle = ParagraphStyle(
    name='MyDoctorHeader',
    fontName='Helvetica',
    fontSize=13,
    leading =10
)
data = [[Paragraph("Dr John Doe's ENT Clinic", style = headstyle)], [Paragraph("Dr John Doe", style = doctorstyle)], [Paragraph("ENT Specialist", style = doctorstyle)], [Paragraph("Registration No. ", style = doctorstyle)]]
elements.append(Table(data, repeatRows=1))
line1 = ("Name", "Test", "Age", "20yr")
line2 = ("MRD No.", "18","Date", "14-11-2018")
line3 = ("No.","#", "Doctor", "Dr.John Doe")
data=[line1,line2, line3]
patientdetailstable = Table(data)
patientdetailstable.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (4, 0), '#CFEAD4'),
    ('BACKGROUND', (0, 2), (4, 2), '#CFEAD4'),
    ('BOX',(0,0),(-1,-1), 0.5, '#CFEAD4'),
    ('GRID',(0,0),(-1,-1), 0.5, colr(12, 43, 8)),
]))
elements.append(patientdetailstable)
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