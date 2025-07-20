import pandas as pd
import pyodbc

# Read Excel file
df = pd.read_excel("Oyo_Sales.xlsx")

# Convert date columns to datetime
df['check_in'] = pd.to_datetime(df['check_in'])
df['check_out'] = pd.to_datetime(df['check_out'])
df['date_of_booking'] = pd.to_datetime(df['date_of_booking'])

# Connection to SQL Server
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=OYO;"
    "UID=sa;"
    "PWD=Poojashree"
)

cursor = conn.cursor()

# Insert row by row
for index, row in df.iterrows():
    cursor.execute("""
        INSERT INTO BookingDetails (booking_id, customer_id, status, check_in, check_out, no_of_rooms, hotel_id, amount, discount, date_of_booking)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        row['booking_id'], row['customer_id'], row['status'],
        row['check_in'], row['check_out'], row['no_of_rooms'],
        row['hotel_id'], row['amount'], row['discount'], row['date_of_booking']
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Data inserted successfully from Excel to SQL Server.")
