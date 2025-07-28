import pandas as pd

#1 Load the CSV file into a DataFrame
data = pd.read_csv("C:/Users/shree/Downloads/DE Case Study Assignments/PYTHON CASE STUDY/CASE STUDY 1/LoanData.csv")
'''
#2 Display the first 10 rows
print(data.head(10))
print(data.tail())

#3.Printing the column names of the DataFrame

print("Column Names:")
print(data.columns.tolist())

#4.Summary of Data Frame

print("\nSummary of data frame:")
print(data.info())

#5.Descriptive Statistical Measures of a DataFrame
print("\nDescriptive Statistical Measures of a DataFrame:")
print(data.describe())
'''

#7. Sorting DataFrame values
# Sort by ApplicantIncome in descending order
sorted_data = data.sort_values(by='ApplicantIncome', ascending=False)
print(sorted_data[['ApplicantIncome', 'LoanAmount']].head())

'''

#8.Merge Data Frames
# Creating anotherDataFrame for merge
new_data = pd.DataFrame({
    'Loan_ID': data['Loan_ID'],
    'Status': ['Verified']*len(data)
})
# Merge on Loan_ID
merged_data = pd.merge(data, new_data, on='Loan_ID')
print(merged_data.head(3))



#9.Apply Function
# Define a function to categorize loan risk
def loan_risk(row):
    if row['Credit_History'] == 0 and row['LoanAmount'] > 150:
        return 'High Risk'
    elif row['Credit_History'] == 1 and row['LoanAmount'] <= 150:
        return 'Low Risk'
    else:
        return 'Moderate Risk'
# Apply the function row-wise
data['LoanRisk'] = data.apply(loan_risk, axis=1)
# Display result
print(data[['Credit_History', 'LoanAmount', 'LoanRisk']].head())

#11.Visualizing DataFrame
data.plot(x='ApplicantIncome', y='CoapplicantIncome', kind= 'hist')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("C:/Users/shree/Downloads/DE Case Study Assignments/PYTHON CASE STUDY/CASE STUDY 1/LoanData.csv")
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (15,5)
plt.subplot(1,3,1)
sns.boxplot(data['ApplicantIncome'])
plt.subplot(1,3,2)
sns.boxplot(data['CoapplicantIncome'])
plt.subplot(1,3,3)
sns.boxplot(data['LoanAmount'])
plt.suptitle('Outliers Detection')
plt.show()
'''