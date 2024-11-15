import datetime
import inspect
import os

import utils.file_utils as file_utils
import utils.jsonprms as jsonprms
import utils.mylog as mylog

import sqlite3
import mysql.connector
from utils.mydecorators import _error_decorator

import dalib.sqlite.dbcontext
import dalib.mariadb.dbcontext

class Migrator:

    def trace(self,stck):                
                self.log.lg(f"{stck[0].function} ({ stck[0].filename}-{stck[0].lineno})")

    @_error_decorator()
    def remove_logs(self):
            self.trace(inspect.stack())
            keep_log_time = self.jsprms.prms['keep_log']['time']
            keep_log_unit = self.jsprms.prms['keep_log']['unit']
            self.log.lg(f"=>clean logs older than {keep_log_time} {keep_log_unit}")                        
            file_utils.remove_old_files(f"{self.root_app}{os.path.sep}log", keep_log_time, keep_log_unit)                        

    def init_main(self, jsonfile):
        try:
                self.root_app = os.getcwd()
                self.log = mylog.Log(self.root_app)
                self.log.init(jsonfile)
                self.trace(inspect.stack())
                jsonFn = f"{self.root_app}{os.path.sep}data{os.path.sep}conf{os.path.sep}{jsonfile}.json"                        
                self.jsprms = jsonprms.Prms(jsonFn)                        
                self.log.lg("=HERE WE GO=")                        
                self.remove_logs()
        except Exception as e:
                self.log.errlg(f"Wasted ! : {e}")
                raise

    def get_sqlite_db_context(self, param):
            dbcontext = dalib.sqlite.dbcontext.Dbcontext(self.log)
            dbpath = f"{self.root_app}{os.path.sep}data{os.path.sep}database{os.path.sep}{param}"
            dbcontext.set_sqlite_dbpath(dbpath)
            dbcontext.connect()
            return dbcontext
    
    def get_maria_db_context(self):
            dbcontext = dalib.mariadb.dbcontext.Dbcontext(self.log)
            root_db = self.jsprms.prms['maria']
            host = root_db['host']
            user = root_db['user']
            password = root_db['pssword']
            database = root_db['database']            
            dbcontext.set_maria_params(host, user, password, database)
            dbcontext.connect()
            return dbcontext
    
    def do_category(self):
        sqlite_rows = self.sqlite_dbcontext.get_categorie_list()        
        print(sqlite_rows)
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_category_obj()
                m.id = r.id
                m.title = r.intitule
                m.color = r.couleur
                m.code = r.code
                m.type_category = r.type_categorie                
                self.maria_dbcontext.add_to_db(m)
    
    def do_category_object(self):
        sqlite_rows = self.sqlite_dbcontext.get_categorie_objets_list()        
        print(sqlite_rows)
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_category_object_obj()               
                m.category_id = r.categories_id
                m.contact_id = 0 if r.contacts_id == '' else r.contacts_id
                m.project_id = r.projets_id                
                self.maria_dbcontext.add_to_db(m)
    
    def do_contact(self):
        sqlite_rows = self.sqlite_dbcontext.get_contacts_list()        
        print(sqlite_rows)
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_contact_obj()               
                m.id = r.id
                m.username = r.pseudo
                m.name = r.nom
                m.firstname = r.prenom
                m.nickname = r.surnom
                m.address = r.adresse
                m.zip_code = r.code_postal
                m.town = r.ville
                m.address_work = r.adresse_trav
                m.zip_code_work = r.code_postal_trav
                m.town_work = r.ville_trav
                m.code_building = r.code_immeuble
                m.title = r.titre
                m.company = r.societe
                m.email = r.email
                m.email_work = r.email_trav
                m.phone = r.tel
                m.phone_work = r.tel_trav
                m.phone_cel = r.tel_portable
                m.phone_cel_work = r.tel_portable_trav
                m.phone_fax_work = r.tel_fax_trav
                m.date_birth = r.date_naissance
                m.date_nameday = r.date_fete
                m.status = r.statut
                m.service = r.service
                m.responsable = r.responsables
                m.associate = r.collaborateurs
                m.comment = r.commentaires
                m.site_web = r.site_web
                m.site_web_work = r.site_web_trav
                m.schedules_work = r.horaires_trav
                m.date_delete = r.date_efface
                m.is_visua = r.is_visua
                m.is_synch = r.is_synch
                self.maria_dbcontext.add_to_db(m)

    def main(self):
        self.init_main("default")
        # Connexion à la base de données SQLite
        self.sqlite_dbcontext = self.get_sqlite_db_context(self.jsprms.prms['sqlite_dbpath'])
        self.maria_dbcontext = self.get_maria_db_context()        
        
        # self.do_category()
        # self.do_category_object()
        self.do_contact()
        print("Migration terminée avec succès !")