'''
This python code is to load data to consumption layer table user_analysis using users,message,subscription tables
'''
import pyodbc
import spark_test_properties
import spark_test_dervied_layer_insert_query as src_qry
import pandas as pd
import sys

# Getting connection details from spark_test_properties.py file
conn = spark_test_properties.connection_details()

cursor = conn.cursor()


# This function is to run sql insert command 
def insert_data(query):
	# Insert Data into SQL Server table user_analysis:
	try:
		cursor.execute(query)
	except pyodbc.Error as e:
		print(e)
		sys.exit(1)


src_dt = pd.read_sql_query(
	'''select max(etl_insert_dt) as etl_insert_dt from users;''',
	conn)._get_value(0, 'etl_insert_dt')
tgt_dt = pd.read_sql_query(
	'''select max(etl_insert_dt) as etl_insert_dt from user_analysis;''',
	conn)._get_value(0, 'etl_insert_dt')

# The below condition is to load only recent data or historical data load
if src_dt is not None:
	if tgt_dt is not None:
		if src_dt > tgt_dt:
			query = src_qry.user_analysis_insert_qry + \
					' where u.etl_insert_dt > ' + "'" + str(
				tgt_dt)[0:23] + "'"
			# Calling insert_data function
			insert_data(query)
			print('Delta Data Insertion is completed')
		else:
			print('No latest data to insert')
	else:
		# Calling insert_data function
		insert_data(src_qry.user_analysis_insert_qry)
		print('Full Load/Historical Data Insertion is completed')
else:
	print('No data to insert')
# Commiting the data inserts & Closing the connection
conn.commit()
cursor.close()
