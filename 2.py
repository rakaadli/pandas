import pandas as pd
import numpy as np

# df = pd.read_csv(
#     '2.csv',
#     header=None, 
#     names=['id','nama','usia','massa'],
#     # na_values=['-','n.a']
# )
# # print(df.set_index('id'))
# df = df.set_index('id')

# 1,Andi,21,65
# 2,Budi,22,45
# 3,Caca,23,76
# 4,Deni,24,65
# 5,Euis,25,76
# 6,Fafa,26,54
# 7,Gaga,27,55
# 8,Hani,28,78
# 9,Inne,29,82
# 10,Janu,30,43
# print(df[['nama','massa','usia']])
# print(df.iloc[1::2].sort_values(by='nama',ascending=False)[['nama','usia']])

#############

# 1,Andi,21,65
# 2,Budi,22,45
# 3,n.a,-,76
# 4,Deni,24,65
# 5,Euis,25,n.a
# 6,Fafa,26,n.a
# 7,Gaga,27,55
# 8,Hani,-,n.a
# 9,n.a,29,82
# 10,Janu,30,43

# print(df['massa'].mean())
# df = df.fillna(0)
# df = df.fillna({
#     'massa':0,
#     'usia':0,
#     'nama': 'Tanpa nama'
# })
# df = df.fillna(method='ffill',axis='columns') #bfill = backwards
# df = df.fillna(method='ffill')
# df = df.interpolate().fillna({
#     'nama': 'Tanpa nama'
# })
# df = df.ffill().fillna({
#     'nama': 'Tanpa nama'
# })

# df=df.dropna() #yang ada NaN ga boleh ikut
# df=df.dropna(thresh=2)
# df=df.dropna(axis='columns')
# df = df.dropna(subset=['nama'])
# df = df.replace(['-','n.a'], 'Data Tidak Tersedia')
# df = df.replace(['-','n.a'], np.NaN)
# df = df.fillna('x')
# df = df.replace({
#     '-' : 0,
#     'n.a': np.NaN
# })
# df = df.replace({
#     '-' : 0,
#     'n.a': np.NaN
# })
# df = df.replace(
#     to_replace=['-','n.a'],
#     method = 'ffill'
# )
# print(df)


#############

# 1,Andi,21,65
# 2,Budi,22,45
# 3,-,-,76
# 4,Deni,24,65
# 5,Euis,25,-
# 6,Fafa,26,-
# 7,Gaga,27,55
# 8,Hani,-,n.a
# 9,-,29,82
# 10,Janu,30,43


# df=df.replace({
#     'nama': '-',
#     'usia': '-',
#     # 'massa':['-','n.a']
# },{'nama':'Anonim',
#     'usia':0,
#     # 'massa': 0
#     })

# df['massa'] = df['massa'].replace(
#     to_replace=['-','n.a'],
#     method='ffill'
# )


# print(df)

#############

# 1,Andi,21,65,Jakarta
# 2,Budi,22,45,Bandung
# 3,Caca,23,76,Jakarta
# 4,Deni,24,46,Bandung
# 5,Euis,25,76,Denpasar
# 6,Fafa,26,55,Jakarta
# 7,Gaga,27,87,Denpasar
# 8,Hani,28,76,Jakarta
# 9,Halo,29,82,Surabaya
# 10,Janu,30,43,Bandung

df = pd.read_csv(
    '2.csv',
    header=None, 
    names=['id','nama','usia','massa','kota'],
    # na_values=['-','n.a']
)
# print(df.set_index('id'))
df = df.set_index('id')
# df = df.drop('usia',axis=1)
df = df.drop('nama',axis=1)
grup = df.groupby('kota')
dfJkt=grup.get_group('Jakarta')
dfBdg=grup.get_group('Bandung')

print(dfJkt['massa'].mean())
# print(dfJkt[['nama']][dfJkt['massa']>68])
# print(dfJkt[dfJkt['massa']>=dfJkt['massa'].mean()])
print(grup.max())
print(grup.mean())