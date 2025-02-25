import streamlit as st
from docx2pdf import convert
import os
import tempfile

def main():
    st.title("Word to PDF Converter")
    st.write("Upload a Word document (.docx) and convert it to PDF")

    # File uploader
    uploaded_file = st.file_uploader("Choose a Word document", type=['docx'])

    if uploaded_file is not None:
        # Create a temporary directory to store the files
        with tempfile.TemporaryDirectory() as temp_dir:
            # Save the uploaded file
            docx_path = os.path.join(temp_dir, uploaded_file.name)
            with open(docx_path, 'wb') as f:
                f.write(uploaded_file.getbuffer())

            # Create output PDF path
            pdf_path = os.path.join(temp_dir, os.path.splitext(uploaded_file.name)[0] + '.pdf')

            # Convert button
            if st.button('Convert to PDF'):
                with st.spinner('Converting...'):
                    try:
                        # Convert DOCX to PDF
                        convert(docx_path, pdf_path)

                        # Read the PDF file
                        with open(pdf_path, 'rb') as pdf_file:
                            pdf_data = pdf_file.read()

                        # Create download button
                        st.success('Conversion completed!')
                        st.download_button(
                            label="Download PDF",
                            data=pdf_data,
                            file_name=os.path.splitext(uploaded_file.name)[0] + '.pdf',
                            mime='application/pdf'
                        )
                    except Exception as e:
                        st.error(f'An error occurred: {str(e)}')

if __name__ == '__main__':
    main()
