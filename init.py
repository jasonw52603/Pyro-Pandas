import pandas as pd
import numpy as np
import openpyxl as xl
import config as cfg
import dataFrameFunctions as dfFunc


# Init code goes here

# Sheet names
wb = xl.load_workbook(filename='/home/jasonw/Desktop/pyro-pandas/samplesheet0.xlsx')
sheetnames = wb.sheetnames
print(sheetnames[3])

# Dataframe
rawSheet = pd.ExcelFile('~/Desktop/pyro-pandas/samplesheet0.xlsx')
df0 = pd.read_excel(rawSheet, sheetnames[3])
print(df0)

for sheet_num in range(len(sheetnames)):
    df0 = pd.read_excel(rawSheet, sheetnames[sheet_num])

    df0 = dfFunc.reset_column_names(df0)
    df0 = dfFunc.reset_row_names(df0)

    for rowName in cfg.rowsToIgnore:
        df0 = dfFunc.delete_row(df0, rowName)

    df0 = dfFunc.reset_row_names(df0)

    for column in range(3):  # Removes the extra statistics from the scouting app
        df0 = df0[df0.columns[:-1]]

    # df0 = df0.rename(columns={'dfdf': '1'})
    print('\n \n' + sheetnames[sheet_num] + ' final result:')
    print(df0)


