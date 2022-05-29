from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    venmo_id = Column(Integer)
    access_token = Column(Integer)
    phone_no = Column(Integer)

    def __repr__(self):
        return "<Users(id='{}', venmo_id='{}', access_token='{}', phone_no='{}')>"\
            .format(self.id, self.venmo_id, self.access_token, self.phone_no)

class Requests(Base):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    sender_id = Column(Integer)
    rec_id = Column(Integer)
    amount = Column(Integer)
    note = Column(String)
    frequency = Column(Integer)
    start_date = Column(Integer)
    end_date = Column(Integer)
    next = Column(Integer)

    def __repr__(self):
        return '''<Requests(id='{}', sender_id='{}', rec_id='{}', amount='{}', 
        note='{}', frequency='{}', start_date='{}', end_date='{}', next='{}')>'''\
            .format(self.id, self.sender_id, self.rec_id, self.amount, self.frequency, self.start_date, self.end_date, self.next)

class Devices(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    device_id = Column(Integer)

    def __repr__(self):
        return "<Users(id='{}', user_id='{}', device_id='{}')>"\
            .format(self.id, self.user_id, self.device_id)

def connect():
    engine = create_engine('postgresql://postgres:jainaryan7@localhost:5432/venmo_scheduler')
    Session = sessionmaker(engine)
    return Session()

def insert_or_update_user(session, v_id, access, number):
    record = session.query(Users).filter(Users.venmo_id == v_id).first()
    if not record:
        add_user = Users(
            venmo_id = v_id,
            access_token = access,
            phone_no = number
        )
        session.add(add_user)
    else:
        session.query(Users).filter(Users.venmo_id == v_id).\
            update({'access_token': access})
    session.commit()

def insert_request(session, sender, rec, amt, note, frq, stdate, enddate):
    # calc req 
    nxt = stdate + frq 
    add_request = Requests(
        sender_id = sender, 
        rec_id = rec, 
        amount = amt, 
        note = note,
        frequency = frq, 
        start_date = stdate, 
        end_date = enddate,
        next = nxt
    )
    session.add(add_request)
    session.commit()

def insert_device(session, usr_id, dev):
    add_device = Devices(
        user_id = usr_id,
        device_id = dev
    )
    session.add(add_device)
    session.commit()

def update_next(session, id):
    record = session.query(Requests).filter(Requests.id == id).first()
    update_next = int(record.next) + int(record.frequency)

    if update_next > int(record.end_date):
        session.delete(record)
    else:
        session.query(Requests).filter(Requests.id == id).\
            update({'next': Requests.next + Requests.frequency})
    
    session.commit()

def get_requests(session, time):
    records = session.query(Requests).filter(Requests.next <= time).all()
    return records
    
# def refresh(session, id): # low priority 
# insert_or_update_user(connect(), 1, 1234, 847)








