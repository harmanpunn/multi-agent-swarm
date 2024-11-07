import sqlite3

def load_sql_script():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    
    # Execute SQL script to create and populate the tasks table
    with open('tasks_schema.sql', 'r') as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()

    with open('tasks_mock_data.sql', 'r') as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()


    
    # Query the table to make sure things are looking good
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(task)
    
    conn.close()
    print("Database initialized with tables and sample data.")


def load_sql_script_2():
    conn = sqlite3.connect('analytics.db')
    cursor = conn.cursor()

    # Execute SQL script to create and populate the analytics table
    with open('sales_and_customer_schema.sql', 'r') as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()

    with open('sales_and_customer_mock_data.sql', 'r') as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    conn.commit()

    # Query the table to make sure things are looking good
    cursor.execute("SELECT * FROM sales")
    sales = cursor.fetchall()
    for sale in sales:
        print(sale)

    conn.close()
    print("Database initialized with tables and sample data.")


if __name__ == "__main__":
    load_sql_script()
    load_sql_script_2()
