import pandas as pd

def deleteRow(dataframe, rowIndex):
    dataframe = dataframe.drop(index=[rowIndex])
    return dataframe

def resetColumnNames(dataframe):
    # Renames columns to integers starting from 0
    for column in range(len(dataframe.columns)):
        dataframe = dataframe.rename(columns={dataframe.columns[column]: column})
    return dataframe

def resetRowNames(dataframe):
    for row in range(len(dataframe.index)):
        dataframe = dataframe.rename(index={dataframe.index[row]: row})
    return dataframe