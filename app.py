import spacy
import streamlit as st
import pandas as pd

# Load your trained model
MODEL_PATH = r"E:\NLP\NLP with Sequence Models\LSTM and Named Entity Recognition\Medical NER Application\model-best"
nlp = spacy.load(MODEL_PATH)

st.title("🩺 Medical NER Application")
st.write("Enter medical text below to extract entities (diseases, drugs, conditions, etc.).")

# Use Streamlit's text_area instead of custom HTML
text = st.text_area(
    "Type or paste medical notes here...",
    height=150,
    placeholder="Enter your medical text here..."
)

if st.button("Analyze"):
    if text and text.strip():  # text is now a proper Python string
        doc = nlp(text)

        ents = [(ent.text, ent.label_) for ent in doc.ents]
        if ents:
            # Display entities as a table
            df = pd.DataFrame(ents, columns=["Entity", "Label"])
            st.subheader("Extracted Entities")
            st.table(df)

            # Annotated text
            highlighted_text = text
            offset = 0
            for ent in doc.ents:
                insert_text = f" [{ent.label_}] "
                pos = ent.end_char + offset
                highlighted_text = highlighted_text[:pos] + insert_text + highlighted_text[pos:]
                offset += len(insert_text)

            st.subheader("Annotated Report")
            st.write(highlighted_text)
        else:
            st.info("⚠️ No entities found in the text.")
    else:
        st.warning("Please enter some text before analyzing.")
