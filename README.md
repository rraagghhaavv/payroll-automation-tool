# 🧾 Payroll Automation Tool – Python

This project automates the generation of employee payslips using Python.

## 🔧 Features
- Reads employee data from Excel
- Calculates tax and net salary
- Generates personalized PDF payslips using ReportLab
- Saves all PDFs into a structured folder

## 📂 Input Format
An Excel file (`employees.xlsx`) with the following columns:
- Name
- Gross Salary
- Tax %

## 🖥 Tech Used
- Python
- Pandas
- ReportLab
- Excel (via OpenPyXL)

## 📦 Output
PDF files named like: `Raghav_Sood_Payslip.pdf` stored in `payslips/` folder.

## 📌 How to Run
```bash
pip install pandas reportlab openpyxl
python project1.py
# payroll-automation-tool
Python project to automate payslip generation from Excel using ReportLab

📣 Author  
Raghav Sood  
Backend Automation | Python | Excel Integration

