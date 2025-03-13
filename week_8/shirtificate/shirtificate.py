#!/usr/bin/env python3
from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("helvetica", style = "B", size = 30)
    pdf.cell(200, 50, "CS50 Shirtificate", new_x = "LMARGIN", new_y = "NEXT", align = "C")

    pdf.image("shirtificate.png", x = 15, y = 80, w = 180)

    pdf.set_font("helvetica", style = "B", size = 25)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 180, f"{name} took CS50", align = "C")

    pdf.output("shirtificate.pdf")
   

if __name__ == "__main__":
    main()
