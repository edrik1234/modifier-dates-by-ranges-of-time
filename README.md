notes and explanations of each line:
Readme explanation:
📌 Lines 1–3:
Import the required libraries:

-pandas for handling table-like data (DataFrames),

-datetime and time for date/time manipulation,

-csv for manually reading CSV files row by row.
#########################################
Lines 5–7:
-Define the file path to your CSV file:
-file_path stores the location of the CSV file you'll read.
🟢 User Note:
You must manually change this path to match the location of your CSV file on your computer.
For example, change it to:
"C:\\Users\\YourName\\Documents\\your_file.csv"
##############################################
Lines 9–14:
Open and read the CSV manually:

-Read the entire CSV into a list of rows.

-Use the 3rd row (index 2) as the column headers.

-Use all rows starting from the 4th row (index 3) as the actual data.
#################################################
 Line 17:
Create a DataFrame using the data and headers:

-Builds a structured table (df) with labeled columns using pandas.
###################################################
Lines 19–21:
Define two date strings that will be assigned based on time:

-date_input_1: used for times after or equal to 20:00:00 (8 PM).

-date_input_2: used for times before 20:00:00.

🟢 User Input Required:
You need to manually choose these two dates(each date in format dd:mm:yyyy):
date_input_1: will be assigned to rows where Time is between 20:00 (8 PM) and 00:00.

date_input_2: will be assigned to rows where Time is between 00:00 and before 20:00 (8 PM).
######################################################
Lines 24–25:
Convert the date strings to real datetime objects:

-Makes the dates usable for formatting and comparison later.
######################################################
Lines 28–32:
Search for the "Time" column in the DataFrame:

- Loop through column names and check for a case-insensitive match to "Time".

- Save the matched column name in time_column.
#######################################################
Line 35:
Define the evening cutoff time:

- evening_threshold is set to 8:00 PM (20:00:00) to determine which date to apply.
########################################################
Lines 37–47:
Define a function assign_date(val):

-Tries to convert the input val (a time string) into a time object.

-If the time is greater than or equal to 8:00 PM, return date1.

-If the time is before 8:00 PM, return date2.

-If conversion fails (bad format), return "Invalid".
########################################################
Lines 50–58:
Apply the time-based logic and export a new CSV:

-If a "Time" column was found:

-Apply assign_date() to each value in that column.

-Store the result in a new "Date" column.

-Save the updated DataFrame as a new CSV on the desktop.

-Print a success message.

-If no "Time" column was found, print an error.

🟢 User Note for Line 54:
You need to decide where you want to save the output file, and what name you want to give the output file.
Example:
you want that your output file name will be extra_easy:
"C:\\Users\\YourName\\Documents\\extra_easy.csv"





