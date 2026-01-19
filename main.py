import psycopg2
connection = psycopg2.connect(
    database="postgres",
    user="postgres",
    password="shraddha123",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()
print("Database connected successfully")

# insert_query = """
# INSERT INTO employees (name,department,salary)
# VALUES (%s,%s,%s);

# """
# cursor.execute(insert_query,("Rahul","finance",90000))
# connection.commit()
# print("Record inserted successfully")

# select_query = "SELECT * FROM employees;"
# cursor.execute(select_query)
# records = cursor.fetchall()
# for row in records:
#     print(row)
    

# update_query = """
# UPDATE employees 
# SET salary = %s
# WHERE name = %s
# """
# cursor.execute(update_query, (8000, "Rahul"))
# connection.commit()
# print("Record updated successfully")

delete_query = """
DELETE FROM employees 
WHERE id = %s
"""
cursor.execute(delete_query, (4,))
connection.commit()
print("Record deleted successfully")

cursor.close()
connection.close()
print("Database connection closed")