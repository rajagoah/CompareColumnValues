#importing package
import pandas as pd

#importing the csv file
df_int = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/Ankush Saini dataset for comparison/exportint_dec19.csv')
df_prd = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/Ankush Saini dataset for comparison/exportprod_dec19.csv')

#displaying the data type of the two variables holding the imported files
print(type(df_int))
print(df_int.shape)
print(df_int.head())

print(type(df_prd))
print(df_prd.shape)
print(df_prd.head())

#converting thw two dataframes into list
lst_int = df_int['REPAIR_ORDER_NBR'].tolist()
lst_prd = df_prd['REPAIR_ORDER_NBR'].tolist()

#difference in length of the two calues in the two columns in dataframes
print('The difference in the lenght of the two lists is: ',len(lst_int)-len(lst_prd))

#extracting the non common elements by converting the list to a set first
set_int = set(lst_int)
set_prd = set(lst_prd)

#using the difference operator to extract the non common elements
set_non_common_elements = set_int.difference(set_prd)

print(set_non_common_elements)

#exporting to a csv by converting to a df
pd.DataFrame(set_non_common_elements).to_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/Ankush Saini dataset for comparison/Set_non_common_elements.csv')