import sqlite3
import mysql.connector

import inspect
import os

import utils.file_utils as file_utils
import utils.jsonprms as jsonprms
import utils.mylog as mylog
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
        conn_mariadb = mysql.connector.connect(
            host=root_db['host'],
            user=root_db['user'],
            password=root_db['pssword'],
            database=root_db['database']
        )
        cursor_mariadb = conn_mariadb.cursor()

        # Récupérer la liste des tables SQLite
        sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' and name<>'sqlite_sequence';")
        tables = sqlite_cursor.fetchall()
        # Créer les tables dans MariaDB
        for table in tables:
            table_name = table[0]
            # Récupérer la structure de la table SQLite
            sqlite_cursor.execute(f"PRAGMA table_info({table_name});")
            columns = sqlite_cursor.fetchall()

            # Construire la requête SQL pour créer la table dans MariaDB
            create_table_sql = f"CREATE TABLE {table_name} ("
            for column in columns:
                column_name = column[1]
                data_type = column[2]
                # Convertir les types de données si nécessaire (par exemple, INTEGER en INT)
                if 'INTEGER' in data_type:
                    data_type = data_type.replace('INTEGER', 'INT')
                if 'CHAR' in data_type:
                    data_type = data_type.replace('CHAR', 'VARCHAR')            
                    if '(' not in data_type:
                          data_type +="(255)"
                create_table_sql += f"{column_name} {data_type},"
            create_table_sql = create_table_sql[:-1] + ");"
            print(create_table_sql)
            
            # Exécuter la requête pour créer la table
         
            cursor_mariadb.execute(create_table_sql)
        """
            # Insérer les données dans les tables MariaDB
            for table in tables:
                table_name = table[0]
                # Récupérer les données de la table SQLite
                sqlite_cursor.execute(f"SELECT * FROM {table_name};")
                data = sqlite_cursor.fetchall()

                # Construire la requête SQL pour insérer les données dans MariaDB
                insert_sql = f"INSERT INTO {table_name} VALUES (%s," * (len(data[0]) - 1) + "%s)"
                cursor_mariadb.executemany(insert_sql, data)

            # Valider les changements
            conn_mariadb.commit()

            # Fermer les connexions
    
            conn_mariadb.close()
        """
        sqlite_conn.close()
        print("Migration terminée avec succès.")