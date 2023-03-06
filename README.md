
The Assignment SuperPy

SUPERPY is a Command Line Tool for a supermarket to keep track of their inventory en to make reports of various kinds of data like profit and revenue over a certain period of time, or to see what and the amount of products that are in stock. 

To build this tool the following the following standard libraries of Python had to be used:
-	CSV files, to store the data
-	Argparse, to build the command line tool, to parse to the csv file
-	Datetime, to set ‘today’ to a certain date and make it possible to go back and forth in time to get the reports from that day or period of time.


First: what to install?

Assuming Python and Pip is installed, the following third-party libraries have to be installed:

PANDAS

	pip install pandas

TABULATE

	pip install tabulate


How to use the CLI?

To start: you always have to start by typing in python main.py followed by a command. The commands are:

-	buy
-	read
-	sold
-	write
-	inventory
-	revenue
-	revenuemonth
-	revenueyear
-	profit
-	profitmonth
-	profityear

 
Let’s see what these commands do:

Buy: By using the command buy, you can add a product to the inventory of the supermarket. Fill in the id, the product name, the number of products that are bought, the buy date, the buy price and the expiration date. For example:

	python main.py buy 3 rice 40 2022-12-03 1.39 2023-10-19


Read: If you want to see a list of all the products that are bought, you can fill in read, that will show a table with all the products.

	python main.py read


Sold: Next, by using the command sold, you can make a list of the products that has been sold. Therefor you have to fill in the id of the product, the number of the product sold, the sell date and the sell price.

	python main.py sold 3 15 2022-12-20 1.99


Write: To actually remove the count of the sold products from the inventory you have to write it to the inventory by using the command write. You only have to fill in the id of the product that has been sold.

    python main.py write 3


Inventory: We can now see the inventory of today or of a day in the past or future. Simply type in the number of days you want to look back or ahead (if you want to go back in time you have to put ‘-‘ in front of the number) or a 0 for todays inventory. 

	python main.py inventory 0



Revenue: Now to see the revenue of a certain day, we can use the command revenue followed by the number of days you want to look back or into the future. If you want to see the revenue of today, you can fill in a ‘0’. If you want to go back in time you have to put a  ‘-‘ in front of the number like -3.

	python main.py revenue 8


Revenuemonth: You can also see the revenue of a whole month. To see that, you have to fill in the month as a number (1 for January, 2 for February, 3 for March etc.) followed by the year you want the revenue of.

	python main.py revenuemonth 9 2022

Revenueyear: For the revenue of a whole year you can fill in the year you want the revenue of.

	python main.py revenueyear 2023


Profit: The same goes for the profit: to see the profit of a certain day, we can use the command profit followed by the number of days you want to look back or into the future. If you want to see the profit of today, you can fill in a ‘0’. If you want to go back in time you have to put a  ‘-‘ in front of the number like -3.

	python main.py profit -2


Profitmonth: For the profit of a month, fill in the month and the year you want to see the profit of.

	python main.py profit 2 2023


Profityear: For the profit of a whole year, fill in the year you want to see the profit of.

	python main.py profit 2022



