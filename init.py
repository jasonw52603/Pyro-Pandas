import pandas as pd
import numpy as np
import openpyxl as xl 
import config as cfg
import dataFrameFunctions as dfFunc


#init code goes here

wb = xl.load_workbook(filename = '/home/jasonw/Desktop/pyro-pandas/samplesheet.xlsx')
dict = wb.sheetnames
print(dict[3])

rawSheet = pd.ExcelFile('~/Desktop/pyro-pandas/samplesheet.xlsx')
df0 = pd.read_excel(rawSheet, dict[3])
print(df0)

df0 = dfFunc.resetColumnNames(df0)
df0 = dfFunc.resetRowNames(df0)

for rowName in cfg.rowsToIgnore:
    df0 = dfFunc.deleteRow(df0, rowName)

df0 = dfFunc.resetRowNames(df0)

for column in range(3): # Removes the extra statistics from the scouting app
    df0 = df0[df0.columns[:-1]]


# df0 = df0.rename(columns={'dfdf': '1'})
print("\n \n Final result:")
print(df0)


