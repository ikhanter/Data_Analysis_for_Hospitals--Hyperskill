import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 8)

general_df = pd.read_csv('test/general.csv', )
prenatal_df = pd.read_csv('test/prenatal.csv')
sports_df = pd.read_csv('test/sports.csv')

prenatal_df.rename(columns={'HOSPITAL': 'hospital', 'Sex': 'gender'}, inplace=True)
sports_df.rename(columns={'Hospital': 'hospital', 'Male/female': 'gender'}, inplace=True)

total_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
total_df.drop(columns=['Unnamed: 0'], inplace=True)

total_df.dropna(axis=0, how='all', inplace=True)

total_df['gender'] = total_df['gender'].replace(['man', 'male'], 'm')
total_df['gender'] = total_df['gender'].replace(['woman', 'female'], 'f')
total_df['gender'] = total_df['gender'].fillna('f')

for column in ['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']:
    total_df[column] = total_df[column].fillna(0)


# Q1: Which hospital has the highest number of patients?
# Q2: What share of the patients in the general hospital suffers from stomach-related issues?
# Round the result to the third decimal place.
# Q3: What share of the patients in the sports hospital suffers from dislocation-related issues?
# Round the result to the third decimal place.
# Q4: What is the difference in the median ages of the patients in the general and sports hospitals?
# Q5: After data processing at the previous stages, the blood_test column has three values: t= a blood test was taken,
# f= a blood test wasn't taken, and 0= there is no information. In which hospital the blood test was taken
# the most often (there is the biggest number of t in the blood_test column among all the hospitals)?
# How many blood tests were taken?


# answer_1 = total_df.hospital.mode()[0]
# answer_2 = total_df.pivot_table(index='diagnosis', columns='hospital', values='gender', aggfunc='count')
# answer_2 = round(answer_2.loc['stomach', 'general'] / answer_2.general.sum(), 3)
# answer_3 = total_df.pivot_table(index='diagnosis', columns='hospital', values='gender', aggfunc='count')
# answer_3 = round(answer_3.loc['dislocation', 'sports'] / answer_3.sports.sum(), 3)
# answer_4 = abs(total_df[total_df['hospital'] == 'general'].age.median() - total_df[total_df['hospital'] == 'sports'].age.median())
# answer_5 = total_df.pivot_table(index='hospital', columns='blood_test', values='gender', aggfunc='count')
# answer_5_1 = answer_5.loc[answer_5.t == answer_5.t.max()].index[0]

# print(f'The answer to the 1st question is {answer_1}')
# print(f'The answer to the 2nd question is {answer_2}')
# print(f'The answer to the 3rd question is {answer_3}')
# print(f'The answer to the 4th question is {answer_4}')
# print(f'The answer to the 5th question is {answer_5_1}, {answer_5.t.max()} blood tests')

# Q1: What is the most common age of a patient among all hospitals? Plot a histogram and choose one of
# the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80
# Q2: What is the most common diagnosis among patients in all hospitals? Create a pie chart
# Q3: Build a violin plot of height distribution by hospitals. Try to answer the questions.
# What is the main reason for the gap in values? Why there are two peaks, which correspond to the relatively
# small and big values? No special form is required to answer this question


# It doesn't work in Pycharm, I opened this in IDLE for getting plots
# Answer 1
total_df.plot(y='age', kind='hist')
# Answer 2
answer_2 = total_df.pivot_table(index='diagnosis', values='gender', aggfunc='count')
answer_2.plot(y='gender', kind='pie')
# Answer 3

fig, axes = plt.subplots()
axes.violinplot(dataset=[total_df[total_df.hospital == 'general']['height'].values,
                         total_df[total_df.hospital == 'prenatal']['height'].values,
                         total_df[total_df.hospital == 'sports']['height'].values])
plt.show()
print('The answer to the 1st question: 15-35')
print('The answer to the 2nd question: pregnancy')
print('''The answer to the 3rd question: It can be associated in different metrics. General and Prenatal hospitals provide the information about height in meters, sports hospital in ft.''')

