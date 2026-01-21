import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
from pdf_text_extractor import extract_text_from_pdf

load_dotenv()

api_key = os.getenv("GOOGLE-GEMINI-API-KEY")
if not api_key:
    raise ValueError("GOOGLE_GEMINI_API not found") 

genai.configure(api_key= api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")

st.header("Resume Matcher with Google Gemini")

st.subheader("Tips to use the App")

tips = """
- Upload a PDF resume using the uploader below.
- The app will extract text from the PDF and generate a summary using Google Gemini.
- Review the generated summary displayed on the app.
"""
st.markdown(tips)

st.sidebar.header("Upload your Resume", divider="green")
st.sidebar.subheader("Upload a PDF resume to get started.")
pdf_doc = st.sidebar.file_uploader("Upload a PDF Resume", type="pdf")

pdf_text = ""
if pdf_doc is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(pdf_doc.getbuffer())
    pdf_text = extract_text_from_pdf("temp_resume.pdf")
    st.sidebar.success("PDF uploaded and text extracted successfully!")

else:
    st.sidebar.info("Please upload a PDF resume to proceed.")

job_description = st.text_area("Enter Job Description", height=150)


prompt = f'''Assuming you are an expert in job skill matching and profile short listing.
You have the resume = {pdf_text} and job description = {job_description}. Using this data generate the
output on the following otline

* Calculate and show the ATS score. Discuss matching and non matching keywords (max 2 line discussion).
* Claculate and show the chances of selection of profile (One line discussion)
* Perform SWOT analysis and discuss in bullet points.
* Discuss in bullet points what the positives in the resume that will help in getting shortlisted.
* Discuss in bullet points what other things can be mentioned and discussed in resume.
* Prepare two revised resume's for this particular job description with chances of selection 
being maximised while implementing all the points discussed above.
* Prepare these resume in such a way that it can be copied and pasted in word and generate pdf.'''

if job_description:
    if pdf_text == None:
        st.warning("Please upload a PDF resume to proceed.")

    else:
        with st.spinner("Generating summary..."):
            response = model.generate_content(prompt)

        st.subheader("Generated Summary")
        st.markdown(response.text)