import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='RIRI@eshgh2020',
    autocommit=True
)

cursor = connection.cursor()


maakoodi = input("Anna maakoodi: ")


query = """
SELECT type, COUNT(*) 
FROM airport 
WHERE iso_country = %s 
GROUP BY type;
"""

cursor.execute(query, (maakoodi,))
results = cursor.fetchall()


if results:
    print(f"Lentokenttien lukumäärät maassa {maakoodi}:")
    for airport_type, count in results:
        print(f"{airport_type}: {count} kpl")


cursor.close()
connection.close()
