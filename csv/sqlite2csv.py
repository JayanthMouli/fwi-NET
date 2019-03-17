import sqlite3

with open('/Desktop/fire/fire.csv', 'w+') as write_file:
# open a file to write to
    conn = sqlite3.connect('/Desktop/fire/FPA_FOD_20170508.sqlite')
    # connect to your database
    cursor = conn.cursor()
    # create a cursor object (which lets you address the table results individually)
    for row in cursor.execute('SELECT * FROM fires'):
    # use the cursor as an iterable
        write_file.write(row)
        # write to the csv, then you can open the csv in Excel.
        # Open up your csv in Excel.
# You can also use the 'csv' module, which has an Excel dialect.

# Completely untested, so look up the 'sqlite3' and 'csv' modules on:
# https://docs.python.org/3/library/csv.html
#https://docs.python.org/3.4/library/sqlite3.html
