# -*- coding: utf-8 -*-
"""malaprabha.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15ZPgP0TaWJh0eaHukO8fXMSgcFM2NMDh
"""

import xarray as xr
import pandas as pd
pd.set_option('display.max_rows', None)

from google.colab import drive
drive.mount('/content/gdrive/', force_remount = True)

ds = xr.open_dataset('/content/gdrive/MyDrive/Malaprabha/RF25_IMD0p252019_jas.nc')
df = ds.to_dataframe()
df.to_csv('data.csv')
df = pd.read_csv('data.csv')

df['TIME'] = pd.to_datetime(df['TIME'], format='%Y-%m-%d')
df = df.sort_values(by = 'TIME')

df.head(10)





selected_df = df.loc[(df['LONGITUDE'] == 73.25) & (df['LATITUDE'] == 36.25) & (df['TIME'] >= pd.Timestamp(2019, 8, 1)) & (df['TIME'] <= pd.Timestamp(2019, 8, 31))]
selected_df = selected_df[~selected_df['RAINFALL'].isna()]
# selected_df = df.loc[(df['LONGITUDE'] == 73.25) & (df['LATITUDE'] == 36.25) & (df['TIME'] == pd.Timestamp(2019, 2, 1))]
# selected_df = df.loc[(df['LONGITUDE'] == 70.00) & (df['LATITUDE'] == 16.5)]
# selected_df = df['TIME'] == pd.Timestamp(2019, 4, 16)
selected_df

