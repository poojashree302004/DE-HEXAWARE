import pandas as pd
import pyodbc

# Step 1: Read Excel
df = pd.read_excel("Oyo_City.xlsx", engine='openpyxl')

# Step 2: Connect to SQL Server
conn = pyodbc.connect(
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=localhost;'
    'Database=OYO;'   # Change this to your DB
    'UID=sa;'
    'PWD=Poojashree;'
)
cursor = conn.cursor()

# Step 3: Optional – Create Table (Only if it doesn't exist)
cursor.execute("""
IF NOT EXISTS (
    SELECT * FROM INFORMATION_SCHEMA.TABLES 
    WHERE TABLE_NAME = 'Hotels'
)
BEGIN
    CREATE TABLE Hotels (
        hotel_id INT PRIMARY KEY,
        city VARCHAR(50)
    )
END
""")
conn.commit()

# Step 4: Insert Data from Excel
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO Hotels (hotel_id, city)
        VALUES (?, ?)
    """, row['hotel_id'], row['city'])

conn.commit()
cursor.close()
conn.close()

print("✅ Excel data inserted into SQL Server successfully!")
