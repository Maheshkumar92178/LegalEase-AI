import streamlit as st
from datetime import date

# -----------------------------
# LegalEase - Simple Legal Document Generator
# -----------------------------

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="centered"
)

st.title("⚖️ LegalEase")
st.subheader("Simple Legal Document Generator")

st.write("Fill in the details below to generate a basic legal document.")

# -----------------------------
# User Details
# -----------------------------

name = st.text_input("Your Name")

email = st.text_input("Email")

document_type = st.selectbox(
    "Select Document Type",
    [
        "Rental Agreement",
        "Affidavit",
        "Authorization Letter",
        "Legal Notice",
        "General Agreement"
    ]
)

other_party = st.text_input("Other Party Name")

details = st.text_area(
    "Enter the details of the document",
    height=180
)

document_date = st.date_input(
    "Document Date",
    value=date.today()
)

# -----------------------------
# Generate Document
# -----------------------------

if st.button("Generate Document", type="primary"):

    if not name:
        st.error("Please enter your name.")
        st.stop()

    if not details:
        st.error("Please enter the document details.")
        st.stop()

    document = f"""
LEGAL DOCUMENT
===============

Document Type:
{document_type}

Date:
{document_date}

First Party:
{name}

Email:
{email}

Other Party:
{other_party}

DETAILS
-------

{details}


DECLARATION
-----------

I, {name}, confirm that the information provided above
is true and correct to the best of my knowledge.

Signature:

________________________
{name}
"""

    st.success("Document generated successfully!")

    st.text_area(
        "Generated Document",
        document,
        height=400
    )

    st.download_button(
        label="Download Document",
        data=document,
        file_name="LegalEase_Document.txt",
        mime="text/plain"
    )