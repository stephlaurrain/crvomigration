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
                self.log.lg("###############################################")

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
            self.trace(inspect.stack())
            dbcontext = dalib.sqlite.dbcontext.Dbcontext(self.log)
            dbpath = f"{self.root_app}{os.path.sep}data{os.path.sep}database{os.path.sep}{param}"
            dbcontext.set_sqlite_dbpath(dbpath)
            dbcontext.connect()
            return dbcontext
    
    def get_maria_db_context(self):
            self.trace(inspect.stack())
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
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_categorie_list()                
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_category_obj()
                m.id = r.id
                m.title = r.intitule
                m.color = r.couleur
                m.code = r.code
                m.type_category = r.type_categorie                
                self.maria_dbcontext.add_to_db(m)
    
    def do_category_object(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_categorie_objets_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_category_object_obj()               
                m.category_id = r.categories_id
                m.contact_id = 0 if r.contacts_id == '' else r.contacts_id
                m.project_id = r.projets_id                
                self.maria_dbcontext.add_to_db(m)
    
    def do_contact(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_contacts_list()                
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_contact_obj()               
                m.id = r.id
                m.username = r.pseudo
                m.name = r.nom
                m.firstname = r.prenom
                m.nickname = r.surnom
                m.address = r.adresse
                m.zip_code = r.code_postal
                m.city = r.ville
                m.address_work = r.adresse_trav
                m.zip_code_work = r.code_postal_trav
                m.city_work = r.ville_trav
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
    
    def do_contact_project(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_contacts_projets_list()                
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_contact_project_obj()               
                m.contact_id = r.contacts_id
                m.project_id = r.projets_id
                self.maria_dbcontext.add_to_db(m)

    def do_decisional(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_decisionnel_list()                
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_decisional_obj()               
                m.id = r.id
                m.project_id = r.projets_id
                m.scoring = r.notation
                m.solution = r.solution
                m.title = r.intitule
                m.type_decisional = r.type_decisionnel
                self.maria_dbcontext.add_to_db(m)
    
    def do_sticker(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_etiquettes_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_sticker_obj()               
                m.id = r.id
                m.project_id = r.projets_id
                m.color_back = r.couleur_fd
                m.color_write = r.couleur_ec
                m.contain = r.contenu
                m.font = r.font
                self.maria_dbcontext.add_to_db(m)
    
    def do_arrow(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_fleches_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_arrow_obj()               
                m.id = r.id
                m.color = r.couleur
                m.size = r.size
                m.visua_dest_id = r.visuas_dest_id
                m.visua_org_id = r.visuas_org_id
                m.x_dest = r.x_dest
                m.y_dest = r.y_dest
                m.x_org = r.x_org
                m.y_org = r.y_org                
                self.maria_dbcontext.add_to_db(m)

    def do_picture(self):
        self.trace(inspect.stack())               
        sqlite_rows = self.sqlite_dbcontext.get_images_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_picture_obj()               
                m.id = r.id
                m.project_id = r.projets_id
                m.filename = r.nom_fichier
                m.color_back = r.couleur_fd
                m.date_delete = r.date_efface        
                self.maria_dbcontext.add_to_db(m)
    
    def do_link(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_liens_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_link_obj()               
                m.id = r.id
                m.project_id = r.projets_id
                m.title = r.titre
                m.path = r.chemin
                m.is_ged = 0 if r.is_ged == '' else r.is_ged
                m.date_delete = r.date_efface
                m.is_visua = r.is_visua                
                self.maria_dbcontext.add_to_db(m)
    
    def do_note(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_notes_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_note_obj()               
                m.id = r.id
                m.project_id = r.projets_id
                m.title = r.intitule
                m.contain = r.contenu
                m.date_delete = r.date_efface
                m.is_visua = r.is_visua
                m.color_back = r.couleur_fd
                m.type_note = r.type_note
                m.is_rich = r.is_rich
                self.maria_dbcontext.add_to_db(m)
    
    def do_goal(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_objectifs_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_goal_obj()               
                m.id = r.id
                m.abscon = r.abscon
                m.formulation = r.formulation
                m.measurable = r.mesurable
                m.resource = r.ressources
                m.ecological = r.ecologique
                m.circumstantial = r.circonstancie
                m.realistic = r.realiste
                m.exciting = r.excitant
                m.reward = r.recompense                
                m.project_id = r.projets_id
                self.maria_dbcontext.add_to_db(m)

    def do_param(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_params_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_param_obj()               
                m.node = r.noeud
                m.key = r.cle
                m.second_key = r.souscle
                m.value = r.valeur
                self.maria_dbcontext.add_to_db(m)

    def do_project(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_projets_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_project_obj()               
                m.type_projet = r.type_projet
                m.title = r.intitule
                m.date_creation 
                m.project_id = r.projets_id
                m.place = r.lieu
                m.address = r.adresse
                m.city = r.ville
                m.zip_code = r.code_postal
                m.color = r.couleur
                m.price_projected = None if r.prix_prevu == '' else r.prix_prevu
                m.priority = 0 if r.priorite == '' else r.priorite
                m.description = r.description
                m.date_delete = r.date_efface
                m.is_done = r.is_effectue
                m.font = r.font
                m.color_visua = r.couleur_visua
                m.date_end = r.date_fin
                m.date_begin = r.date_debut
                m.price =  None if r.prix == '' else r.prix
                m.note = r.note
                m.time = r.temps
                m.counter = r.compteur
                m.date_done = r.date_effectue
                m.is_visua = r.is_visua
                m.is_synch = r.is_synch                
                self.maria_dbcontext.add_to_db(m)

    def do_reminder(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_rappels_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_reminder_obj()               
                m.id = r.id
                m.reminder = r.rappel
                m.unit_reminder = r.unite_rappel
                m.project_id = r.projets_id                
                self.maria_dbcontext.add_to_db(m)

    def do_type_category(self):
        self.trace(inspect.stack())         
        sqlite_rows = self.sqlite_dbcontext.get_types_categories_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_type_category_obj()               
                m.type_category = r.type_categorie
                m.title = r.libelle                
                self.maria_dbcontext.add_to_db(m)

    def do_type_project(self):
        self.trace(inspect.stack())
        sqlite_rows = self.sqlite_dbcontext.get_types_projets_list()        
        for r in sqlite_rows:
                m = self.maria_dbcontext.get_type_project_obj()               
                m.type_project = r.type_projet
                m.title = r.libelle                
                self.maria_dbcontext.add_to_db(m)

    def do_visuas(self):
        self.trace(inspect.stack())

    def main(self):
        self.init_main("default")
        # Connexion à la base de données SQLite
        self.sqlite_dbcontext = self.get_sqlite_db_context(self.jsprms.prms['sqlite_dbpath'])
        self.maria_dbcontext = self.get_maria_db_context()        
        
        self.do_category()
        self.do_category_object()
        self.do_contact()
        self.do_contact_project()

        self.do_decisional()
        self.do_sticker()
        self.do_arrow()
        self.do_picture()
        self.do_link()
        self.do_note()
        self.do_goal()
        self.do_param()
        self.do_project()
        self.do_reminder()
        self.do_type_category()
        self.do_type_project()
        self.do_visuas()
    

        print("Migration terminée avec succès !")