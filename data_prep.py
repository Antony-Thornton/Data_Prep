# Import python libraries
import pandas as pd
import numpy as np
import openpyxl

# Import scripts
import data_import
import config


def data_prep(df, df1, ldf):

    print("Printing df info.")
    df_info = df.info()
    print(df_info, end="\n\n")

    print("Printing df1 info.")
    df_info = df1.info()
    print(df_info, end="\n\n")

    print("Printing ldf info.")
    df_info = ldf.info()
    print(df_info, end="\n\n")

    new_df = df.merge(
        ldf,
        on=["VisitType Description"],
        how="left",
        suffixes=("_left", "_right"),
        indicator=True
    )

    # rename the column header "_merge" to "new_header"
    new_df.rename(columns={'_merge': 'Matching required'}, inplace=True)

    new_df["Matching required"] = np.where(
        new_df["Matching required"] == 'both',
        '',
        new_df["Matching required"]
    )

    print("Printing merged dataset (df to ldf)")
    print(new_df.head(10).to_markdown())

    file_path = config.data_path
    file_name = "BI Developer Task (Merged table)"

    new_df.to_excel(file_path + "/" + file_name + ".xlsx", sheet_name="Summary", index=False)

    return df, df1, ldf


df = data_import.create_data_frame()
df1 = data_import.create_data_frame1()
ldf = data_import.create_lookup_data_frame()

# Runs this function in script
data_prep(df, df1, ldf)