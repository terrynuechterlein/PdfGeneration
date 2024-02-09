from fpdf import FPDF

# creates an empty pdf instance (no pages).
# portrait orientation.
# unit is used for text
pdf = FPDF(orientation='P', unit='pt', format='A4')

# adds a page to pdf
pdf.add_page()

pdf.image('meditation.png', w=100, h=100)

pdf.set_font(family='Times', style='B', size=24)
# to add text use cell method. 0 width makes it occupy entire width of row
pdf.cell(w=0, h=50, txt="Importance of Meditation", align='C', ln=1)

pdf.set_font(family='Times', size=14)
txt1="""Meditation is vital for mental health, offering a retreat from the chaos of daily life. It improves focus, reduces stress, and enhances emotional well-being by cultivating mindfulness and a sense of inner peace. Regular practice can lead to better sleep, lower anxiety levels, and an overall increase in happiness and life satisfaction"""
pdf.multi_cell(w=0, h=15, txt=txt1, align='L')

pdf.set_font(family='Times', style='I', size=12)
pdf.cell(w=0, h=50, txt="-Terry Nuechterlein", align='R', ln=1)
pdf.output('output.pdf')
