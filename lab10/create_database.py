import sys

from sqlalchemy import ForeignKey, String, Column, Integer, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Station(Base):
    __tablename__ = 'stations'
    station_id = Column(Integer, primary_key=True)
    station_name = Column(String, nullable=False)


class Rental(Base):
    __tablename__ = 'rentals'
    rental_id = Column(Integer, primary_key=True)
    bike_number = Column(Integer, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    rental_station = Column(Integer, ForeignKey('stations.station_id'), nullable=False)
    return_station = Column(Integer, ForeignKey('stations.station_id'), nullable=False)


def create_database(db_name):
    engine = create_engine(f"sqlite:///{db_name}.sqlite3")
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uzycie: python create_database.py <database_name>")
        sys.exit(1)

    db_name = sys.argv[1]
    create_database(db_name)
    print(f"Baza danych {db_name}.sqlite3 utworzona pomyslnie.")
