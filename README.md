# Medical Named Entity Recognition (NER) Project

## Overview

This project implements a medical Named Entity Recognition (NER) system using two approaches:

1. **Custom spaCy Model Training**: Training a custom NER model from scratch using annotated medical text data.
2. **Pre-trained Transformer Model**: Using a pre-trained biomedical NER model from Hugging Face.

The system is designed to identify and extract medical entities from clinical text, including:

- **Medications**: Drug names and prescriptions (e.g., Aspirin, Metformin, Warfarin)
- **Diseases**: Medical conditions and diagnoses (e.g., diabetes, pneumonia, COPD)
- **Treatments**: Medical procedures and therapies (e.g., surgery, inhaler therapy)

---

## Project Structure

The project is organized into the following steps:

1. **Data Loading and Exploration**
   - Upload annotated JSON dataset.
   - Explore data structure and annotation format.

2. **Data Preprocessing**
   - Convert JSON annotations into spaCy-compatible format `(start_char, end_char, label)`.
   - Verify entity alignment with text content.

3. **spaCy Training Data Preparation**
   - Convert processed data into `DocBin` format for spaCy.
   - Handle overlapping entities and alignment issues.

4. **Model Training**
   - Initialize spaCy NER configuration.
   - Train custom spaCy NER model on prepared data.
   - Save `model-best/` for best checkpoint.

5. **Model Inference (spaCy)**
   - Load the trained model and test on sample medical text.
   - Visualize entities using spaCy's `displacy`.

6. **Transformer Model Inference**
   - Load pre-trained biomedical NER model from Hugging Face (`d4data/biomedical-ner-all`).
   - Use `pipeline("ner")` for entity extraction.
   - Aggregate subword tokens into complete entities.

---

## Use Cases

- Automated extraction of medical information from clinical notes.
- Medical record processing and analysis.
- Drug-disease relationship extraction.
- Clinical decision support systems.

---

## Technologies Used

- **spaCy**: For custom NER model training and inference.
- **Transformers (Hugging Face)**: For pre-trained biomedical NER.
- **Pandas**: For data manipulation.
- **PyTorch**: Backend for transformer models.
- **Google Colab / Local Python Environment**: Development and testing.

---

## Advantages of Pre-trained Models

1. **No Training Required**: Ready to use without annotated data.
2. **Broad Coverage**: Recognizes Chemicals/Drugs, Diseases, Genes, Species, Cell Types.
3. **High Accuracy**: Transformer-based models handle context and ambiguity better than simple models.

---

## Comparison: Custom spaCy vs Pre-trained Transformer

| Aspect          | Custom spaCy Model         | Pre-trained Transformer       |
|-----------------|---------------------------|-------------------------------|
| Training        | Requires annotated data   | Ready to use                 |
| Speed           | Fast inference            | Slower (but more accurate)  |
| Customization   | Fully customizable        | Limited without fine-tuning |
| Entity types    | Only what you train       | Pre-defined broad set        |
| Memory          | Small footprint           | Large (100s of MBs)         |

---

## Alternative Biomedical NER Models

- `dmis-lab/biobert-base-cased-v1.1`
- `allenai/scibert_scivocab_uncased`
- `microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract`

Each model is specialized for different biomedical domains, including clinical notes and research articles.
