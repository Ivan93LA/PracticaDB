import pandas as pd
import mysql.connector
from mysql.connector import Error

# Aqui se ponen los datos necesarios para realizar la conexion

cnx = mysql.connector.connect(user='IvanLeon', 
                              password='1993',
                              host='127.0.0.1',
                              database='my_database')
#cnx.close()


mycursor = cnx.cursor(buffered=True)

mycursor.execute("SELECT * FROM product_product")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
# Obtener los días con stock
stock_query = """
     
    SELECT 
        product_id, 
        COUNT(DISTINCT date) AS days_with_stock
    FROM 
        stock_history
    WHERE 
        date >= CURRENT_DATE - INTERVAL '60' DAY
        AND quantity > 0
    GROUP BY 
        product_id

"""


# Obtener las ventas diarias, con las 3 comillas se puede ejecutar la sentencia sql
sales_query = """

    SELECT 
        sol.product_id,
        so.date AS sale_date,
        SUM(sol.price_subtotal) AS daily_sales
    FROM 
        sale_order_line sol
        JOIN sale_order so ON sol.order_id = so.id
    WHERE 
        so.date >= CURRENT_DATE - INTERVAL '60' DAY and  so.state = 'aprobado' and sol.state= 'aprobado'
    GROUP BY 
        sol.product_id, so.date;

"""

StockedDays = pd.read_sql_query(stock_query, cnx)
print("Estos son los Stocked days", StockedDays)


# Ejecutar la consulta y obtener las ventas diarias en un DataFrame

try:
    # Ejecutar la consulta y obtener el resultado
    sales_diary = pd.read_sql_query(sales_query, cnx)   
    myresult = mycursor.fetchall()
    print( "Estas son las ventas diarias:")
    print(sales_diary)

except Exception as e:
    # Manejar cualquier excepción que ocurra
    myresult = mycursor.fetchall()
    print(f"Se produjo un error al ejecutar la consulta: {e}")


#Creo pequeñas funciones de operandos
# Calcular la media diaria de ventas
# Unir las ventas diarias con los días con stock, on y how no los conocía y busqué por stakOverflow como crear la union que en ese caso es toda...inner join
def unir_ventas(sales_diary, StockedDays):
    result_media = pd.merge(sales_diary, StockedDays, on='product_id', how='inner')
    print(result_media)
    return result_media


# Calcular la media diaria de ventas por producto 
#Chat GPT recomendó crear la funcion "Transform" para sumar todos los valores del daily_sales
def calcula_media_diaria(result_media):   
    result_media['avg_daily_sales'] = result_media.groupby('product_id')['daily_sales'].transform('sum') / result_media['days_with_stock']
    print(result_media)
    return result_media

# Eliminar duplicados para obtener un dato final con una fila por producto

def eliminar_duplicados(result_media):
    final_result = result_media[["product_id", "avg_daily_sales"]].drop_duplicates()
    return final_result