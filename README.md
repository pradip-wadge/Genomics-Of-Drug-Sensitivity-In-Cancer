# Genomics of Drug Sensitivity in Cancer (GDSC) - Dashboard and Dataset Analysis

## Overview
This project provides insights into the **Genomics of Drug Sensitivity in Cancer (GDSC)** dataset, exploring the sensitivity of various cancer types to specific drugs. The dataset enables analysis of drug efficacy, cancer treatment effectiveness, and pathway sensitivities. Our Power BI dashboard visualizes key aspects, offering actionable insights for understanding cancer drug responses.

## Technology Stack
- **Python**
- **SQL**
- **Power BI**

## Installation & Getting Started

To get started with the project, ensure you have the required packages installed. Run the following command to install dependencies:

```bash
pip install mysql-connector-python mysqlclient pandas
```

## Dataset Details

The dataset includes the following columns:
- **Cancer Type**: Type of cancer being analyzed.
- **Drug Name**: Name of the drug used in the treatment.
- **Target Pathway**: The biological pathway targeted by the drug.
- **LN_IC50**: Logarithmic value of the half-maximal inhibitory concentration, a measure of drug sensitivity.
- **AUC**: Area Under the Curve, representing the drug's effectiveness.
- **MSI Status**: Microsatellite Instability Status (e.g., MSI-H or MSI-L).
- **Gene Expression**: Expression level of specific genes in response to drug treatment.
- **Screening Medium**: Medium used for screening drug effectiveness.
- **Drug Type**: Classification or type of the drug.
- **COSMIC ID**: Catalogue Of Somatic Mutations In Cancer ID.
- **First Gene Expression**: Expression value of the first gene recorded in the dataset.
- **Average AUC**: Average effectiveness of the drug.
- **Average LN_IC50**: Average sensitivity of the drug.
- **Comparative Drug Efficacy**: Comparative effectiveness of drugs across different screening mediums.
- **Consistency Across Mediums**: Consistency of drug efficacy across various screening environments.

## Dashboard Insights

The Power BI dashboard provides a comprehensive view of the GDSC dataset through the following visualizations:
- **Top 10 Drugs by LN_IC50 Impacting Pathway Sensitivity**: Highlights drugs with the highest sensitivity impact on specific pathways.
- **AUC Trends**: Tracks trends in drug effectiveness across cancer types.
- **Comparative Drug Efficacy and Consistency Across Mediums**: Displays drug consistency and effectiveness across different screening environments.
- **Drug Efficacy Gauge Chart**: Measures overall drug efficacy.
- **Cancer-Specific Analysis**: Provides insights into drug sensitivity based on cancer type and pathway.

## Design Decisions and Assumptions

- We selected Power BI for interactive data visualization, enabling real-time analysis of drug sensitivity across multiple cancer types.
- Assumptions include a consistent definition of drug sensitivity across cancer types and an accurate MSI status categorization, which aids in specific genetic analyses.
- Assumed the data is clean and does not require extensive preprocessing for integration into the Power BI dashboard.

## Features

- **Drug Sensitivity Analysis**: Visualizes the sensitivity (LN_IC50) and effectiveness (AUC) of drugs across different cancer types.
- **Pathway Impact Insights**: Shows how different drugs affect biological pathways, aiding in targeted therapy research.
- **Comparative Analysis**: Enables side-by-side comparison of drug efficacy across screening mediums.
- **Microsatellite Instability Analysis**: Provides MSI insights, useful for understanding mutation statuses in cancers.

## Video Walkthrough of the Project

[Presentation Link](https://youtu.be/ZxJ36yWMhnY)

## Team Info  

<img src="logo.jpeg.jpg" alt="Project Logo" width="150"/>  

- **Mohit Agarwal**  
- **Saurabh**  
- **Pradip**  
- **Malhar**  

---

This project is ideal for researchers and healthcare professionals looking to understand and compare drug responses across cancer types, providing a foundation for developing targeted cancer treatments.
