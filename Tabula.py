import tabula
import os
# read PDF file
tables = tabula.read_pdf("1710.05006.pdf", pages="all")

# save them in a folder
folder_name = "tables"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
# iterate over extracted tables and export as excel individually
'''for i, table in enumerate(tables, start=1):
    table.to_excel(os.path.join(folder_name, f"table_{i}.xlsx"), index=False)'''

# convert all tables of a PDF file into a single CSV file
# supported output_formats are "csv", "json" or "tsv"
tabula.convert_into("1710.05006.pdf", "output.csv", output_format="csv", pages="all")