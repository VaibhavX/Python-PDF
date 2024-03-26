from PyPDF2 import PdfReader
import PyPDF2

print("Reading the PDF file")

first_name="Test"
middle_initial="A"
last_name="User"

user_email="test@test.com"

pdf_file = open('SDNS-01.pdf', 'rb')
reader=PdfReader(pdf_file)
print(reader.pages)

print(f'No of pages: {len(reader.pages)}')
# for page in reader.pages:
#     print(page.extract_text())
#print(f'first page content: \n{reader.pages[0].extract_text()}')

first_page = reader.pages[0]

applicant_name = first_name+", "+middle_initial+", "+last_name


fields = reader.get_fields()

for field_name, field_value in fields.items():
    # if field_value{'/TU'} == "PART 1 - IDENTIFICATION INFORMATION.   1.  APPLICANT'S NAME: (First, Middle Initial, Last Name)":
    #     print(field_name)
    #print(f"Fillable field: {field_name} - Value {field_value}")
    print(type(field_value))
    break

writer = PyPDF2.PdfWriter()
writer.add_page(first_page)
writer.update_page_form_field_values(writer.pages[0], {"TextField1[0]": "Jane, Doe"})
writer.add_page(reader.pages[1])
writer.add_page(reader.pages[2])
with open("VA_Form_Filled.pdf", "wb") as output_stream:
    writer.write(output_stream)

with open('VA_Form_Filled.pdf', 'rb') as temp_pdf:
    pdf_reader = PyPDF2.PdfReader(temp_pdf)

    # Create a new PDF writer
    pdf_writer = PyPDF2.PdfWriter()

    # Add each page (flattened) to the new PDF
    for page in pdf_reader.pages:
        #page = page.flatten_fields()  # Flatten the form fields
        pdf_writer.add_page(page)
    pdf_writer._root_object["/AcroForm"].update({NameObject("/NeedAppearances"): BooleanObject(False)})

    # Save the final PDF as "DL_Application_Jane.pdf"
    with open('FINAL_Output.pdf', 'wb') as final_output:
        pdf_writer.write(final_output)

# for field in first_page['/Annots']:
#     if field.subtype == '/FormField':
#         # Check if the field name matches 'Applicant Name' (replace if needed)
#         if field.get('/FieldName', None) == "1. APPLICANT'S NAME: (First, Middle Initial, Last Name)":
#             field.update({'/V': applicant_name})  # Set value for 'Applicant Name'

# if "/Annots" in first_page:
#     for annot in first_page["/Annots"]:
#         subtype = annot.get_object()["/Subtype"]
#         if subtype == "/Text":
#             print(annot.get_object()["/Contents"])


# for page in reader.pages:
#     if "/Annots" in page:
#         print(page["/Annots"])

#if '/NeedAppearances' in page.annots:




# for page in reader.pages:
#     print(page)

# for page in reader.pages:
#     if "/Annots" in page:
#         for annot in page["/Annots"]:
#             subtype = annot.get_object()["/Subtype"]
#             if subtype == "/Text":
#                 print(annot.get_object()["/Contents"])