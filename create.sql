-- Create script: use this to initialize the database



CREATE TABLE delegation(
	d_name			char(20),
	country			char(3) NOT NULL,
	email			char(20),
	tel				char(20),

	CONSTRAINT PK_DELEG primary key (d_name)
);

CREATE TABLE facility(
	f_name		char(20),
	adress 		char(50),
	capacity	integer,		

	CONSTRAINT PK_FACILITY primary key (f_name)
);

CREATE TABLE equipment(
	e_id 			serial,
	e_name			char(20) NOT NULL,
	description 	char(255) NOT NULL,
	owner			char(20) NOT NULL,

	CONSTRAINT PK_EQUIP primary key (e_id),
	CONSTRAINT FK_EQUIP foreign key (owner) 
		REFERENCES delegation (d_name) ON DELETE CASCADE
	
);

CREATE TABLE stock(
	f_name		char(20),
	e_id		integer,
	
	CONSTRAINT PK_STOCK primary key (f_name, e_id),
	CONSTRAINT FK_STOCK_f foreign key (f_name) 
		REFERENCES facility (f_name) ON DELETE CASCADE,
	CONSTRAINT FK_STOCK_e foreign key (e_id) 
		REFERENCES equipment (e_id) ON DELETE CASCADE
);


CREATE TABLE employee(
	CPF			char(10),
	RG			char(10) NOT NULL,
	civil_name	char(20) NOT NULL,
	work_on 	char(20) NOT NULL,
	password	char(50) NOT NULL,
	is_active	boolean DEFAULT TRUE,		

	CONSTRAINT PK_EMPLOYEE primary key (CPF),
	CONSTRAINT SK_EMPLOYEE unique (RG),
	CONSTRAINT FK_EMPLOYEE foreign key (work_on) 
		REFERENCES facility (f_name) ON DELETE SET NULL
);

CREATE TABLE employee_fluent(
	CPF			char(10),
	language	char(20),

	CONSTRAINT PK_EMPLOYEE_FLUENT primary key (CPF, language)
	CONSTRAINT FK_EMPLOYEE_FLUENT foreign key (CPF) 
		REFERENCES employee (CPF) ON DELETE CASCADE,
);

CREATE TABLE supervisor(
	CPF 	char(10),
	level	integer DEFAULT 0,

	CONSTRAINT PK_SUPERVISOR primary key (CPF),
	CONSTRAINT FK_SUPERVISOR foreign key (CPF)
		REFERENCES employee (CPF) ON DELETE CASCADE
);

CREATE TABLE supervisor_of(
	CPF_sup 	char(10),
	CPF_emp		char(10),

	CONSTRAINT PK_SUPERVISOR_OF primary key (CPF_sup, CPF_emp),
	CONSTRAINT FK_SUPERVISOR_OF_SUP foreign key (CPF_sup)
		REFERENCES supervisor (CPF) ON DELETE CASCADE,
	CONSTRAINT FK_SUPERVISOR_OF_EMP foreign key (CPF_emp)
		REFERENCES employee (CPF) ON DELETE CASCADE

);

CREATE TABLE local_of_equip(
	e_id 		integer,
	status		integer DEFAULT 0,
	local		char(20),

	CONSTRAINT PK_LOCAL_OF_EQUIP primary key (e_id),
	CONSTRAINT FK_LOCAL_OF_EQUIP_LOCAL foreign key (e_id)
		REFERENCES equipment (e_id) ON DELETE CASCADE,
	CONSTRAINT FK_LOCAL_OF_EQUIP_FACILITY foreign key (local)
		REFERENCES facility (f_name) ON DELETE RESTRICT
);

CREATE TABLE request(
	r_id		serial,
	e_id 		integer,
	r_status	integer DEFAULT 0,
	local_in	char(20) NOT NULL,
	local_out	char(20) NOT NULL,
	date_in		timestamp without time zone NOT NULL,
	date_out	timestamp without time zone NOT NULL,

	CONSTRAINT PK_REQUEST primary key (r_id),
	CONSTRAINT FK_REQ_EQUIP foreign key (e_id)
		REFERENCES equipment (e_id) ON DELETE CASCADE,
	CONSTRAINT FK_REQ_IN foreign key (local_in)
		REFERENCES facility (f_name) ON DELETE CASCADE,
	CONSTRAINT FK_REQ_OUT foreign key (local_out)
		REFERENCES facility (f_name) ON DELETE CASCADE
);

CREATE TABLE service(
	r_id		integer NOT NULL,
	s_id		serial,
	employee	char(10) NOT NULL,
	description	char(255) NOT NULL,

	CONSTRAINT PK_SERVICE primary key (s_id),
	CONSTRAINT FK_SERVICE_ORDER foreign key (r_id)
		REFERENCES request (r_id) ON DELETE CASCADE,
	CONSTRAINT FK_SERVICE_EMP foreign key (employee)
		REFERENCES employee (CPF) ON DELETE CASCADE
);
