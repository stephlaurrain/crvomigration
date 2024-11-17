from datetime import datetime

import utils.date_utils as date_utils
from sqlalchemy import and_, case, create_engine, func, text
from sqlalchemy.orm import sessionmaker
from dalib.mariadb.models import Category, CategoryObject, Contact, ContactProject, \
    Decisional, Sticker, Arrow, Picture, Link, Note, Goal, Param, Project, \
    Reminder, TypeCategory, TypeProject, Visua 


class Dbcontext:
    
    def __init__(self, log):
        self.log = log            

    def set_maria_params(self,host, user, password, database):
        self.engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}/{database}")
    
    def connect(self):
        self.connection = self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()     

    def execute_script(self, sql_script):
        with self.engine.connect() as connection:
            connection.execute(text(sql_script))
            connection.commit() 

    def execute_script_from_file(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            sql_script = file.read()
            
        for statement in sql_script.split(';'): 
            if statement.strip(): 
                self.execute_script(statement)            
    

    def add_to_db(self, obj):        
        self.session.add(obj)  
        self.session.commit() 

    def get_category_obj(self):
        return Category()

    def get_category_object_obj(self):
        return CategoryObject()

    def get_contact_obj(self):
        return Contact()
    
    def get_contact_project_obj(self):
        return ContactProject()
    
    def get_decisional_obj(self):
        return Decisional()
    
    def get_sticker_obj(self):
        return Sticker()
    
    def get_arrow_obj(self):
        return Arrow()
    
    def get_picture_obj(self):
        return Picture()
    
    def get_link_obj(self):
        return Link()
    
    def get_note_obj(self):
        return Note()
    
    def get_goal_obj(self):
        return Goal()

    def get_param_obj(self):
        return Param()

    def get_project_obj(self):
        return Project()

    def get_reminder_obj(self):
        return Reminder()

    def get_type_category_obj(self):
        return TypeCategory()

    def get_type_project_obj(self):
        return TypeProject()

    def get_visua_obj(self):
        return Visua()
    
    # disconnection        
    def disconnect(self):   
        self.session.close()
        self.session.bind.dispose()
        self.connection.close()        
        self.engine.dispose()

        
                

