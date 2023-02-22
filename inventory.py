import pandas as pd
import csv

def inv():
    df1 = pd.read_csv("bought.csv")
    df2 = pd.read_csv("sold.csv")


# compare the two dataframes
    df_diff = df1.compare(df2)

# print the differences between the two dataframes
    print(df_diff)



"""


    df1 = pd.read_csv("bought.csv")
    df2 = pd.read_csv("sold.csv")

    count_to_subtract = df2["count"].iloc[0]

    df1["count"] = df1["count"] - count_to_subtract

    df1.to_csv("inventory.csv", index=False)
    """
    