import pandas as pd
import jinja2 as j2
from weasyprint import HTML
import argparse
import os
from pathlib import Path

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate packing labels from an Excel file')
parser.add_argument('input_file', help='Path to the Excel file to process')
args = parser.parse_args()

# Create output directories if they don't exist
Path("generated").mkdir(exist_ok=True)
Path("pdfs").mkdir(exist_ok=True)

df = pd.read_excel(args.input_file, dtype=str) # Read the purchase list with all values as strings
# Replace NaN/None values with empty strings
df = df.fillna("")

# Log first and last rows to verify data
print("\n" + "="*50)
print("DATA VERIFICATION")
print("="*50)
print(f"\nTotal rows in dataframe: {len(df)}")
print("\nFIRST ROW (index 0):")
print(df.iloc[0])
print(f"\nLAST ROW (index {len(df)-1}):")
print(df.iloc[-1])
print("="*50 + "\n")

grocery_list = {}

# Load template once before the loop
template = j2.Template(open("label.html").read())

def update_grocery_list(item):
    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1


for index, row in df.iterrows(): # Iterate through the rows
    if row.iloc[13] == "No":
        continue # Skip the header row and RSVP as no
    
    # Note: Consider using column names instead of iloc for better maintainability
    # e.g., row['Name'] instead of row.iloc[7]
    name = row.iloc[6]
    its = row.iloc[7]
    phone = row.iloc[8]
    city = row.iloc[10]
    contribution = row.iloc[11]
    items= []

    if row.iloc[14] == "Yes":
        items.append("Salt & Pepper")
        update_grocery_list("Salt & Pepper")
    if row.iloc[15] == "Yes":
        items.append("Kilonji")
        update_grocery_list("Kilonji")
    if row.iloc[16] == "Yes":
        items.append("Honey")
        update_grocery_list("Honey")
    if row.iloc[17] == "Yes":
        items.append("Egg Tray 2.5 Dozen")
        update_grocery_list("Egg Tray 2.5 Dozen")
    if row.iloc[18] == "Yes":
        items.append("Dates")
        update_grocery_list("Dates")
    if row.iloc[19] == "Yes":
        items.append("Jam")
        update_grocery_list("Jam")
    if(row.iloc[20] == "Yes"):
        items.append("Butter")
        update_grocery_list("Butter")
    if(row.iloc[21] == "Yes"):
        items.append("Evaporated Milk Can x2")
        update_grocery_list("Evaporated Milk Can x2")
    if(row.iloc[22] == "Yes"):
        items.append("Jaggery")
        update_grocery_list("Jaggery")
    
    # Tea/coffee
    if(row.iloc[23] != ""):
        items.append(row.iloc[23])
        update_grocery_list(row.iloc[23])

    # Bread
    if(row.iloc[24] != ""):
        items.append(row.iloc[24])
        update_grocery_list(row.iloc[24])

    # Biscuit
    if(row.iloc[25] != ""):
        items.append(row.iloc[25])
        update_grocery_list(row.iloc[25])

    # Sugar
    if(row.iloc[26] != ""):
        items.append(row.iloc[26] + " Sugar")
        update_grocery_list(row.iloc[26] + " Sugar")
    
    # Oil/Ghee
    if(row.iloc[27] != ""):
        items.append(row.iloc[27])
        update_grocery_list(row.iloc[27])
    
    # Oats / Cornflakes
    if(row.iloc[28] != ""):
        items.append(row.iloc[28])
        update_grocery_list(row.iloc[28])
    

    html = template.render(name=name, its=its, phone=phone, city=city, items=items, contribution=contribution) # Render the template with the row data
    with open(f"generated/purchase_{index+1}_{name}.html", "w") as f: # Write the HTML to a file
        f.write(html)

    # Convert the HTML to PDF using WeasyPrint
    HTML(string=html).write_pdf(f"pdfs/purchase_{index+1}_{name}.pdf")

# Print and save grocery list
print("\n" + "="*50)
print("GROCERY LIST SUMMARY")
print("="*50)
for item, count in sorted(grocery_list.items()):
    print(f"{item:40} x {count}")
print("="*50)

# Save grocery list to file
with open("generated/grocery_list.txt", "w") as f:
    f.write("GROCERY LIST SUMMARY\n")
    f.write("="*50 + "\n")
    for item, count in sorted(grocery_list.items()):
        f.write(f"{item:40} x {count}\n")
    f.write("="*50 + "\n")
    f.write(f"\nTotal unique items: {len(grocery_list)}\n")

print(f"\nGenerated {len(df)-1} labels and saved grocery list to generated/grocery_list.txt")
