from sqlalchemy import create_engine

def connect():
    engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
    return engine