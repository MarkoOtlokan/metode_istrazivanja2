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
TIME = survey['TIME'].value_counts()
print(TIME)
print('\n-------MONEY-----------------')
MONEY = survey['MONEY'].value_counts()
print(MONEY)
print('\n------FUNCTIONALITY-----------')
FUNCTIONALITY = survey['FUNCTIONALITY'].value_counts()
print(FUNCTIONALITY)
print('\n-------QUALITY--------')
QUALITY = survey['QUALITY'].value_counts()
print(QUALITY)

columns = ['TIME', 'MONEY', 'FUNCTIONALITY', 'QUALITY']
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(30, 10))
for i, col in enumerate(columns):
  sns.countplot(x=survey[col],ax=axes[i//2, i%2])
plt.show();



print('-------priority_time-----------')
priority_time = survey['TIME'].value_counts()
print(priority_time.sort_values(ascending=False))
print('\n-------priority_money-----------------')
priority_money = survey['MONEY'].value_counts()
print(priority_money.sort_values(ascending=False))
print('\n------priority_functionality-----------')
priority_functionality = survey['FUNCTIONALITY'].value_counts()
print(priority_functionality.sort_values(ascending=False))
print('\n-------priority_quality--------')
priority_quality = survey['QUALITY'].value_counts()
print(priority_quality.sort_values(ascending=False))

columns = ['TIME', 'MONEY', 'FUNCTIONALITY', 'QUALITY']
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(30, 10))
for i, col in enumerate(columns):
  sns.countplot(x=survey[col],ax=axes[i//2, i%2])
plt.show()

######################################################################################3


columns = [delivery_time_opinion, finance_opinion, functionality_opinion, delivery_quality_opinion]
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
for i, ax in enumerate(axes.flatten()):
  col = columns[i]
  ax.pie(col.values, labels=col.index, autopct='%.2f%%')
  ax.set_title(col.name)
plt.show();
