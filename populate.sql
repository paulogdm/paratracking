-- Populate script: use this to insert some data


-- delegation

INSERT INTO delegation (d_name, country, email)
	VALUES ('BRA_volley', 'BRA', 'volley@brasil.org');
	
INSERT INTO delegation (d_name, country, email, tel)
	VALUES ('BRA_waterpolo', 'BRA', 'wp@brasil.org', '911');

INSERT INTO delegation (d_name, country, email)
	VALUES ('USA_volley', 'USA', 'volley@murika.org');
	
INSERT INTO delegation (d_name, country, email)
	VALUES ('CAN_waterpolo', 'CAN', 'wp@sorry.org');
	
INSERT INTO delegation (d_name, country, email)
	VALUES ('ITA_waterpolo', 'ITA', 'wp@ita.org');


-- facility

INSERT INTO facility (f_name, adress, capacity)
	VALUES ('central', 'Rua Itapoca 23', 100);

INSERT INTO facility (f_name, adress)
	VALUES ('airport', 'Airport of Galeao');

INSERT INTO facility (f_name, capacity)
	VALUES ('distribution center', 500);

INSERT INTO facility (f_name, capacity)
	VALUES ('delivery hub', 50);


-- equipment
INSERT INTO equipment (e_name, description, owner)
	VALUES ('Mikasa Balls', '10 Mikasa Balls WP3', 'CAN_waterpolo');

INSERT INTO equipment (e_name, description, owner)
	VALUES ('Caps', '20 Main Caps + 2 keeper', 'ITA_waterpolo');

INSERT INTO equipment (e_name, description, owner)
	VALUES ('Mikasa Balls', '2 Mikasa Balls', 'BRA_waterpolo');

INSERT INTO equipment (e_name, description, owner)
	VALUES ('Gatorade', '200 Garrafas', 'BRA_volley');

----------------
-- checkpoint --
----------------

-- employee
INSERT INTO equipment (e_name, description, owner)

