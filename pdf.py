import PyPDF2
import re


def extract_grand_titres_from_pdf(file_path):
    grand_titres = []
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page_text = pdf_reader.pages[page_number].extract_text()

            # Recherche des grands titres sur la page
            grand_titres_page = re.findall(r'^([IV]+|[1-5]+|[a-e]+)\.\s+(.*?)$', page_text, flags=re.MULTILINE)
            grand_titres.extend(grand_titres_page)
    return grand_titres


# Exemple d'utilisation
pdf_file_path = 'leetCode/ik.pdf'
titres = extract_grand_titres_from_pdf(pdf_file_path)
for titre in titres:
    print(titre[0], titre[1])
