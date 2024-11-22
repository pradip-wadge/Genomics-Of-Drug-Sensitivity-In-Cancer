import pandas as pd
import mysql.connector

# MySQL connection details
db_host = "127.0.0.1"
db_user = "root"
db_password = "12345678"
db_name = "gdsc"  # Database name is "gdsc"

# Step 1: Establish connection to MySQL
try:
    connection = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    
    if connection.is_connected():
        print("Connected to MySQL Database")
        cursor = connection.cursor()

        # Step 2: Drop all existing tables in the database
        cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for table in tables:
            drop_table_query = f"DROP TABLE IF EXISTS {table[0]}"
            cursor.execute(drop_table_query)
            print(f"Dropped table {table[0]}")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
        
        # Step 3: Read the Main GDSC Dataset
        gdsc_path = "E:/DA Projects/GDSC/GDSC_DATASET.csv"
        gdsc_df = pd.read_csv(gdsc_path)

        # Clean the dataset (e.g., handle missing values as needed)
        gdsc_df.fillna(0, inplace=True)  # Example: fill missing values with 0

        # Helper function to create table and insert data
        def create_and_insert_table(df, table_name):
            # Define SQL types for each column based on pandas dtype
            columns = []
            for col in df.columns:
                # Enclose column names with spaces in backticks
                col_name = f"`{col}`" if ' ' in col else col
                col_type = "FLOAT" if df[col].dtype in ["float64", "float32"] else "VARCHAR(255)"
                columns.append(f"{col_name} {col_type}")
                
            column_definitions = ', '.join(columns)
            
            # Create table
            create_table_query = f"""
            CREATE TABLE {table_name} (
                {column_definitions}
            )
            """
            cursor.execute(create_table_query)
            
            # Insert data into the table
            for _, row in df.iterrows():
                placeholders = ', '.join(['%s'] * len(row))
                insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
                try:
                    cursor.execute(insert_query, tuple(row))
                except mysql.connector.Error as insert_error:
                    print(f"Error inserting row into {table_name}: {insert_error}")
                    continue  # Skip this row if insertion fails
            
            connection.commit()
            print(f"Data inserted into {table_name} table successfully.")
        
        # Create table and insert data
        create_and_insert_table(gdsc_df, "GDSC_Dataset")

except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
