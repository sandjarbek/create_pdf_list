from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")
df_dict = df.to_dict()
# print(df_dict)

for index, row in df.iterrows():

    # set a heater
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0,50,50)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    # set a footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(100,50,50)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")




    x= row["Pages"]
    for i in range(x-1):
        pdf.add_page()
        # set a footer
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(100, 50, 50)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")




pdf.output("output.pdf")