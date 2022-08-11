import camelot

# PDF file to extract tables from
file = "foo.pdf"
tables = camelot.read_pdf(file)
print("Total tables extracted:", tables.n)
# print the first table as Pandas DataFrame
print(tables[0].df)
# export individually as CSV
# tables[0].to_csv("foo.csv")
# or export all in a zip
tables.export("foo.csv", f="csv", compress=True)
