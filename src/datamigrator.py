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
        for row in sqlite_rows:
                m = self.maria_dbcontext.get_category_obj()
                m.id = row.id
                m.title = row.intitule
                m.color = row.couleur
                m.code = row.code
                m.type_category = row.type_categorie                
                self.maria_dbcontext.add_to_db(m)
    
    def do_category_object(self):
        sqlite_rows = self.sqlite_dbcontext.get_categorie_objets_list()        
        print(sqlite_rows)
        for row in sqlite_rows:
                m = self.maria_dbcontext.get_category_object_obj()               
                m.category_id = row.categories_id
                m.contact_id = 0 if row.contacts_id == '' else row.contacts_id
                m.project_id = row.projets_id                
                self.maria_dbcontext.add_to_db(m)

    def main(self):
        self.init_main("default")
        # Connexion à la base de données SQLite
        self.sqlite_dbcontext = self.get_sqlite_db_context(self.jsprms.prms['sqlite_dbpath'])
        self.maria_dbcontext = self.get_maria_db_context()        
        
        # self.do_category()
        self.do_category_object()
        
        print("Migration terminée avec succès !")