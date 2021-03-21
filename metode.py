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


#columns = ['TIME', 'MONEY', 'FUNCTIONALITY', 'QUALITY']
#fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
#for i, ax in enumerate(axes.flatten()):
 # col = columns[i]
  #ax.pie(col.values, labels=col.index, autopct='%.2f%%')
  #ax.set_title(col.name)
#plt.show();



'''print('-------priority_stack_time-----------')
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


print("WM - time: " + str(((priority_stack_time[2] * 4) + (priority_stack_time[1] * 3) + (priority_stack_time[0] * 2) + priority_stack_time[3])/160))
print("WM - money: " + str(((priority_stack_money[3] * 4) + (priority_stack_money[2] * 3) + (priority_stack_money[1] * 2) + priority_stack_money[0])/160))
print("WM - functionality: " + str(((priority_stack_functionality[0] * 4) + (priority_stack_functionality[1] * 3) + (priority_stack_functionality[2] * 2) + priority_stack_functionality[3])/160))
print("WM - quality: " + str(((priority_stack_quality[2] * 4) + (priority_stack_quality[1] * 3) + (priority_stack_quality[3] * 2) + priority_stack_quality[0])/160))

'''

survey.columns



adhoc_successful = survey.adhoc_successful.value_counts()
adhoc_challenged = survey.adhoc_challenged.value_counts()
adhoc_failed = survey.adhoc_failed.value_counts()

print("AdHoc - succesful")
print(adhoc_successful)
print("\n AdHoc - challenged")
print(adhoc_challenged)
print("\n AdHoc - failed")
print(adhoc_failed)

data = [adhoc_successful, adhoc_challenged, adhoc_failed]
fig = plt.figure(figsize=(17,17))
rows = 2
cols = 2
for i, feature in enumerate(data):
  fig.add_subplot(rows, cols, i+1)
  plt.pie(feature.values, labels=feature.index, autopct='%.2f%%')
  plt.title(feature.name)
plt.show()

iterative_successful = survey.iterative_successful.value_counts()
iterative_challenged = survey.iterative_challenged.value_counts()
iterative_failed = survey.iterative_failed.value_counts()

print("Iterative - succesful")
print(iterative_successful)
print("\n Iterative - challenged")
print(iterative_challenged)
print("\n Iterative - failed")
print(iterative_failed)




data = [iterative_successful, iterative_challenged, iterative_failed]
fig = plt.figure(figsize=(17,17))
rows = 2
cols = 2
for i, feature in enumerate(data):
  fig.add_subplot(rows, cols, i+1)
  plt.pie(feature.values, labels=feature.index, autopct='%.2f%%')
  plt.title(feature.name)
plt.show()





agile_successful = survey.agile_successful.value_counts()
agile_challenged = survey.agile_challenged.value_counts()
agile_failed = survey.agile_failed.value_counts()

print("Agile - succesful")
print(agile_successful)
print("\n Agile - challenged")
print(agile_challenged)
print("\n Agile - failed")
print(agile_failed)





data = [agile_successful, agile_challenged, agile_failed]
fig = plt.figure(figsize=(17,17))
rows = 2
cols = 2
for i, feature in enumerate(data):
  fig.add_subplot(rows, cols, i+1)
  plt.pie(feature.values, labels=feature.index, autopct='%.2f%%')
  plt.title(feature.name)
plt.show()





traditional_successful = survey.traditional_succesful.value_counts()
traditional_challenged = survey.traditional_challenged.value_counts()
traditional_failed = survey.traditional_failed.value_counts()

print("Traditional - succesful")
print(traditional_successful)
print("\n Traditional - challenged")
print(traditional_challenged)
print("\n Traditional - failed")
print(traditional_failed)





data = [traditional_successful, traditional_challenged, traditional_failed]
fig = plt.figure(figsize=(17,17))
rows = 2
cols = 2
for i, feature in enumerate(data):
  fig.add_subplot(rows, cols, i+1)
  plt.pie(feature.values, labels=feature.index, autopct='%.2f%%')
  plt.title(feature.name)
plt.show()




columns =  ['adhoc_successful', 'adhoc_challenged', 'adhoc_failed',
       'iterative_successful', 'iterative_challenged', 'iterative_failed',
       'agile_successful', 'agile_challenged', 'agile_failed',
       'traditional_succesful', 'traditional_challenged',
       'traditional_failed']

data = []
for col in columns:
  helper = survey[survey[col] != "Don't Know"]
  data.append({'count': helper[col].count(), 'valueCount' : helper[col].value_counts(sort=True)})


# Moglo je elegantnije, ali nisam imao vremena...
def calcWeightSum(x):
  switcher = {
    0: 1,
    '1-10%': 2,
    '11-20%': 3,
    '21-30%': 4,
    '31-40%': 5,
    '41-50%': 6,
    '51-60%': 7,
    '61-70%': 8,
    '71-80%': 9,
    '81-90%': 10,
    '91-100%': 11,
  }

  length = len(x.index)

  i = 0
  sum = 0
  while i < length:
    sum += x.values[i] * switcher.get(x.index[1], 1)
    i += 1

  return sum

wAvgMean = {}
i = 0
while i < len(data):
  wAvgMean.update({data[i]['valueCount'].name: (calcWeightSum(data[i]['valueCount'])/data[i]['count'])})
  i += 1


adhoc = {}
agile = {}
traditional = {}
iterative = {}
for k, v in wAvgMean.items():
  if 'adhoc' in k:
    adhoc.update({k:v})
  elif 'agile' in k:
    agile.update({k:v})
  elif 'traditional' in k:
    traditional.update({k:v})
  elif 'iterative' in k:
    iterative.update({k:v})

agileDF = pd.DataFrame.from_dict(list(agile.items()))
adhocDF = pd.DataFrame.from_dict(list(adhoc.items()))
traditionalDF = pd.DataFrame.from_dict(list(traditional.items()))
iterativeDF = pd.DataFrame.from_dict(list(iterative.items()))



data = [agileDF, adhocDF, traditionalDF, iterativeDF]
fig = plt.figure(figsize=(17,17))
rows = 2
cols = 2
for i, feature in enumerate(data):
  fig.add_subplot(rows, cols, i+1)
  plt.pie(feature[1], labels=feature[0], autopct='%.2f%%')
plt.show()
