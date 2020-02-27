

def delete_row(dataframe, row_index):
    return dataframe.drop(index=row_index)


def delete_column(dataframe, column_index):
    return dataframe.drop(columns=column_index)


def reset_column_names(dataframe):
    # Renames columns to integers starting from 0
    for column in range(len(dataframe.columns)):
        dataframe = dataframe.rename(columns={dataframe.columns[column]: column})
    return dataframe


def reset_row_names(dataframe):
    for row in range(len(dataframe.index)):
        dataframe = dataframe.rename(index={dataframe.index[row]: row})
    return dataframe


def get_end_column(dataframe):
    return dataframe.columns.values[-1]
