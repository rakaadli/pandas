# kaggle datasets download -d karangadiya/fifa19 --unzip

import pandas as pd 
# df=pd.read_csv('data.csv')

# print(df.loc[0:5, ['Name','Age','Nationality']])
# print(df['Name'])
# print(df['Age'].max())
# print(df['Age'].min())
# print(df['Age'].mean())
# print(df['Age'].describe())


#works
# print(df['Name'][df['Age'] == df['Age'].max()])
# print(df[df['Age']==df['Age'].max()]['Name'])

# print(df[['Name','Club','Overall']][df['Overall']>90])

# print(df[['Name','Club','Overall']][df['Overall']>=90][df['Club'] == 'Real Madrid'])

# df=pd.read_json('data.json')

# print(df)
# print(df['nama'][df['usia']==df['usia'].max()])

#####################################################################################################

# pip install xlrd

# df1=pd.read_excel('data.xlsx','Sheet1',header=4)
# df1= df1.loc[:,['no','nama','usia','kota']]
df1 = pd.read_json('data.json')
df2=pd.read_excel('data.xlsx','Sheet2')


df1.to_csv('databaru.csv')
df1.to_json('databaru.json',orient='index')
#pip install openpyxl
df1.to_excel('databaru.xlsx')

# print(df1)
# print(df2)