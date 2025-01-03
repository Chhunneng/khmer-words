import sqlite3
import csv
import re

# Function to clean up the numbers in angle brackets and '/a' tags
def clean_data(text):
    # Remove number references like <"3713">
    cleaned_text = re.sub(r'<"\d+">', '', text)
    
    # Remove '/a' and extra spaces
    cleaned_text = re.sub(r'/a', '', cleaned_text)
    
    # Clean up extra spaces (if any)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

# Database file and output CSV file
db_file = "khmer_dictionary.db"
csv_file = "khmer_dictionary_cleaned.csv"

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
    
    # Process and write the rows
    for row in rows:
        word = clean_data(row[0])  # Clean the word
        definition = clean_data(row[1])  # Clean the definition
        writer.writerow([word, definition])

# Close the database connection
conn.close()

print(f"Data from the `dict` table has been written to {csv_file}")
