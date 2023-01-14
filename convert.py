from pdf2image import convert_from_path

pages = convert_from_path('note.pdf')

for i, page in enumerate(pages):
    file_name = "note-{:03d}".format(i + 1) + ".png"
    page.save("./png/" + file_name, "PNG")