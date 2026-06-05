import streamlit as st

from retrieval.retriever import retrieve

from drafting.generator import generate_draft

from drafting.citation_builder import attach_citations

st.set_page_config(
    page_title="Legal AI Assistant",
    layout="wide"
)

st.title("📄 Legal AI Assistant")

st.write(
    "Grounded Legal Draft Generation"
)

query = st.text_area(
    "Ask a Question",
    value="Create a case fact summary."
)

if st.button("Generate Draft"):

    evidence = retrieve(query)

    draft = generate_draft(
        query,
        evidence
    )

    final_output = attach_citations(
        draft,
        evidence
    )

    st.subheader(
        "Generated Draft"
    )

    st.text_area(
        "Output",
        final_output,
        height=500
    )

    st.subheader(
        "Retrieved Evidence"
    )

    for chunk in evidence:

        st.write(chunk)