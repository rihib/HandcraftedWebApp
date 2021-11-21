from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///my_webapp.db')
Model = declarative_base()

class User(Model):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True)    
    email = Column(String(255))    # 問題点：emailも重複がないようにしたい
    password = Column(String(255))

def register(input_email, input_password):
    new_user = User(email=input_email, password=input_password)
    session.add(new_user)
    session.commit()

def retrieve():
    user_id = None
    email = None
    password = None
    user_info = {
        'USER_ID': user_id,
        'EMAIL': email,
        'PASSWORD': password,
    }
    return user_info

def login(input_email, input_password):  
    login_user_list = session.query(User).filter(User.email==input_email).all()
    if len(login_user_list) == 1:
        for user in login_user_list:
            login_user = user
    else:
        return False
    email = login_user.email
    password = login_user.password
    return input_email == email and input_password == password

def update():
    pass

def delete():
    pass


Model.metadata.create_all(engine)

SessionClass = sessionmaker(engine)
session = SessionClass()