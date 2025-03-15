import mysql.connector
from geopy.distance import geodesic


connector = mysql.connector.connect(
  host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='RIRI@eshgh2020',
    autocommit=True
)

cursor = connector.cursor()



def coordinates(icao_code):
    query = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()

    if result:
        latitude, longitude = result
        return (latitude, longitude)




icao1 = input("Anna lentokentän ICAO-koodi: ")
icao2 = input("Anna toisen lentokentän ICAO-koodi: ")

coordinates1 = coordinates(icao1)
coordinates2 = coordinates(icao2)

if coordinates1 and coordinates2:

    distance = geodesic(coordinates1, coordinates2).kilometers
    print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {distance:.2f} km.")



cursor.close()
connector.close()
