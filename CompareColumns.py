import pandas as pd
import numpy as np

#reading the excel file
df = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/dis_rep_prod.csv', low_memory=False, header=None)

print('read complete')
df=df.drop([1,2], axis = 1)
print(df.head())

#creating a dataframe to store first column. Using the astype(str) function to help convert the entire dataframe to a string data type
print('creating a new dataframwe to store column values')
df_1 = pd.DataFrame(df[[0]].astype(str))
print(df_1.head(1))
print('done')

df_3 = pd.DataFrame(df[[3]].astype(str))
print(df_3.head(2))
print('done 3')

#comparing the two dataframes and spitting the difference list. For this we will use numpy  
print('******* the difference is *******')
df_diff = pd.DataFrame(np.setdiff1d(df_1, df_3, assume_unique= False))
print(df_diff)
df_diff.to_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/comparison_dis_rep_prod.csv')
print('****comparison complete')


