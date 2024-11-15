from sqlalchemy import create_engine, Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    color = Column(String(50))
    type_category = Column(String(1))
    code = Column(String(5))


class CategoryObject(Base):
    __tablename__ = 'category_object'   
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey('category.id'), default=0)    
    project_id = Column(Integer, ForeignKey('project.id'), default=0)
    contact_id = Column(Integer, ForeignKey('contact.id'), default=0)
    # project = relationship('Project', back_populates='contact')
    # contact = relationship('Contact', back_populates='project')


class Contact(Base):
    __tablename__ = 'contact'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    name = Column(String(150))
    firstname = Column(String(50))
    nickname = Column(String(50))
    address = Column(Text)
    zip_code = Column(String(5))
    city = Column(String(50))
    address_work = Column(Text)
    zip_code_work = Column(String(50))
    city_work = Column(String(50))
    code_building = Column(String(50))
    title = Column(String(50))
    company = Column(String(50))
    email = Column(String(50))
    email_work = Column(String(50))
    phone = Column(String(50))
    phone_work = Column(String(50))
    phone_cel = Column(String(50))
    phone_cel_work = Column(String(50))
    phone_fax_work = Column(String(50))
    date_birth = Column(DateTime)
    date_nameday = Column(DateTime)
    status = Column(String(50))
    service = Column(String(50))
    responsable = Column(Text)
    associate = Column(Text)
    comment = Column(Text)
    site_web = Column(String(250))
    site_web_work = Column(String(50))
    schedules_work = Column(String(50))
    date_delete = Column(DateTime)
    is_visua = Column(Integer)
    is_synch = Column(Integer)


class ContactProject(Base):
    __tablename__ = 'contact_project'    
    # project_id = Column(Integer)
    # contact_id = Column(Integer, ForeignKey('contact.id'))
    project_id = Column(Integer, ForeignKey('project.id'), primary_key=True)
    contact_id = Column(Integer, ForeignKey('contact.id'), primary_key=True)
    # projet_id = Column(Integer, ForeignKey('projet.id'))
    # contact_id = Column(Integer, ForeignKey('contact.id'))
    # projet = relationship('Projet', back_populates='contact')
    # contact = relationship('Contact', back_populates='project')


class Decisional(Base):
    __tablename__ = 'decisional'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    type_decisional = Column(String(255))
    scoring = Column(Integer)
    project_id = Column(Integer)
    solution = Column(String(255))


class Sticker(Base):
    __tablename__ = 'sticker'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer)
    contain = Column(Text)
    color_back = Column(String(255))
    date_delete = Column(DateTime)
    color_write = Column(String(255))
    font = Column(String(255))


class Arrow(Base):
    __tablename__ = 'arrow'
    id = Column(Integer, primary_key=True, autoincrement=True)
    visua_org_id = Column(Integer)
    visua_dest_id = Column(Integer)
    color = Column(String(255))
    size = Column(Integer)
    y_org = Column(Integer)
    y_dest = Column(Integer)
    x_org = Column(Integer)
    x_dest = Column(Integer)


class Picture(Base):
    __tablename__ = 'picture'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer)
    filename = Column(Text)
    color_back = Column(String(255))
    date_delete = Column(DateTime)


class Link(Base):
    __tablename__ = 'link'
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer)
    title = Column(String(255))
    path = Column(String(255))
    is_ged = Column(Integer)
    date_delete = Column(DateTime)
    is_visua = Column(Integer)


class Note(Base):
    __tablename__ = 'note'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    contain = Column(Text)
    project_id = Column(Integer)
    date_delete = Column(DateTime)
    is_visua = Column(Integer)
    color_back = Column(String(255))
    type_note = Column(String(255))
    is_rich = Column(Integer)


class Goal(Base):
    __tablename__ = 'goal'
    id = Column(Integer, primary_key=True, autoincrement=True)
    abscon = Column(Text)
    formulation = Column(Text)
    measurable = Column(Text)
    resource = Column(Text)
    ecological = Column(Text)
    circumstantial = Column(Text)
    realistic = Column(Text)
    exciting = Column(Text)
    reward = Column(Text)
    project_id = Column(Integer)


class Param(Base):
    __tablename__ = 'param'
    node = Column(String(255), primary_key=True)
    key = Column(String(255), primary_key=True)
    second_key = Column(String(255), primary_key=True)
    value = Column(String(255))


class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type_projet = Column(String(1))
    title = Column(String(255))
    date_creation = Column(DateTime)
    project_id = Column(Integer)
    lieu = Column(String(100))
    address = Column(String(255))
    city = Column(String(50))
    zip_code = Column(String(5))
    color = Column(String(255))
    price_projected = Column(Float(16, 2))
    priority = Column(Integer)
    description = Column(Text)
    date_delete = Column(DateTime)
    is_done = Column(Integer)
    font = Column(String(50))
    color_visua = Column(String(255))
    date_end = Column(DateTime)
    date_begin = Column(DateTime)
    price = Column(Float(14, 2))
    note = Column(Integer)
    time = Column(String(8))
    counter = Column(Integer)
    date_done = Column(DateTime)
    is_visua = Column(Integer)
    is_synch = Column(Integer)


class Reminder(Base):
    __tablename__ = 'reminder'
    id = Column(Integer, primary_key=True, autoincrement=True)
    reminder = Column(Integer)
    unity_reminder = Column(String(10))
    project_id = Column(Integer)


class TypeCategory(Base):
    __tablename__ = 'type_category'
    type_category = Column(String(3), primary_key=True)
    title = Column(String(50))


class TypeProject(Base):
    __tablename__ = 'type_project'
    type_project = Column(String(2), primary_key=True)
    title = Column(String(50))


class Visua(Base):
    __tablename__ = 'visua'
    id = Column(Integer, primary_key=True, autoincrement=True)
    position_x = Column(Integer)
    position_y = Column(Integer)
    height = Column(Integer)
    width = Column(Integer)
    date_delete = Column(DateTime)
    project_id = Column(Integer)
    note_id = Column(Integer)
    link_id = Column(Integer)
    contact_id = Column(Integer)
    sticker_id = Column(Integer)
    picture_id = Column(Integer)
    action_id = Column(Integer)
