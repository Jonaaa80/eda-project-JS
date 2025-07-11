# King County Housing Market – Exploratory Data Analysis by Jonatan Stursberg

## Overview

This project applies exploratory data analysis (EDA) techniques to the King County Housing Dataset. The goal is to extract key insights into how different housing attributes influence sale prices and to provide tailored recommendations for a selected client (either buyer or seller). This work combines data exploration, hypothesis-driven analysis, and result communication for both technical and non-technical audiences.

The repository contains:
- a structured Jupyter notebook with documented EDA steps
- a data cleaning workflow (optional)
- a presentation (PDF export) summarizing the main findings and recommendations
- this README file for guidance

## Objective

The analysis aims to:
1. Provide general insights about the King County housing market based on the dataset.
2. Explore relationships between features and housing prices.
3. Formulate and test hypotheses about market behavior.
4. Deliver at least three tailored recommendations for a specific client profile.

## Dataset

- **Source:** King County Housing Data (USA)
- **Content:** Information about ~21,000 property sales, including price, location, physical features, renovation status, and more.
- **Tables used:** Two joined tables via SQL (schema: `eda`), exported and analyzed as `.csv`.
- **Note:** Column definitions were reverse-engineered based on context due to missing documentation, simulating a realistic business scenario.

## Methodology

The project follows an iterative data science workflow:
- Initial exploration and validation of data quality
- Hypothesis formulation based on domain knowledge and client needs
- Feature analysis through statistical metrics and visualizations
- Cleaning and transformation where required (e.g., outliers, missing values)
- Summary of findings and generation of client recommendations


## Hypotheses not related to customer

These hypotheses apply broadly to the entire dataset and are not client-specific:

1. **Hypothesis 1**
   _There should be a correlation between a high house's grade on one hand and time since renovation on the other hand_

2. **Hypothesis 2**  
   _There should be a correlation between a high price per sqft and the location based on zip-codes_

3. **Hypothesis 3**  
   _The higher price correlates to high sqft of nearest neighbours' houses_

## Client-Specific Hypotheses 

The following hypotheses reflect the preferences of our client Zachary Brooks - a seller focused on maximizing profits from historic homes in premium neighborhoods:

1. **A seller seeking for high profits**
2. **Invests in historical houses in the best neighbourhoods**
3. **Asking for best timing to sell within a year (seasonal market behavior).**
4. **Unsure about renovation contributes to profit optimisation**


These hypotheses reflect the preferences or constraints of the chosen client profile:

1. **Hypothesis 1**  
   _There is a correlation between house prices and the time of the year the houses were sold_

2. **Hypothesis 2**  
   _Time since last renovation will affect the price of the house_

> The selected client (buyer or seller) and assumptions made will be explicitly documented in the notebook and presentation.

## Deliverables

1. **Jupyter Notebook** – Includes all relevant EDA steps and interpretations.
2. **Presentation (PDF)** – 10-minute summary for non-technical stakeholders.
3. **README.md** – Project guide and summary.
4. **(Optional)** Python scripts with modular cleaning functions.

## How to Use This Repository

- Clone the repository.
- Inspect the notebook in the `notebooks/` directory.
- Review the presentation in the `presentation/` folder.
- Review this README for project scope and methodology.


**Note:** The data file is excluded from version control as per `.gitignore` rules and must be added manually to the `data/` folder.

