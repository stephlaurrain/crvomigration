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

    def get_categorie_list(self):
        return self.session.query(Categories).all()

    def get_categorie_objets_list(self):
        return self.session.query(CategoriesObjets).all()

    def get_contacts_list(self):
        return self.session.query(Contacts).all()

    def get_contacts_projets_list(self):
        return self.session.query(ContactsProjets).all()


    """
    , Contacts, \
    ContactsProjets, Decisionnel, Etiquettes, Fleches, Images, Liens, \
    Notes, Objectifs, Params, Projets, Rappels, TypesCategories, TypesProjets, Visuas
    """
    # disconnection        
    def disconnect(self):   
        self.session.close()
        self.session.bind.dispose()
        self.connection.close()        
        self.engine.dispose()

        
                

