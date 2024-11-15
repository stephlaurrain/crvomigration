from datetime import datetime

import utils.date_utils as date_utils
from sqlalchemy import and_, case, create_engine, func
from sqlalchemy.orm import sessionmaker
from dalib.mariadb.models import Category, CategoryObject, Contact, ContactProject, \
    Decisional, Sticker, Arrow, Picture, Link, Note, Goal, Params, Project, \
    Reminder, TypeCategory, TypeProject, Visuas 


class Dbcontext:
    
    def __init__(self, log):
        self.log = log            

    def set_maria_params(self,host, user, password, database):
        self.engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    
    def connect(self):
        self.connection = self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()     

    def get_category_obj(self):
        return Category()

    def add_to_db(self, obj):        
        self.session.add(obj)  
        self.session.commit() 
    
    def get_category_object_obj(self):
        return CategoryObject()
        

    # disconnection        
    def disconnect(self):   
        self.session.close()
        self.session.bind.dispose()
        self.connection.close()        
        self.engine.dispose()

        
                

