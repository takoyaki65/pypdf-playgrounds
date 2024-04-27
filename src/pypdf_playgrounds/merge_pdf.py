import sys
from pypdf import PdfReader, PdfWriter

def merge_pdfs(pdf_files: list[str], output_file: str) -> None:
    pdf_writer = PdfWriter()

    for pdf_file in pdf_files:
        pdf_reader = PdfReader(pdf_file)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    
    with open(output_file, "wb") as f:
        pdf_writer.write(f)
    
    print(f"PDFs merged into {output_file}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python merge_pdf.py <pdf_file1> <pdf_file2> ... <output_file>")
        sys.exit(1)

    output_file = sys.argv[-1]
    pdf_files = sys.argv[1:-1]

    merge_pdfs(pdf_files, output_file)
