# ai-genetic-sequence-investigation
MSc research project exploring AI and machine learning techniques for investigating DNA, RNA, and protein sequences.

## Project Overview

This project investigates whether artificial intelligence and machine-learning techniques can identify sequence-level patterns and evolutionary differences in **BRCA1 DNA, RNA and protein sequences across six species**.

The selected species are:

- Human (*Homo sapiens*)
- Chimpanzee (*Pan troglodytes*)
- House mouse (*Mus musculus*)
- Dog (*Canis lupus familiaris*)
- Domestic cat (*Felis catus*)
- Chicken (*Gallus gallus*)

## Methods

The project uses Python and Biopython for sequence processing and Scikit-learn for machine-learning analysis.

The main workflow includes:

1. FASTA sequence acquisition and validation
2. Species-specific duplicate removal
3. Exploratory data analysis
4. Protein 3-mer feature extraction
5. PCA for dimensionality reduction
6. K-Means clustering for unsupervised analysis
7. Random Forest classification
8. Four-fold stratified cross-validation
9. Feature importance analysis
10. Cross-species duplicate and leakage checks
11. Human-downsampled sensitivity analysis

## Dataset

The dataset contains **914 sequence records**, comprising DNA, RNA and protein sequences. The machine-learning classification analysis focuses specifically on the validated BRCA1 protein sequences and their 3-mer representations.

## Key Results

The analysis identified clear sequence-level patterns across species. PCA and K-Means provided exploratory evidence of clustering, while Random Forest was used to evaluate species-specific classification patterns. Due to the small and imbalanced dataset, the results are interpreted cautiously rather than as evidence of clinical or biological causation.

## Tools

- Python
- Google Colab
- Biopython
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

## Project Purpose

The project demonstrates a reproducible machine-learning workflow for comparative biological sequence analysis while considering **class imbalance, validation reliability, data leakage and responsible interpretation of AI results**.
