import pandas as pd
from datetime import datetime, time
import csv

# File path (update this if needed)
file_path = "C:\\Users\\edrian\\Desktop\\test.csv"
# Step 1: Read the CSV manually

# - Use the 3rd row (index 2) as header
# - Read the data starting from the 4th row (index 3)
with open(file_path, newline='', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    header = reader[2]  # Actual header
    data = reader[3:]   # Actual data

# Step 2: Create DataFrame
df = pd.DataFrame(data, columns=header)

# Step 3: Set the two input dates (you can replace these with user input if needed)
date_input_1 = "14:04:2025"  # for time >= 20:00:00 and < 00:00:00
date_input_2 = "15:04:2025"  # for time >= 00:00:00 and < 20:00:00

# Convert the string dates to datetime objects
date1 = datetime.strptime(date_input_1, "%d:%m:%Y")
date2 = datetime.strptime(date_input_2, "%d:%m:%Y")

# Step 4: Find the 'Time' column (case-insensitive)
time_column = None
for col in df.columns:
    if str(col).strip().lower() == "time":
        time_column = col
        break

# Step 5: Define time logic:
# - If time is >= 20:00:00 → use date1
# - If time is < 20:00:00 → use date2
evening_threshold = time(20, 0, 0)

def assign_date(val):
    try:
        parsed_time = pd.to_datetime(str(val).strip(), format="%H:%M:%S").time()
        if parsed_time >= evening_threshold:
            return date1.strftime("%d/%m/%Y")
        else:
            return date2.strftime("%d/%m/%Y")
    except:
        return "Invalid"

# Step 6: Apply the rule and save the output
if time_column:
    df["Date"] = df[time_column].apply(assign_date)

    # Save updated CSV without the index column
    output_path = "C:\\Users\\edrian\\Desktop\\updated_data.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Done. File saved as: {output_path}")
else:
    print("❌ 'Time' column not found.")
