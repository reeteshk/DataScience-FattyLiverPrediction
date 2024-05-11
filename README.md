# Non-Alcohol Fatty Liver Disease Prediction Project README

## Project Description
This Project focuses on predicting non-alcoholic fatty liver disease (NAFLD) using clinical data. The project applies statistical and machine learning techniques to assess the risk factors associated with NAFLD and predicts its occurrence in individuals.

## Authors
- Santosha Nagaratnakar Chakkapalli
- Reetesh Kesarwani

## Notebook Contents
1. **Introduction**: An overview of NAFLD(Non-Alcohol Fatty Liver Disease) and the importance of its early prediction.
2. **Abstract**: Explains the progression from NAFLD to more severe liver diseases and the objective of the study.
3. **Dataset Attributes**: Detailed attributes used in the analysis including demographic, physiological, and clinical data points.

4. **Data Preparation and Analysis**:
   - **Python Libraries**: Instructions on installing Python libraries such as `matplotlib`, `seaborn`, `pandas`, `numpy`, which are crucial for data manipulation and visualization.
   - **Data Loading**: How to load data using pandas for analysis.
   - **Data Cleaning**: Techniques for handling missing data, outlier detection, and normalization.
   - **Exploratory Data Analysis (EDA)**:
     - **Statistical Summaries**: Use of descriptive statistics to understand central tendency, dispersion, and shape of datasets.
     - **Data Visualization**: Utilization of `matplotlib` and `seaborn` for creating histograms, box plots, scatter plots, and heatmaps to visualize distributions and correlations among variables.

5. **Model Building**:
   - **Feature Selection**: Techniques to identify the most relevant features for predicting NAFLD.
   - **Model Training**: Use of various machine learning algorithms:
     - **Logistic Regression**: A statistical model for binary classification.
     - **Random Forest**: An ensemble learning method for classification that operates by constructing a multitude of decision trees.
     - **K-Nearest Neighbours**: A non-parametric method used for classification and regression.
     - **Support Vector Machines (SVM)**: Supervised learning models with associated learning algorithms that analyze data used for classification and regression analysis.
     - **XGBoost**: An implementation of gradient boosted decision trees designed for speed and performance.
   - **Model Evaluation**: Discusses the use of accuracy, precision, recall, and F1-score to evaluate model performance. Implementation of cross-validation techniques to ensure model reliability.

6. **Deployment**:
   - **Model Saving**: How to save trained models using `joblib`.
   - **Streamlit Application**: Steps to set up a user-friendly web application using Streamlit to deploy the predictive model.

7. **References**: Cites sources for data and further reading.
8. **License**: The project is released under an MIT License, allowing extensive permissions for use and distribution.

## Installation
Make sure to install the required libraries before running the notebook to ensure all functionalities are available.

## Usage
Execute each cell in the Jupyter notebook from top to bottom to replicate the analysis and results. Comprehensive comments and explanations are provided throughout the notebook to guide users through the process.


<video width="320" height="240" controls>
  <source src="Video_Explanation.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>
