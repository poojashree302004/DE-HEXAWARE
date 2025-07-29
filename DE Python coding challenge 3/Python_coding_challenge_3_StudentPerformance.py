
import pandas as pd
#1. Loading dataset
df = pd.read_csv('StudentsPerformance.csv')

#2. Printing Rows of the Data
print(df.head())
print(df.tail())

#3. Summary of Data Frame
print(df.info())


#4. Descriptive Statistical Measures
print(df.describe())


#5. counting null values in each column
print(df.isnull().sum())


#joins in pandas
import pandas as pd

# 1. Load and clean the dataset
df = pd.read_csv('StudentsPerformance.csv')
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# 2. Create two subsets of data with non-overlapping indexes

scores = df.loc[0:4, ['gender', 'math_score', 'reading_score', 'writing_score']].copy()
scores['student_id'] = scores.index

profile = df.loc[2:6, ['gender', 'race/ethnicity', 'test_preparation_course']].copy()
profile['student_id'] = profile.index

print("\n--- Scores DataFrame ---\n", scores)
print("\n--- Profile DataFrame ---\n", profile)

# 3. Perform all four types of joins

# INNER JOIN (only matching student_ids)
inner_join = pd.merge(scores, profile, on='student_id', how='inner', suffixes=('_score', '_profile'))
print("\n--- Inner Join ---\n", inner_join)

# LEFT JOIN (all from scores, match from profile if exists)
left_join = pd.merge(scores, profile, on='student_id', how='left', suffixes=('_score', '_profile'))
print("\n--- Left Join ---\n", left_join)

# RIGHT JOIN (all from profile, match from scores if exists)
right_join = pd.merge(scores, profile, on='student_id', how='right', suffixes=('_score', '_profile'))
print("\n--- Right Join ---\n", right_join)

# OUTER JOIN (all records from both sides, NaNs where no match)
outer_join = pd.merge(scores, profile, on='student_id', how='outer', suffixes=('_score', '_profile'))
print("\n--- Outer Join ---\n", outer_join)
