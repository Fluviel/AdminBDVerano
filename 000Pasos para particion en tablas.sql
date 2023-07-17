--Ingresar a postgres--
sudo -u postgres psql
--Crear base de datos storeee--
CREATE DATABASE storeee;
--Dirigirnos a la base de datos creada--
\c storeee
--Crear la BD de product con particion de rango--
CREATE TABLE product (
    id SERIAL,
    product_name TEXT,
    price DECIMAL,
    PRIMARY KEY (id, price)
)
PARTITION BY RANGE (price);
-- Crear las particiones y establecer los rangos--
CREATE TABLE product_partition_1 PARTITION OF product
    FOR VALUES FROM (1.00) TO (3000.00);

CREATE TABLE product_partition_2 PARTITION OF product
    FOR VALUES FROM (3000.01) TO (6000.00);

CREATE TABLE product_partition_3 PARTITION OF product
    FOR VALUES FROM (6000.01) TO (10000.00);

-- Para la partición product_partition_1-2-3
ALTER TABLE product_partition_1
ADD CONSTRAINT product_partition_1_price_check
CHECK (price >= 1.00 AND price <= 3000.00);


ALTER TABLE product_partition_2
ADD CONSTRAINT product_partition_2_price_check
CHECK (price >= 3000.01 AND price <= 6000.00);


ALTER TABLE product_partition_3
ADD CONSTRAINT product_partition_3_price_check
CHECK (price >= 6000.01 AND price <= 10000.00);

--Importar los registros a nuestra tabla--
\i /var/lib/postgresql/product.sql
--Listamos las tablas creadas--
\dt    
--visualizamos todos los registros en la tabla product--
select * from product;
--Con esta linea consultamos las particiones--
select * from product_partition_1;
select * from product_partition_2;
select * from product_partition_3;
------------------------------------------------------------------

--Crear la tabla client--
CREATE TABLE client (
    id_client SERIAL,
    first_name TEXT,
    last_name TEXT,
    adreess TEXT,
    country TEXT,
    email TEXT,
    cellphone TEXT,
    telephone TEXT,
    job_title TEXT,
    gender TEXT,
    college TEXT,
    PRIMARY KEY (id_client, gender)
) PARTITION BY LIST (gender);


--Crear las particiones con su rango--
CREATE TABLE client_partition_female PARTITION OF client
    FOR VALUES IN ('Female', 'female', 'FEMALE');

CREATE TABLE client_partition_male PARTITION OF client
    FOR VALUES IN ('Male', 'male', 'MALE');

ALTER TABLE client_partition_female ADD CONSTRAINT partition_female_check CHECK (gender IN ('Female', 'female', 'FEMALE'));

ALTER TABLE client_partition_male ADD CONSTRAINT partition_male_check CHECK (gender IN ('Male', 'male', 'MALE'));

--Importar los registros a nuestra tabla--
\i /var/lib/postgresql/client.sql
--Listamos las tablas creadas--
\dt    
--visualizamos todos los registros en la tabla product--
select * from client;
--Con esta linea consultamos las particiones--
select * from client_partition_female;
select * from client_partition_male;

