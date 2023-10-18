import PyPDF2

merger = PyPDF2.PdfWriter()

for pdf in ["1.pdf", "sample.pdf", "dummy.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()