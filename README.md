# spark_test
this repository contains the test details to spark

# Details of Each Folder

>> In the **property_files** folder it has property file with .py extension with data base connection details & one function which is used in one of .py scripts.

1. _spark_test_properties.py_ --> This file has data base connection details & one function which is used in one of .py scripts.


>> In the **sql_scripts** folder it has sql queries (DDLs, DMLs) either in .sql or .py extension.

1. _spark_test_create_tables.sql_ --> This file has the DDLs (create table) statements for the data base tables.

2. _sql_test.sql_ --> This file has the sql queries for the queries for some scenarios that are asked in the document.

3. _spark_test_dervied_layer_insert_query.py_ --> This file has the insert query to insert data into user_analysis table (this can be considered as a derived table created using users, subscription, message tables) & used in _user_analysis_data_load.py_ script.


>> In the **python_scripts** folder it has python scritps to load data from url & run some sql queries.

1. _user_subscription_data_load.py_ --> This python script can be used to laod data from Users URL to Users & subscription tables.

2. _message_data_load.py_ --> This python script can be used to laod data from Message URL to message table.

3. _user_analysis_data_load.py_ --> This pyhton script can be used to laod data from users, subscription, message tables to user_analysis which is a derived table using these 3 tables. 



# Order of execution
1. First execute the statements in _spark_test_create_tables.sql_ file in Data base to create tables.
2. Then Execute _user_subscription_data_load.py_ python file using command : python user_subscription_data_load.py.
3. Then Execute _message_data_load.py_ python file using command : python message_data_load.py.
4. Then Execute _user_analysis_data_load.py_ using command : python user_analysis_data_load.py.
Once the above 4 steps is completed, this ensures that required tables are created in database & data is loaded from the json data format from URLs.
5. Now Finally run _sql_test.sql_ queries in data base to get the output of queries for some scenarios that The Product Owner is interested to see the results.
