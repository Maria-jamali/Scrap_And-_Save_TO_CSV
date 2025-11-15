import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0'})
url = 'https://www.scrapethissite.com/pages/forms/'
columns_indices = [1,2,3,4]
CSV_File_Name = ("Task.csv")
page = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find_all('table', attrs={'class':'table'})

df_full = pd.read_html(str(table[0]))[0]

print(table)
if max(columns_indices) >= len(df_full.columns):
    print("Error: The selected column indices are out of bounds for the scraped table.")
    print(f"Table has {len(df_full.columns)} columns, but indices {columns_indices} were requested.")
    columns_to_keep = df_full.columns[:4]
else:
    columns_to_keep = [df_full.columns[i] for i in columns_indices]
df_final = df_full[columns_to_keep]

print(f"\n--- Selected Columns: {columns_to_keep} ---")
print("Preview of the data:")
print(df_final.head())
df_final.to_csv(CSV_File_Name, index=False, encoding='utf-8')

print(f"\nSUCCESS! Data saved to {CSV_File_Name}")
print("You can download this file from the 'Files' tab on the left sidebar in Google Colab.")