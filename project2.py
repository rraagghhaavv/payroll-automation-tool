import pandas as pd
from reportlab.pdfgen import canvas
import os
from datetime import datetime

# Load data from Excel
df = pd.read_excel("employees.xlsx")

# Create output folder
if not os.path.exists("payslips"):
    os.makedirs("payslips")

# Generate payslip for each employee
for index, row in df.iterrows():
    name = row['Name']
    gross_salary = row['Gross Salary']
    tax_percent = row['Tax %']
    
    tax_amount = gross_salary * (tax_percent / 100)
    net_salary = gross_salary - tax_amount

    filename = f"payslips/{name.replace(' ', '_')}_Payslip.pdf"
    c = canvas.Canvas(filename)
    c.setPageSize((600, 400))  # Optional: page size for layout

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 370, "JGC Technologies Pvt. Ltd.")

    # Sub-header
    c.setFont("Helvetica", 12)
    c.drawString(50, 340, f"Payslip for: {name}")
    c.drawString(400, 340, f"Date: {datetime.today().strftime('%d-%m-%Y')}")

    # Line separator
    c.line(50, 330, 550, 330)

    # Salary Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 300, "Salary Details:")

    c.setFont("Helvetica", 11)
    c.drawString(70, 280, f"Gross Salary: ₹{gross_salary}")
    c.drawString(70, 260, f"Tax Deducted (@{tax_percent}%): ₹{tax_amount}")
    c.drawString(70, 240, f"Net Salary: ₹{net_salary}")

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(50, 200, "This is a system-generated payslip. No signature required.")

    c.save()


    print("Payslips generated in 'payslips/' folder.")
