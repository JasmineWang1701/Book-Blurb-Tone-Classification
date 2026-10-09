# Book Blurb Tone Classification

## Overview

A team NLP project exploring whether machine learning can classify book blurbs into seven tone categories: informative, suspenseful, humorous, inspirational, optimistic, pessimistic, and poetic.

The project examined annotation agreement, class imbalance, and baseline model performance, highlighting the challenges of subjective text classification and underrepresented labels.

## My Contributions

I primarily contributed to **data annotation and baseline model development**.

* **Data Annotation:** Labeled book blurbs across seven tone categories and contributed to establishing the ground-truth dataset.
* **Baseline Modelling:** Developed a Random Forest classifier using TF-IDF text features, with class weighting to account for imbalanced labels.
* **Model Evaluation:** Evaluated validation performance using accuracy, precision, recall, and F1-score, identifying weaknesses in minority-class classification.
* **Data Analysis:** Examined inter-annotator agreement, label distributions, and class imbalance to understand how data quality affected model performance.

## Methodology

* **Annotation Analysis:** Evaluated inter-annotator agreement using Cohen's kappa and established ground-truth labels through agreement and manual adjudication.
* **Baseline Evaluation:** Compared random and majority-class prediction baselines.
* **Text Representation:** Converted text into TF-IDF features.
* **Model Training:** Trained a Random Forest classifier with 300 trees and class weighting.
* **Model Evaluation:** Assessed validation accuracy and class-level precision, recall, and F1-score.

## Results

* **51.72% validation accuracy** with the TF-IDF + Random Forest model.
* **0.15 macro F1-score**, indicating weak performance across the seven classes.
* Cohen's kappa of **0.496** for the subset annotated by two annotators.
* The most frequent tone label appeared approximately 7.19 times as often as the least frequent label.

Although the model improved on simple prediction baselines in overall accuracy, it struggled to identify several minority classes. This highlighted the importance of evaluating class-level performance rather than relying on accuracy alone.

## Key Takeaways

* Explored the impact of subjective annotations and inconsistent label interpretation on supervised learning.
* Investigated class imbalance in multi-class text classification.
* Built and evaluated a TF-IDF-based Random Forest baseline.
* Identified opportunities to improve annotation guidelines and minority-class performance.

## Team

This project was completed collaboratively with:

* Mujtaba Zaidi
* Mankaran Rooprai
* Ashwin Unnithan

## Limitations

This project focused on baseline modelling and validation rather than a fully optimized classifier. Results demonstrated that stronger overall accuracy did not necessarily translate into reliable predictions across all tone categories.

The project was an academic team project exploring multi-class text classification and model evaluation.
