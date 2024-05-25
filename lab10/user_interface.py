from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from create_database import Base, Station, Rental


def get_stations(db_name):
    engine = create_engine(f"sqlite:///{db_name}.sqlite3")
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    stations = session.query(Station).all()
    session.close()
    return stations


def get_station_statistics(db_name, station_id):
    engine = create_engine(f"sqlite:///{db_name}.sqlite3")
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    avg_start_duration = session.query(
        func.avg(func.julianday(Rental.end_time) - func.julianday(Rental.start_time)) * 24 * 60).filter(
        Rental.rental_station == station_id).scalar()
    avg_end_duration = session.query(
        func.avg(func.julianday(Rental.end_time) - func.julianday(Rental.start_time)) * 24 * 60).filter(
        Rental.return_station == station_id).scalar()
    unique_bikes = session.query(func.count(func.distinct(Rental.bike_number))).filter(
        Rental.return_station == station_id).scalar()
    num_rentals_starting = session.query(func.count(Rental.rental_id)).filter(
        Rental.rental_station == station_id).scalar()

    session.close()
    return avg_start_duration, avg_end_duration, unique_bikes, num_rentals_starting


def main():
    while True:
        db_name = input("Wpisz nazwę bazy danych (lub wpisz 'q' lub 'quit' żeby zakończyć działanie programu): ")
        if db_name.lower() in ['q', 'quit']:
            print("Koniec działania programu.")
            break

        stations = get_stations(db_name)

        print("Wybierz stację:")
        for station in stations:
            print(f"{station.station_id}. {station.station_name}")

        station_id_input = input("Wpisz id stacji (lub wpisz 'q' lub 'quit' żeby zakończyć działanie programu): ")
        if station_id_input.lower() in ['q', 'quit']:
            print("Koniec działania programu")
            break

        station_id = int(station_id_input)

        avg_start_duration, avg_end_duration, unique_bikes, num_rentals_starting = get_station_statistics(db_name,
                                                                                                          station_id)

        if avg_start_duration is not None:
            print(f"Średni czas trwania przejazdu rozpoczynanego na stacji(w minutach): {avg_start_duration:.2f}")
        else:
            print(f"Średni czas trwania przejazdu rozpoczynanego na stacji: brak danych")

        if avg_end_duration is not None:
            print(f"Średni czas trwania przejazdu kończonego na stacji(w minutach): {avg_end_duration:.2f}")
        else:
            print(f"Średni czas trwania przejazdu kończonego na stacji: brak danych")

        print(f"Liczba różnych rowerów parkowanych na stacji: {unique_bikes}")

        if num_rentals_starting is not None:
            print(f"Liczba wypożyczeń rozpoczynanych na stacji: {num_rentals_starting}")
        else:
            print(f"Liczba wypożyczeń rozpoczynanych na stacji: brak danych")


if __name__ == "__main__":
    main()

