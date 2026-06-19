import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='b55squotgizhaurggsjk-mysql.services.clever-cloud.com',
            user='ua1wonmkoyvugjno',
            password='I65l5FFAMn1nDstI5xO5',
            database='b55squotgizhaurggsjk',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
