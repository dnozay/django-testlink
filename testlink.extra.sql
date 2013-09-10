# this is needed because django doesn't support multi-column primary keys (yet)
alter table user_group_assign add column `id` integer NOT NULL PRIMARY KEY;