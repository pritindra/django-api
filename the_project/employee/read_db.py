import pandas as pd
from sqlalchemy import create_engine
from models import employee

# Read the CSV file
df = pd.read_csv('employee.csv')

# Save the data to the database
engine = create_engine('snowflake://vickydeka:Vicky1213@GVNUKEQ-WR96016.snowflakecomputing.com/new_employee?warehouse=COMPUTE_WH&schema=new_employee')
df.to_sql('employee', con=engine, if_exists='append', index=False)

# Print the data from the database
for employee in employee.objects.all():
    print(employee)
