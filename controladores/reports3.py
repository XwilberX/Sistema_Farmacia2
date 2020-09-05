from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
styles = getSampleStyleSheet()
doc = SimpleDocTemplate("simple_table.pdf", pagesize=letter)
elements = []

data= [['00', '01', '02', '03', '04'],
       ['10', Paragraph('Here is large field retrieve from database', styles['Normal']), '12', '13', '14'],
       ['20', '21', '22', '23', '24'],
       ['30', '31', '32', 'Here is second value', '34']]
t=Table(data)
elements.append(t)
doc.build(elements)