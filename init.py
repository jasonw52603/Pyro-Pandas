import pandas as pd
import openpyxl as xl 
import config as cfg


#init code goes here

wb = xl.load_workbook(filename = '/home/jasonw/Desktop/pyro-pandas/samplesheet.xlsx')
dict = wb.sheetnames
print(dict[3])

rawSheet = pd.ExcelFile('~/Desktop/pyro-pandas/samplesheet.xlsx')
df0 = pd.read_excel(rawSheet, dict[3])
print(df0)

for column in range(len(df0.columns)):
    df0.rename(index={df0.columns[column]: '0'})

df0.rename(columns={'Unnamed: 0': '1'})
print(df0)


