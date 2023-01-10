from fpdf import FPDF

class CS50():
    def __init__(self, my_name):
        self._cs50 = FPDF()
        self._cs50.add_page()
        self._cs50.set_font("helvetica", "B", 45)
        self._cs50.cell(0, 60, "CS50 Shirtificate", align="C")
        self._cs50.image("shirtificate.png", x=0, y=70)
        self._cs50.set_font_size(27)
        self._cs50.set_text_color(255, 255, 255)
        self._cs50.text(x=46, y=140, txt=f"{my_name} took CS50")

    def save(self, my_name):
        self._cs50.output(my_name)

my_name = input("Name: ")
cs50 = CS50(my_name)
cs50.save("shirtificate.pdf")
