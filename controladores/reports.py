from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

class GeneretReport():
    def export(data):
        #print(data)
        doc = SimpleDocTemplate("test_report_lab.pdf", pagesize=A4, rightMargin=30, leftMargin=30, topMargin=30,
                                bottomMargin=18)
        doc.pagesize = landscape(A4)
        elements = []

        #TODO: Get this line right instead of just copying it from the docs
        style = TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                            ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                            ('VALIGN', (0, 0), (0, -1), 'TOP'),
                            ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                            ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                            ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                            ])

        # Configure style and word wrap
        s = getSampleStyleSheet()
        s = s["BodyText"]
        s.wordWrap = 'CJK'
        data2 = [[Paragraph(cell, s) for cell in row] for row in data]
        t = Table(data2)
        t.setStyle(style)

        # Send the data and build the file
        elements.append(t)
        doc.build(elements)