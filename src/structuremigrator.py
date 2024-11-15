import datetime
import inspect
import os

import utils.file_utils as file_utils
import utils.jsonprms as jsonprms
import utils.mylog as mylog

import sqlite3
import mysql.connector
from utils.mydecorators import _error_decorator

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

    def main(self):
        self.init_main("default")
        # Connexion à la base de données SQLite
        sqlite_conn = sqlite3.connect(f"{self.root_app}{os.path.sep}data{os.path.sep}database{os.path.sep}{self.jsprms.prms['sqlite_dbpath']}")
        sqlite_cursor = sqlite_conn.cursor()

        # Connexion à la base de données MariaDB
        root_db = self.jsprms.prms['maria']
        mariadb_conn = mysql.connector.connect(
            host=root_db['host'],
            user=root_db['user'],
            password=root_db['pssword'],
            database=root_db['database']
        )
        mariadb_cursor = mariadb_conn.cursor()

        # Extraire la liste des tables de SQLite
        sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name<>'sqlite_sequence';")
        tables = sqlite_cursor.fetchall()        
        for table_name in tables:
            table_name = table_name[0]
            # Extraire les données de la table SQLite
            sqlite_cursor.execute(f"SELECT * FROM {table_name}")
            rows = sqlite_cursor.fetchall()
            
            # Obtenir la structure de la table
            sqlite_cursor.execute(f"PRAGMA table_info({table_name})")
            columns = sqlite_cursor.fetchall()
            # Créer la table dans MariaDB
            create_table_query = f"CREATE TABLE {table_name} ("
            column_definitions = []
            print(columns) 
            for column in columns:
                col_name = column[1]
                col_type = column[2]
                if 'INTEGER' in col_type:
                    col_type = col_type.replace('INTEGER', 'INT')
                if 'CHAR' in col_type:
                    col_type = col_type.replace('CHAR', 'VARCHAR')            
                    if '(' not in col_type:
                          col_type +="(255)"
                print(column[2])
                column_definitions.append(f"{col_name} {col_type}")
            create_table_query += ', '.join(column_definitions) + ');'
            print(create_table_query)            
            try:
                mariadb_cursor.execute(create_table_query)
            except mysql.connector.Error as err:            
                print(f"Erreur lors de la création de la table {table_name}: {err}")
                raise err
        # Fermer les connexions
        sqlite_conn.close()
        mariadb_conn.close()

        print("Migration structure terminée avec succès !")