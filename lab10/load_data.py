import sys
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from create_database import Base, Station, Rental


def load_data(csv_file, db_name):
    engine = create_engine(f"sqlite:///{db_name}.sqlite3")
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        seen_stations = {}
        next_station_id = 1
        seen_rentals = set()

        for row in reader:
            start_station_name = row['Stacja wynajmu']
            end_station_name = row['Stacja zwrotu']

            if start_station_name not in seen_stations:
                seen_stations[start_station_name] = next_station_id
                session.merge(Station(
                    station_id=next_station_id,
                    station_name=start_station_name
                ))
                next_station_id += 1

            if end_station_name not in seen_stations:
                seen_stations[end_station_name] = next_station_id
                session.merge(Station(
                    station_id=next_station_id,
                    station_name=end_station_name
                ))
                next_station_id += 1

            rental_uid = int(row['UID wynajmu'])

            if rental_uid not in seen_rentals:
                rental = Rental(
                    rental_id=rental_uid,
                    bike_number=int(row['Numer roweru']),
                    start_time=datetime.strptime(row['Data wynajmu'], '%Y-%m-%d %H:%M:%S'),
                    end_time=datetime.strptime(row['Data zwrotu'], '%Y-%m-%d %H:%M:%S'),
                    rental_station=seen_stations[start_station_name],
                    return_station=seen_stations[end_station_name]
                )
                session.merge(rental)

    session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uzycie: python load_data.py <csv_file> <nazwa_bazydanych>")
        sys.exit(1)

    csv_file = sys.argv[1]
    db_name = sys.argv[2]
    load_data(csv_file, db_name)
    print(f"Dane z pliku {csv_file} dodane pomyślnie do bazy danych: {db_name}.sqlite3.")
