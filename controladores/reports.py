from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

canvas = canvas.Canvas("form.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)

canvas.drawString(30, 750, 'CARTA DE PRUEBA')
canvas.drawString(30, 735, 'RICARDOGEEK.COM')
canvas.drawString(500, 750, "27/10/2016")
canvas.line(480, 747, 580, 747)

canvas.drawString(275, 725, 'ESTIMADO:')
canvas.drawString(500, 725, "<NOMBRE>")
canvas.line(378, 723, 580, 723)

canvas.drawString(30, 703, 'ETIQUETA:')
canvas.line(120, 700, 580, 700)
canvas.drawString(120, 703, "<ASUNTO DE LA CARTA GENERICO>")

canvas.save()