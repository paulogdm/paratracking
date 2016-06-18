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
--stock
INSERT INTO stock (f_name, e_id)
	VALUES ('airport', 1),('airport', 2);
	
INSERT INTO stock (f_name, e_id)
	VALUES ('delivery hub', 3),('delivery hub', 4);

-- employee
INSERT INTO employee (CPF, RG, civil_name, work_on, password)
	VALUES 	('100', '100', 'Rogerio Manjaro', 'airport', '123'),
			('200', '200', 'Cibeli Arch', 'airport', '123'),
			('300', '300', 'Pricila Gentoo', 'central', '123'),
			('400', '400', 'Yan Deepin', 'central', '123'),
			('500', '500', 'Juan Porteus', 'delivery hub', '123'),
			('600', '600', 'Maria Antergos', 'delivery hub', '123'),
			('700', '700', 'Pedro Baruwa', 'distribution center', '123'),
			('800', '800', 'Amanda Salix', 'distribution center', '123'),
			('900', '900', 'Felipe Elem', 'distribution center', '123'),
			('10', '10', 'Mr G', 'central', '123'),
			('1000', '1000', 'Vini Tails', 'central', '123');

-- supervisor
INSERT INTO supervisor (CPF, level)
	VALUES 	('10', 4),
			('900', 3),
			('600', 3),
			('100', 2);

-- supervisor_of
INSERT INTO supervisor_of (CPF_sup, CPF_emp)
	VALUES	('10', '400'),
			('10', '300'),
			('10', '1000'),
			('900', '800'),
			('900', '700'),
			('600', '500'),
			('100', '200');

--local_of_equip
INSERT INTO local_of_equip (e_id, local)
	VALUES (1, 'airport'), (2, 'central'), 
	(3, 'distribution center'), (4, 'delivery hub');



--request
INSERT INTO request (e_id, local_in, local_out, date_in, date_out)
	VALUES (1, 'airport', 'central', TIMESTAMP '2016-10-22 08:00:00', TIMESTAMP '2016-10-23 08:00:00'),
	(1, 'central', 'delivery hub', TIMESTAMP '2016-10-23 08:00:00', TIMESTAMP '2016-10-23 10:00:00'),
	(2, 'central', 'distribution center', TIMESTAMP '2016-10-20 10:00:00', TIMESTAMP '2016-10-20 11:00:00'),
	(2, 'distribution center', 'delivery hub', TIMESTAMP '2016-10-21 08:00:00', TIMESTAMP '2016-10-22 10:00:00');


--service 
INSERT INTO service (r_id, employee, description)
	VALUES (1, '200', 'Coloquei o equipamento no drone para entrega.'),
	(1, '300', 'O pacote foi verificado e esta tudo ok.'),
	(1, '300', 'Equipamento escaneado e pronto para despacho.'),
	(2, '300', 'Encaminhado para entregador.'),
	(2, '500', 'Produto recontado e duas unidades estão faltando.'),
	(2, '500', 'Entrei em contato com proprietarios. Tudo ok.');


--employee_fluent
INSERT INTO employee_fluent (CPF, language) VALUES ('10', 'ITA'), ('10', 'EN-US'), 
('10', 'PT-BR'), ('10', 'ESP');




