from datetime import datetime

import utils.date_utils as date_utils
from dalib.sqlite.models import Categories, CategoriesObjets, Contacts, \
    ContactsProjets, Decisionnel, Etiquettes, Fleches, Images, Liens, \
    Notes, Objectifs, Params, Projets, Rappels, TypesCategories, TypesProjets, Visuas
from sqlalchemy import and_, case, create_engine, func
from sqlalchemy.orm import sessionmaker


class Dbcontext:
    
    def __init__(self, log):
        self.log = log            

    def set_sqlite_dbpath(self, dbpath):
        self.engine = create_engine(f"sqlite:///{dbpath}")

    def connect(self):
        self.connection = self.engine.connect()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()     

    def get_categorie_obj(self):
        return Categories()

    def get_categorie_list(self):
        return self.session.query(Categories).all()
    
    def get_categorie_objets_obj(self):
        return CategoriesObjets()

    def get_categorie_objets_list(self):
        return self.session.query(CategoriesObjets).all()

    # disconnection        
    def disconnect(self):   
        self.session.close()
        self.session.bind.dispose()
        self.connection.close()        
        self.engine.dispose()

        
                

