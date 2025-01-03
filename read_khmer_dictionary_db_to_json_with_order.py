import sqlite3
import json
import re

# Database file and output JSON file
db_file = "khmer_dictionary.db"
json_file = "khmer_dictionary.json"

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

# List to store cleaned data
cleaned_data = []

# Process and store the cleaned data
index = 1
for row in rows:
    word = row[0]
    definition = row[1]
    cleaned_data.append({"index": index, "word": word, "definition": definition})
    # from index 328, it has wrong order
    index += 1

# Write the cleaned data to a JSON file
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(cleaned_data, file, ensure_ascii=False, indent=4)

# Close the database connection
conn.close()

print(f"Data from the `dict` table has been written to {json_file}")
