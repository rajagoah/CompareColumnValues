import pandas as pd
import numpy as np

#reading the excel file
df = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/dis_rep_prod.csv', low_memory=False, header=None)

print('read complete')
df=df.drop([1,2], axis = 1)
print(df.head())

#creating two different sets to store first and the second column. Using the astype(str) function to help convert the entire dataframe to a string data type
print('creating a new lists to store column values')
df_1 = df[0].tolist()
print(df_1)
print('done')

df_3 = df[3].tolist()
print(df_3)
print('done 3')
print(type(df_1))
print(type(df_3))

#converting the list to a set
df_1_set = set(df_1)
df_3_set = set(df_3)

#comparing the sets using the difference operator
df_diff = df_3_set.difference(df_1_set)
print(str(df_diff))

#converting the above set to a df and sending the output as a csv
df_diff_DF = pd.DataFrame(df_diff)
print('*************** PRODUCING THE CSV OUTPUT *******************')
df_diff_DF.to_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/COMPARED_dis_rep_prod.csv')