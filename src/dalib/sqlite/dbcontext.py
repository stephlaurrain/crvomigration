from datetime import datetime

from dalib.sqlite.models import Categories, CategoriesObjets, Contacts, \
    ContactsProjets, Decisionnel, Etiquettes, Fleches, Images, Liens, \
    Notes, Objectifs, Params, Projets, Rappels, TypesCategories, TypesProjets, Visuas
from sqlalchemy import create_engine
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
    
    def get_decisionnel_list(self):
        return self.session.query(Decisionnel).all()
    
    def get_etiquettes_list(self):
        return self.session.query(Etiquettes).all()
    
    def get_fleches_list(self):
        return self.session.query(Fleches).all()
    
    def get_images_list(self):
        return self.session.query(Images).all()
    
    def get_liens_list(self):
        return self.session.query(Liens).all()
    
    def get_notes_list(self):
        return self.session.query(Notes).all()
    
    def get_objectifs_list(self):
        return self.session.query(Objectifs).all()
    
    def get_params_list(self):
        return self.session.query(Params).all()
    
    def get_projets_list(self):
        return self.session.query(Projets).all()
    
    def get_rappels_list(self):
        return self.session.query(Rappels).all()
    
    def get_types_categories_list(self):
        return self.session.query(TypesCategories).all()
    
    def get_types_projets_list(self):
        return self.session.query(TypesProjets).all()
    
    def get_visuas_list(self):
        return self.session.query(Visuas).all()

    # disconnection        
    def disconnect(self):   
        self.session.close()
        self.session.bind.dispose()
        self.connection.close()        
        self.engine.dispose()

        
                

