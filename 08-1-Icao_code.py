import mysql.connector


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='RIRI@eshgh2020',
    autocommit=True
)

def lentokenttä(icao_koodi):
    try:

        kursori = yhteys.cursor()
        sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao_koodi}'"
        kursori.execute(sql)

        tulos = kursori.fetchone()

        if tulos:
            kentän_nimi, sijaintikunta = tulos
            print(f"Lentokentän nimi: {kentän_nimi}")
            print(f"Sijaintikunta: {sijaintikunta}")
        else:
            print("Kenttää ei löytynyt tällä ICAO-koodilla.")

    except mysql.connector.Error as e:
        print(f"Tapahtui virhe: {e}")
    finally:

        kursori.close()


icao_koodi = input("Syötä ICAO-koodi: ")


lentokenttä(icao_koodi)
