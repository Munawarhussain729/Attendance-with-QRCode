import pandas as pd
import qrcode



def GenerateQR(employee_name, laptop):
    laptop_str = str(laptop) if pd.notnull(laptop) else ""
    data = "Employee Name: " + employee_name + "\nLaptop Details: "  + laptop_str
    img = qrcode.make(data)
    img.save(employee_name + '.png')


# Read the Excel sheet
df = pd.read_excel('./Machines Allocation Record.xlsx')

# Iterate over each row
for index, row in df.iterrows():
    employee_name = row['Employee_Name']
    laptop = row['Laptop']

    # Check if there is a value in the "Laptop" column
    if pd.notnull(laptop):
        # Call the function
        GenerateQR(employee_name, laptop)
