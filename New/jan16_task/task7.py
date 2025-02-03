import openpyxl

def create_report_data(file_path):
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Students Report Card"

    #Add messy data
    sheet.append(["Name", "Grades"])
    sheet.append(["Avipsha", "99"])
    sheet.append(["Asmita", "100"]) 
    sheet.append(["Yangji", "95"]) 
    sheet.append(["Prabhu", "89"]) 

    workbook.save(file_path)
    print("Report data created successfully.")

file_path = "report_data.xlsx"
create_report_data(file_path)

