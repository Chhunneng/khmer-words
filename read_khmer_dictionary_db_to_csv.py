import sqlite3
import csv

# Database file and output CSV file
db_file = "khmer_dictionary.db"
csv_file = "khmer_dictionary.csv"

# Connect to the database
conn = sqlite3.connect(db_file)

# Create a cursor object
cursor = conn.cursor()

# Query to fetch all data from the `dict` table
query = "SELECT word, definition FROM dict"

# Execute the query
cursor.execute(query)

# Fetch all rows from the result
rows = cursor.fetchall()

# Write the data to a CSV file
with open(csv_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    
    # Write the header (column names)
    writer.writerow(["word", "definition"])
    
    # Write the rows
    writer.writerows(rows)

# Close the database connection
conn.close()

print(f"Data from the `dict` table has been written to {csv_file}")
