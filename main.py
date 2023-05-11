from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")
df_dict = df.to_dict()
# print(df_dict)

for index, row in df.iterrows():

    x= row["Pages"]
    for i in range(x):

        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(0,50,50)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 20, 200, 20)




pdf.output("output.pdf")