import pandas as pd
import jinja2 as j2
from weasyprint import HTML

df = pd.read_excel("purchase_list.xlsx") # Read the purchase list
grocery_list = {}

def update_grocery_list(item):
    if item in grocery_list:
        grocery_list[item] += 1
    else:
        grocery_list[item] = 1


for index, row in df.iterrows(): # Iterate through the rows
    if index == 0:
        continue # Skip the header row
    template = j2.Template(open("label.html").read()) # Read the template
    name = row.iloc[5]
    its = row.iloc[6]
    phone = row.iloc[7]
    city = row.iloc[9]
    contribution = row.iloc[10]
    items= []

    if row.iloc[13] == "Yes":
        items.append("Salt & Pepper")
        update_grocery_list("Salt & Pepper")
    if row.iloc[14] == "Yes":
        items.append("Kilonji")
        update_grocery_list("Kilonji")
    if row.iloc[15] == "Yes":
        items.append("Honey")
        update_grocery_list("Honey")
    if row.iloc[16] == "Yes":
        items.append("Egg Tray 2.5 Dozen")
        update_grocery_list("Egg Tray 2.5 Dozen")
    if row.iloc[17] == "Yes":
        items.append("Dates")
        update_grocery_list("Dates")
    if row.iloc[18] == "Yes":
        items.append("Jam")
        update_grocery_list("Jam")
    if(row.iloc[19] == "Yes"):
        items.append("Butter")
        update_grocery_list("Butter")
    if(row.iloc[20] == "Yes"):
        items.append("Evaporated Milk Can x2")
        update_grocery_list("Evaporated Milk Can x2")
    
    # Tea/coffee
    items.append(row.iloc[21])
    update_grocery_list(row.iloc[21])

    # Bread
    items.append(row.iloc[22])
    update_grocery_list(row.iloc[22])

    # Biscuit
    items.append(row.iloc[23])
    update_grocery_list(row.iloc[23])

    # Sugar
    items.append(row.iloc[24] + " Sugar")
    update_grocery_list(row.iloc[24] + " Sugar")
    
    html = template.render(name=name, its=its, phone=phone, city=city, items=items, contribution=contribution) # Render the template with the row data
    with open(f"generated/purchase_{index+1}_{name}.html", "w") as f: # Write the HTML to a file
        f.write(html)
    pdfhtml = HTML(filename=f"generated/purchase_{index+1}_{name}.html").write_pdf(f"pdfs/purchase_{index+1}_{name}.pdf") # Convert the HTML to PDF


print(grocery_list) # Print the grocery list


ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILBPhJbHbp8r5YNG6FS5SFDnzeinWYMd+FFl98iCKqy9 vizkid2005@gmail.com
