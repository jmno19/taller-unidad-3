from mysql.connector import Error
import mysql.connector
import pandas as pd

try:
    df = pd.read_excel('data1.xlsx', sheet_name='Data')
    data = [tuple(x) for x in df.to_numpy()]
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='1234567890',  
        db='mi_db_1'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO usuarios (employee_id, full_name, job_title, department, business_unit, gender, ethnicity, age, annual_salary, bonus, country, city) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", data)
        
        if len(data) == cursor.rowcount:
            connection.commit()
            print("{} Filas insertadas exitosamente.".format(len(data)))
        else:
            connection.rollback()
            print("Error: No coinciden las filas, se revirtió la operación.")

except Error as ex:
    print("Error en la conexion o base de datos: {}.".format(ex))
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Conexion cerrada.")