# Series
# dataframe
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# x = [1,2,3,4,5,6,7,8,9]
# y = ['Andi','Budi','Caca','Deni','Euis']
# seriesku = pd.Series(x)
# serieskuy = pd.Series(y)
# serieskuy = pd.Series(y, index= ['a','b','c'.'d','e'])

# print(x)
# print(seriesku)

# print(seriesku[0])
# print(seriesku[0:8])
# print(seriesku[0::2])

# print(serieskuy)

######################################################################################################
# x = np.arange(0,10,1)
# x = np.random.rand(1,10)
# x = np.random.randint(2,size=10)
x = np.random.randint(10, size=10)
# x = np.random.randint(10, size=(2,5))
y = np.random.randint(10, size=10)
z = 'bhksujrmvl'
s = pd.Series(x, index= np.arange(1,11,1))
a = [('Andi', 21,'S1'),
    ('Budi', 21,'S1'),
    ('Caca', 21,'S1'),
    ('Deni', 21,'d3')
]

# data = {
#     'id':[1,2,3,4],
#     'nama':['Andi','Budi','Caca','Deni'],
#     'Job' :['Programmer','Designer','Insyinyur','PNS']
# }


# data1 = [
#     {'nama': 'Andi', 'usia':'23'},
#     {'nama': 'Andi', 'usia':'23'},
#     {'nama': 'Andi', 'usia':'23'},
#     {'nama': 'Andi', 'usia':'23'}
# ]

data2 = {
    'satu':'hai',
    'dua': np.arange(10),
    # 'tiga': pd.Series(np.arange(10))
    'tiga': pd.Series(y),
    'empat': pd.Timestamp('20190220'),
    'lima': pd.date_range('20190220', periods = 10)
    
}

# print(s)
# print(x)
# print(y)

# df = pd.DataFrame([x,y,z])
# df = pd.DataFrame(
#     a,
#     index = ['a','b','c','d'],
#     columns = ['Nama','Usia','Pendidikan']
#     )
# print(df)
# print(df['Nama'])
# print(df[0:1])

# df = pd.DataFrame(data)
# df = pd.DataFrame(data1,index=['a','b','c','d'])

# df = pd.DataFrame(data2)
df = pd.DataFrame(data2,index=list('abcdefghij'))
# print(df)
# print(df.describe())

# a = pd.Series(y)
# print(a)

# plt.plot(data2['lima'], data2['tiga'])
# plt.show()

# print(df.head(2))
# print(df.tail(2))
# print(df.index)
# print(df.columns)
print(df.values[0][0])

# for x in df.values:
#     print(x[0])

# print(df.sort_index(axis=1))

# print(df.sort_index(ascending=False))
# print(df.sort_values(by=['tiga','dua'], ascending=False))

# print(df['satu'])
# print(df.loc[0])
# print(df.loc[0:3,['satu','tiga','lima']])

# print(df.loc['a':'c', ['empat','lima']]) # loc = pakai nama (index nyalain)
# print(df.iloc[1:3,0:2]) # iloc= pakai posisi

# print(df.iloc[[1,3,4,7,9],[0,2,4]])

# print(df.at['b','empat'])
# print(df.iat[1,3])

# print(df.T)

# kaggle datasets download -d karangadiya/fifa19 --unzip