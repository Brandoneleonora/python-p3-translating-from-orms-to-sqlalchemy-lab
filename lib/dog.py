from models import Dog

def create_table(base, engine):
    pass
   
def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name)

    for record in query:
        return record

  

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id)

    for record in query:
        return record


def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name, Dog.breed == breed)

    for record in query:
        return record


def update_breed(session, dog, breed):
    dog.breed = breed

    session.commit()
