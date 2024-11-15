from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, autoincrement=True)
    intitule = Column(String(255))
    couleur = Column(String(50))
    type_categorie = Column(String(1))
    code = Column(String(5))


class CategoriesObjets(Base):
    __tablename__ = 'categories_objets'    
    categories_id = Column(Integer, ForeignKey('categories.id'))
    projets_id = Column(Integer, ForeignKey('projets.id'), primary_key=True)
    contacts_id = Column(Integer, ForeignKey('contacts.id'), primary_key=True)


class Contacts(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pseudo = Column(String(50))
    nom = Column(String(150))
    prenom = Column(String(50))
    surnom = Column(String(50))
    adresse = Column(Text)
    code_postal = Column(String(5))
    ville = Column(String(50))
    adresse_trav = Column(Text)
    code_postal_trav = Column(String(50))
    ville_trav = Column(String(50))
    code_immeuble = Column(String(50))
    titre = Column(String(50))
    societe = Column(String(50))
    email = Column(String(50))
    email_trav = Column(String(50))
    tel = Column(String(50))
    tel_trav = Column(String(50))
    tel_portable = Column(String(50))
    tel_portable_trav = Column(String(50))
    tel_fax_trav = Column(String(50))
    date_naissance = Column(DateTime)
    date_fete = Column(DateTime)
    statut = Column(String(50))
    service = Column(String(50))
    responsables = Column(Text)
    collaborateurs = Column(Text)
    commentaires = Column(Text)
    site_web = Column(String(250))
    site_web_trav = Column(String(50))
    horaires_trav = Column(String(50))
    date_efface = Column(DateTime)
    is_visua = Column(Integer, default=0)
    is_synch = Column(Integer, default=0)


class ContactsProjets(Base):
    __tablename__ = 'contacts_projets'

    projets_id = Column(Integer, ForeignKey('projets.id'), primary_key=True)
    contacts_id = Column(Integer, ForeignKey('contacts.id'), primary_key=True)


class Decisionnel(Base):
    __tablename__ = 'decisionnel'
    id = Column(Integer, primary_key=True, autoincrement=True)
    intitule = Column(String)
    type_decisionnel = Column(String)
    notation = Column(Integer)
    projets_id = Column(Integer, ForeignKey('projets.id'))
    solution = Column(String)


class Etiquettes(Base):
    __tablename__ = 'etiquettes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    projets_id = Column(Integer, ForeignKey('projets.id'))
    contenu = Column(Text)
    couleur_fd = Column(String)
    date_efface = Column(DateTime)
    couleur_ec = Column(String)
    font = Column(String)


class Fleches(Base):
    __tablename__ = 'fleches'
    id = Column(Integer, primary_key=True, autoincrement=True)
    visuas_org_id = Column(Integer, ForeignKey('visuas.id'))
    visuas_dest_id = Column(Integer, ForeignKey('visuas.id'))
    couleur = Column(String)
    size = Column(Integer)
    y_org = Column(Integer)
    y_dest = Column(Integer)
    x_org = Column(Integer)
    x_dest = Column(Integer)


class Images(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, autoincrement=True)
    projets_id = Column(Integer, ForeignKey('projets.id'))
    nom_fichier = Column(Text)
    couleur_fd = Column(String)
    date_efface = Column(DateTime)


class Liens(Base):
    __tablename__ = 'liens'
    id = Column(Integer, primary_key=True, autoincrement=True)
    projets_id = Column(Integer, ForeignKey('projets.id'))
    titre = Column(String)
    chemin = Column(String)
    is_ged = Column(Integer, default=0)
    date_efface = Column(DateTime)
    is_visua = Column(Integer, default=0)


class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    intitule = Column(String)
    contenu = Column(Text)
    projets_id = Column(Integer, ForeignKey('projets.id'))
    date_efface = Column(DateTime)
    is_visua = Column(Integer, default=0)
    couleur_fd = Column(String)
    type_note = Column(String, default='N')
    is_rich = Column(Integer, default=0)


class Objectifs(Base):
    __tablename__ = 'objectifs'
    id = Column(Integer, primary_key=True, autoincrement=True)
    abscon = Column(Text)
    formulation = Column(Text)
    mesurable = Column(Text)
    ressources = Column(Text)
    ecologique = Column(Text)
    circonstancie = Column(Text)
    realiste = Column(Text)
    excitant = Column(Text)
    recompense = Column(Text)
    projets_id = Column(Integer, ForeignKey('projets.id'))


class Params(Base):
    __tablename__ = 'params'
    noeud = Column(String, primary_key=True)
    cle = Column(String)
    souscle = Column(String)
    valeur = Column(String)


class Projets(Base):
    __tablename__ = 'projets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type_projet = Column(String(1))
    intitule = Column(String, nullable=False)
    date_creation = Column(DateTime)
    projets_id = Column(Integer, ForeignKey('projets.id'))
    lieu = Column(String(100))
    adresse = Column(String)
    ville = Column(String(50))
    code_postal = Column(String(5))
    couleur = Column(String)
    prix_prevu = Column(Float(16, 2))
    priorite = Column(Integer)
    description = Column(Text)
    date_efface = Column(DateTime)
    is_effectue = Column(Integer, default=0)
    font = Column(String(50))
    couleur_visua = Column(String)
    date_fin = Column(DateTime)
    date_debut = Column(DateTime)
    prix = Column(Float(14, 2))
    note = Column(Integer)
    temps = Column(String(8))
    compteur = Column(Integer)
    date_effectue = Column(DateTime)
    is_visua = Column(Integer, default=0)
    is_synch = Column(Integer, default=0)


class Rappels(Base):
    __tablename__ = 'rappels'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rappel = Column(Integer)
    unite_rappel = Column(String(10))
    projets_id = Column(Integer, ForeignKey('projets.id'))


class TypesCategories(Base):
    __tablename__ = 'types_categories'
    type_categorie = Column(String(3), primary_key=True)
    libelle = Column(String(50))


class TypesProjets(Base):
    __tablename__ = 'types_projets'
    type_projet = Column(String(2), primary_key=True)
    libelle = Column(String(50))


class Visuas(Base):
    __tablename__ = 'visuas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    position_x = Column(Integer)
    position_y = Column(Integer)
    hauteur = Column(Integer)
    largeur = Column(Integer)
    date_efface = Column(DateTime)
    projets_id = Column(Integer, ForeignKey('projets.id'))
    notes_id = Column(Integer, ForeignKey('notes.id'))
    liens_id = Column(Integer, ForeignKey('liens.id'))
    contacts_id = Column(Integer, ForeignKey('contacts.id'))
    etiquettes_id = Column(Integer, ForeignKey('etiquettes.id'))
    images_id = Column(Integer, ForeignKey('images.id'))
    actions_id = Column
