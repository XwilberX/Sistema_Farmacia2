import os
import pandas as pd
import numpy as np
import reportlab.platypus
from reportlab.pdfgen import canvas
import reportlab.lib.styles
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.pagesizes import letter, landscape



class GeneretReport():
    width, height = A4

    def coord(x, y, unit=1):
        x, y = x * unit, height - y * unit
        return x, y

    def export(data):
        #print(data)
        reportoutputfilepath = os.path.join('.\\test.pdf')


        pdf_file = reportlab.platypus.SimpleDocTemplate(
            reportoutputfilepath,
            pagesize=landscape(letter),
            rightMargin=10,
            leftMargin=10,
            topMargin=38,
            bottomMargin=23
        )

        #TODO: Get this line right instead of just copying it from the docs
        ts_tables = [
            ('BACKGROUND', (0, 0), (6,0), colors.orange),
            ('ALIGN', (4, 0), (-1, -1), 'CENTER'),
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.purple),
            ('FONT', (0, 0), (-1, 0), 'Times-Bold'),
            # ('LINEABOVE', (0, -1), (-1, -1), 1, colors.purple),
            # ('FONT', (0, -1), (-1, -1), 'Times-Bold'),
            ('BACKGROUND', (1, 1), (-2, -2), colors.white),
            ('TEXTCOLOR', (0, 0), (1, -1), colors.black),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
        ]

        # Here is where you put repeatRows=1
        table = reportlab.platypus.Table(data, colWidths=(10 * mm, 15 * mm, 22 * mm, 20 * mm, 23 * mm, 20 * mm, 20 * mm))
        table_style = reportlab.platypus.TableStyle(ts_tables)
        table.setStyle(table_style)
        # elements = []
        # elements.append(table)
        #
        # # Build the PDF
        # pdf_file.build(elements)

        c = canvas.Canvas("a.pdf", pagesize=A4)
        table.wrapOn(c, width, height)
        table.drawOn(c, *coord(1.8, 9.6, cm))
        c.save()
        os.startfile(reportoutputfilepath)
        print(reportoutputfilepath)