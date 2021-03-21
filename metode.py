import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


survey = pd.read_excel("Podaci_uspesnost softverskih projekata.xlsx")

print("Broj instanci u skupu podataka: ", survey.shape[0])
print("Broj atributa(kolona): ", survey.shape[1])
print("Nazivi atributa:")

print("__________________________")
for col in survey.columns:
  print(col)
print("__________________________")

print('Nedostajuće vrednosti po atributima: \n')
print(survey.isna().sum())

survey = survey.dropna()
print("Broj instanci nakon uklanjanja NA vrednosti: ", survey.shape[0])
print('Pregled nedostajućih vrednosti nakon uklanjanja istih: \n')
print(survey.isna().sum())



for col in survey.columns:
  print('-----------------------------------\n' + col + ':')
  print(survey[col].unique())

print(survey.head(10))


POSITIONs = survey.POSITION.value_counts()
plt.subplots(figsize=(11,11))
plt.pie(POSITIONs.values, labels=POSITIONs.index, autopct='%1.2f%%')
plt.show()


EXPERIENCE = survey.EXPERIENCE.value_counts()
plt.subplots(figsize=(11,11))
plt.pie(EXPERIENCE.values, labels=EXPERIENCE.index, autopct='%1.2f%%')
plt.show()




EXPERIENCE_per_POSITION = survey.groupby('POSITION').EXPERIENCE.value_counts().sort_values(ascending=False)
EXPERIENCE_per_POSITION


plt.subplots(figsize=(15,7))
chart = sns.countplot(x="POSITION", hue="EXPERIENCE", data=survey)
chart.legend(loc='upper right')
chart.set_xticklabels(chart.get_xticklabels(), rotation=45);

sns.catplot(y="POSITION", data=survey, col="EXPERIENCE", kind="count", col_wrap=3, palette=sns.color_palette('Paired'));


sectors = survey.SECTOR.value_counts()
plt.subplots(figsize=(11,11))
plt.pie(sectors.values, labels=sectors.index, autopct='%1.2f%%')
plt.show()



sns.catplot(y="POSITION", data=survey, col="SECTOR", kind="count", col_wrap=4, palette=sns.color_palette('Paired'));

DEPARTMENTSIZE = survey.DEPARTMENTSIZE.value_counts()
plt.subplots(figsize=(11,11))
plt.pie(DEPARTMENTSIZE.values, labels=DEPARTMENTSIZE.index, autopct='%1.2f%%')
plt.show()

LOCATION = survey.LOCATION.value_counts()
plt.subplots(figsize=(11,11))
plt.pie(LOCATION.values, labels=LOCATION.index, autopct='%1.2f%%')
plt.show()


print('-------delivery_time_opinion-----------')
delivery_time_opinion = survey['delivery_time_opinion'].value_counts()
print(delivery_time_opinion)
print('\n-------finance_opinion-----------------')
finance_opinion = survey['finance_opinion'].value_counts()
print(finance_opinion)
print('\n------functionality_opinion-----------')
functionality_opinion = survey['functionality_opinion'].value_counts()
print(functionality_opinion)
print('\n-------delivery_quality_opinion--------')
delivery_quality_opinion = survey['delivery_quality_opinion'].value_counts()
print(delivery_quality_opinion)

columns = ['delivery_time_opinion', 'finance_opinion', 'functionality_opinion', 'delivery_quality_opinion']
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(30, 10))
for i, col in enumerate(columns):
  sns.countplot(x=survey[col],ax=axes[i//2, i%2])
plt.show();



print('-------priority_stack_time-----------')
priority_stack_time = survey['priority_stack_time'].value_counts()
print(priority_stack_time.sort_values(ascending=False))
print('\n-------priority_stack_money-----------------')
priority_stack_money = survey['priority_stack_money'].value_counts()
print(priority_stack_money.sort_values(ascending=False))
print('\n------priority_stack_functionality-----------')
priority_stack_functionality = survey['priority_stack_functionality'].value_counts()
print(priority_stack_functionality.sort_values(ascending=False))
print('\n-------priority_stack_quality--------')
priority_stack_quality = survey['priority_stack_quality'].value_counts()
print(priority_stack_quality.sort_values(ascending=False))

columns = ['priority_stack_time', 'priority_stack_money', 'priority_stack_functionality', 'priority_stack_quality']
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(30, 10))
for i, col in enumerate(columns):
  sns.countplot(x=survey[col],ax=axes[i//2, i%2])
plt.show()

columns = ['priority_stack_time', 'priority_stack_money', 'priority_stack_functionality', 'priority_stack_quality']
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(30, 10))
for i, col in enumerate(columns):
  sns.countplot(x=survey[col],ax=axes[i//2, i%2])
plt.show()
