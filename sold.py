import csv
import argparse
import pandas
import datetime
import os


DIR = "C:\\Users\\gerty\\OneDrive\\Documenten\\Winc\\hello-world\\superpy"
os.chdir(DIR)

def sold(args):
    data = {
        "id":[args.id],
        "count":[args.count],
        "sell date":[args.sell_date], 
        "sell price":[args.sell_price], 
        }
    df = pandas.DataFrame(data)
    with open("sold.csv", mode = "a+") as file:  
        total_price = args.count * args.sell_price
        df["total price"] = total_price
        df.to_csv(file, header=file.tell()==0, index=False)   
    print('OK')  
