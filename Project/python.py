import sqlite3
import traceback  # To print detailed error

try:
    conn = sqlite3.connect('food_recommendations.db')
    cursor = conn.cursor()

    # Check unique values in the database
    for column in ['cuisine', 'diet', 'course']:
        cursor.execute(f"SELECT DISTINCT {column} FROM food")
        print(f"Distinct {column} values:", cursor.fetchall())

    conn.close()

except Exception as e:
    print("An error occurred:")
    traceback.print_exc()  # Print detailed error
