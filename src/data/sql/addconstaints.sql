update project set project_id = null where project_id = 0;
update link set project_id = null where project_id = 0;
update note set project_id = null where project_id = 0;
update picture set project_id = null where project_id = 0;
update reminder set project_id = null where project_id = 0;
update sticker set project_id = null where project_id = 0;

ALTER TABLE crvomain.param ADD CONSTRAINT param_unique UNIQUE KEY (node, first_key,second_key);

ALTER TABLE project ADD CONSTRAINT project_project_FK FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE;

ALTER TABLE crvomain.project ADD CONSTRAINT project_type_project_FK FOREIGN KEY (code_type_project) REFERENCES crvomain.type_project(code);

ALTER TABLE category_object ADD CONSTRAINT category_object_category_FK FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE ON UPDATE CASCADE;

DELETE FROM category_object where not exists (select p2.id from project p2 where p2.id = category_object.project_id);

DELETE FROM category_object where not exists (select c.id from contact c where c.id = category_object.contact_id);

ALTER TABLE category_object ADD CONSTRAINT category_object_contact_FK FOREIGN KEY (contact_id) REFERENCES contact(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE category_object ADD CONSTRAINT category_object_project_FK FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE ON UPDATE CASCADE;

DELETE FROM arrow where not exists (select v.id from visua v where v.id = arrow.visua_org_id) or not exists (select v.id from visua v where v.id = arrow.visua_dest_id);

ALTER TABLE arrow ADD CONSTRAINT arrow_visua_org_FK FOREIGN KEY (visua_org_id) REFERENCES visua(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE arrow ADD CONSTRAINT arrow_visua_dest_FK FOREIGN KEY (visua_dest_id) REFERENCES visua(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE category ADD CONSTRAINT category_type_category_FK FOREIGN KEY (code_type_category) REFERENCES type_category(code);

ALTER TABLE contact_project ADD CONSTRAINT contact_project_contact_FK FOREIGN KEY (contact_id) REFERENCES contact(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE contact_project ADD CONSTRAINT contact_project_project_FK FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE decisional ADD CONSTRAINT decisional_project_FK FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE goal ADD CONSTRAINT goal_project_FK FOREIGN KEY (project_id) REFERENCES project(id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE link ADD CONSTRAINT link_project_FK FOREIGN KEY (project_id) REFERENCES project(id);

ALTER TABLE note ADD CONSTRAINT note_project_FK FOREIGN KEY (project_id) REFERENCES project(id);

ALTER TABLE picture ADD CONSTRAINT picture_project_FK FOREIGN KEY (project_id) REFERENCES project(id);

ALTER TABLE reminder ADD CONSTRAINT reminder_project_FK FOREIGN KEY (project_id) REFERENCES project(id);

ALTER TABLE sticker ADD CONSTRAINT sticker_project_FK FOREIGN KEY (project_id) REFERENCES project(id);