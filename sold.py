import csv
import argparse
import pandas
import datetime
import os


DIR = "C:\\Users\\gerty\\OneDrive\\Documenten\\Winc\\hello-world\\superpy"
os.chdir(DIR)

def sold(args):
    data = {
        "product name":[args.product_name], 
        "count":[args.count],
        "sell date":[args.sell_date], 
        "sell price":[args.sell_price], 
        }
    df = pandas.DataFrame(data)
    with open("sold.csv", mode = "a") as file:
        for i in df:
            if i not in df:
                new_df = pandas.DataFrame(data)
                with open("sold.csv", mode = "a") as file:
                    new_df.to_csv(file, header = file.tell()==0, index=False)
        else:    
            df.to_csv(file, header=file.tell()==0, index=False)   
    print('OK')  
