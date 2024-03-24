from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Hotel, Room, Service, Booking
import random
from datetime import timedelta
# Initialize Faker generator
fake = Faker()

# Create SQLite engine
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Bind the engine to the base class
Base.metadata.bind = engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
    print("Seeding Data")

    # Create Hotels
    for _ in range(5):
        hotel = Hotel(
            name=fake.company(),
            location=fake.address(),
            description=fake.text()
        )
        session.add(hotel)
    
    session.commit()

    # Create Rooms
    hotels = session.query(Hotel).all()
    for hotel in hotels:
        for _ in range(10):
            room = Room(
                number=fake.random_number(digits=3),
                capacity=random.randint(1, 6),
                price_per_night=random.randint(50, 300),
                hotel=hotel
            )
            session.add(room)

    session.commit()

    # Create Services
    for _ in range(10):
        service = Service(
            name=fake.word()
        )
        session.add(service)
    
    session.commit()

    # Assign Services to Rooms
    rooms = session.query(Room).all()
    services = session.query(Service).all()
    for room in rooms:
        num_services = random.randint(1, len(services))
        for service in random.sample(services, num_services):
            room.services.append(service)

    session.commit()

    # Create Bookings
    for _ in range(20):
        check_in_date = fake.date_between(start_date='-30d', end_date='+30d')
        check_out_date = check_in_date + timedelta(days=random.randint(1, 7))
        room = random.choice(rooms)
        booking = Booking(
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            room=room
        )
        session.add(booking)

    session.commit()

if __name__ == '__main__':
    seed_data()
