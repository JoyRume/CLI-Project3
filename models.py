from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Association table for many-to-many relationship between Room and Service
room_service_association = Table('room_service_association', Base.metadata,
    Column('room_id', Integer, ForeignKey('rooms.id')),
    Column('service_id', Integer, ForeignKey('services.id'))
)

class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    location = Column(String(100))
    description = Column(String(255))

    rooms = relationship("Room", back_populates="hotel")

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()
class Room(Base):
    __tablename__ = 'rooms'

    id = Column(Integer, primary_key=True)
    number = Column(Integer)
    capacity = Column(Integer)
    price_per_night = Column(Integer)
    hotel_id = Column(Integer, ForeignKey('hotels.id'))

    hotel = relationship("Hotel", back_populates="rooms")
    services = relationship("Service", secondary="room_service_association", backref="rooms_assigned", overlaps="rooms_assigned,services")
    bookings = relationship("Booking", back_populates="room")
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

class Service(Base):
    __tablename__ = 'services'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)

    rooms_associated = relationship("Room", secondary="room_service_association", backref="services_assigned", overlaps="rooms_assigned,services")

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()


class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    check_in_date = Column(Date)
    check_out_date = Column(Date)
    room_id = Column(Integer, ForeignKey('rooms.id'))

    room = relationship("Room", back_populates="bookings")
    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

if __name__ == '__main__':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)