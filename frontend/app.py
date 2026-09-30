import os
import requests
import streamlit as st
from dotenv import load_dotenv


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)

GENERATE_URL = f"{BACKEND_URL}/generate"


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "generated_document" not in st.session_state:
    st.session_state.generated_document = ""

if "editing" not in st.session_state:
    st.session_state.editing = False


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .document-preview {
        background-color: #111827;
        color: #f9fafb;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #374151;
        min-height: 400px;
        white-space: pre-wrap;
        overflow-y: auto;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">⚖️ LegalEase</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Legal Document Generator</div>',
    unsafe_allow_html=True
)

st.divider()


# ============================================================
# INPUT SECTION
# ============================================================

st.subheader("📄 Create Your Legal Document")

col1, col2 = st.columns(2)

with col1:

    document_type = st.text_input(
        "Document Type",
        placeholder="Example: NDA, Employment Contract, Lease Agreement"
    )

    parties = st.text_area(
        "Parties Involved",
        placeholder=(
            "Example:\n"
            "Jane Doe (Service Provider)\n"
            "TechNova Inc. (Client)"
        ),
        height=130
    )

with col2:

    dates = st.text_input(
        "Effective Date",
        placeholder="Example: April 10, 2025"
    )

    terms = st.text_area(
        "Terms & Conditions",
        placeholder=(
            "Enter each term separated by semicolon (;)\n\n"
            "Example:\n"
            "Payment within 30 days; "
            "Confidentiality must be maintained; "
            "Either party may terminate with 15 days notice"
        ),
        height=130
    )


additional_instructions = st.text_area(
    "Additional Instructions (Optional)",
    placeholder="Add any additional requirements for the document...",
    height=100
)


# ============================================================
# GENERATE DOCUMENT
# ============================================================

if st.button(
    "🚀 Generate Document",
    use_container_width=True,
    type="primary"
):

    if not document_type.strip():
        st.error("Please enter the document type.")

    elif not parties.strip():
        st.error("Please enter the parties involved.")

    elif not terms.strip():
        st.error("Please enter the terms and conditions.")

    elif not dates.strip():
        st.error("Please enter the effective date.")

    else:

        request_data = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates,
            "additional_instructions": additional_instructions
        }

        with st.spinner("Generating your legal document..."):

            try:

                response = requests.post(
                    GENERATE_URL,
                    json=request_data,
                    timeout=120
                )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state.generated_document = data.get(
                        "content",
                        ""
                    )

                    st.session_state.editing = False

                    st.success(
                        "Document generated successfully!"
                    )
```
