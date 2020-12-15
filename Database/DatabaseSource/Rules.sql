CREATE OR REPLACE RULE no_lists_insert AS ON INSERT
TO lists DO INSTEAD NOTHING;

CREATE OR REPLACE RULE no_lists_update AS ON UPDATE
TO lists DO INSTEAD NOTHING;

CREATE OR REPLACE RULE no_list_with_tasks_insert AS ON INSERT
TO list_with_tasks DO INSTEAD NOTHING;

CREATE OR REPLACE RULE no_list_with_tasks_update AS ON UPDATE
TO list_with_tasks DO INSTEAD NOTHING;