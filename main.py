# Imports
import argparse
import csv
import os
from datetime import date
import pandas
import sys
from bought import bought, read_bought
from sold import sold
from inventory import inv
from revenue import rev
from profit import prof

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

parser = argparse.ArgumentParser(description = "Stock overview")
subparser = parser.add_subparsers(dest = "command")

buy = subparser.add_parser("buy")
buy.add_argument("product_name", type = str, help = "Name of the bought product.")
buy.add_argument("count", type = int, help = "Number of product bought.")
buy.add_argument("buy_date", type = str, help = "Buy date of the product (yyyy-mm-dd).")
buy.add_argument("buy_price", type = float, help = "Payd price for the bought product.")
buy.add_argument("exp_date", type = str, help = "Date of experation of the product (yyyy-mm-dd).")

read = subparser.add_parser("read")

sell = subparser.add_parser("sold")
sell.add_argument("product_name", type = str, help = "Name of the sold product.")
sell.add_argument("count", type = int, help = "Number of products sold")
sell.add_argument("sell_date", type = str, help = "Selling date of the product (yyyy-mm-dd).")
sell.add_argument("sell_price", type = float, help = "Payd price for the sold product.")

inventory = subparser.add_parser("inventory")
revenue = subparser.add_parser("revenue")
profit = subparser.add_parser("profit")

args = parser.parse_args()


if args.command == "buy":
    bought(args)
if args.command == "read":
    read_bought()
if args.command == "sold":
    sold(args)
if args.command == "inventory":
    inv()
if args.command == "revenue":
    rev()
if args.command == "profit":
    prof()






