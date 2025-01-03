import sqlite3

# Specify the database file
db_file = "khmer_dictionary.db"

# Connect to the database
conn = sqlite3.connect(db_file)

# Create a cursor object
cursor = conn.cursor()

query = "SELECT word FROM dict"

# Execute the query
cursor.execute(query)

# Fetch all rows from the result
rows = cursor.fetchall()

# Print each row
with open("khmer_words.txt", "w", encoding="utf-8") as file:
    for row in rows:
        file.write(f"{row[0]}\n")

# Close the connection
conn.close()
