# Hotel Booking Cancellation Prediction

https://github.com/ravindutw/hotel-booking-cancellation-prediction.git

This project focuses on training classification machine learning models to predict hotel booking cancellations. Predicting whether a guest will cancel their booking is crucial for hotels to optimize revenue and manage room availability.

## Project Structure

- `notebooks/`: Contains Jupyter notebooks for different stages of the machine learning pipeline.
    - [EDA.ipynb](notebooks/EDA.ipynb): Exploratory Data Analysis.
    - [Preprocessing.ipynb](notebooks/Preprocessing.ipynb): Data Cleaning and Preprocessing.

## Exploratory Data Analysis (EDA)

The [EDA notebook](notebooks/EDA.ipynb) provides a comprehensive analysis of the hotel booking dataset. Key steps include:

- **Statistical Summary**: Overview of numerical and categorical features.
- **Data Visualization**: Distribution of classes (canceled vs. not canceled), histograms of numerical features, and heatmaps for correlation analysis.
- **Behavioral Analysis**: Investigating how factors like lead time, special requests, and hotel type influence cancellation risk.
- **Time-based Trends**: Analysis of cancellation rates across months, years, and days of the month.

## Data Preprocessing

The [Preprocessing notebook](notebooks/Preprocessing.ipynb) handles data cleaning and transformation to prepare it for model training. The following steps are performed:

- **Dropping Unnecessary Columns**: Removed `reservation_status` and `reservation_status_date` to prevent data leakage.
- **Handling Duplicates**: Identified and removed duplicate records.
- **Missing Value Treatment**:
    - Dropped rows with missing `country` and `children` values.
    - Filled missing `agent` and `company` IDs with `0` (indicating no agent/company).
- **Type Correction**: Standardized data types for consistency.
- **Data Export**: The cleaned dataset is saved as a Parquet file for efficient loading during the training phase.

## Model Training (Coming soon)

## Model Evaluation (Coming soon)

---
© 2026 Ravindu Wijesundara

https://github.com/ravindutw
