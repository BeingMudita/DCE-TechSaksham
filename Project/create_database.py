import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('food_recommendations.db')
cursor = conn.cursor()

# 🔄 Create the 'food' table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    image TEXT,
    description TEXT,
    cuisine TEXT,
    course TEXT,
    diet TEXT
)
''')

# Load data from CSV
df = pd.read_csv('indian_food_recipes.csv')

# Insert data into the 'food' table
for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO food (name, image, description, cuisine, course, diet)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (row['name'], row['image_url'], row['description'], row['cuisine'], row['course'], row['diet']))

# Commit and close the connection
conn.commit()
conn.close()

print("Data inserted successfully!")
