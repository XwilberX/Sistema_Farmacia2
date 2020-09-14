from reportlab.platypus import (BaseDocTemplate, Paragraph, Spacer,
                            PageBreak, Frame, PageTemplate, NextPageTemplate)
from reportlab.pdfgen import canvas
from reportlab.lib import pagesizes, units, styles, enums

class Report(object):
    def __init__(self, stream, sections):
        self.stream = stream
        self.sections = sections
        w, h = pagesizes.A4
        self._width = w
        self._height = h
        self._story = []
        self._doc = None
        self._canvas = canvas.Canvas(self.stream)
        self._stylesheet = styles.getSampleStyleSheet()

    def generate(self):
        '''Generate the report'''
        self._doc = BaseDocTemplate(self.stream,
                                    pagesize=(self._width, self._height),
                                    showBoundary=True
                                    )
        # Start with the coverpage, then create a new page for each section.
        self.coverpage()
        for i, p in enumerate(self.sections):
            self.render_section(i, p)
        self._doc.build(self._story)
        self._canvas.save()

    def coverpage(self):
        '''Draw the cover page'''
        frame = Frame(0, 0, self._width, self._height)
        self._doc.addPageTemplates(PageTemplate(id='cover', frames=[frame]))
        self._story.append(PageBreak())
        # The cover page just has some drawing on the canvas.
        self._canvas.saveState()
        self._canvas.setFont('Helvetica', 16)
        self._canvas.drawCentredString(self._width / 2.0, self._height - 108,
                                       "This is the first page")
        self._canvas.restoreState()

    def render_section(self, num, text):
        '''Put stuff on the canvas that belong to this section.'''
        frame = Frame(0, 0, self._width, self._height, showBoundary=1)
        self._doc.addPageTemplates(PageTemplate(id='section-%d' % num,
                                                frames=[frame]))
        h1 = self._stylesheet['Heading1']
        h1.alignment = enums.TA_CENTER
        frames = [NextPageTemplate('section-%d' % num),
                  Paragraph(self.sections[num], h1),
                  Spacer(1, units.inch * 0.2),
                  PageBreak()]
        self._story.extend(frames)


if __name__ == '__main__':
    Report('report.pdf', "Why is this not showing?".split(" ")).generate()