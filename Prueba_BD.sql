-- Prueba Tecnica
CREATE DATABASE my_database;
USE my_database;
-- Crear la tabla res_partner
CREATE TABLE res_partner (
    id int PRIMARY KEY auto_increment,
    name VARCHAR(255) NOT NULL
);

-- Crear la tabla product_product
CREATE TABLE product_product (
    id int PRIMARY KEY auto_increment,
    default_code VARCHAR(255) NOT NULL
);

select * from sale_order;
-- Crear la tabla sale_order
CREATE TABLE sale_order (
    id int PRIMARY KEY auto_increment,
    name VARCHAR(255) NOT NULL,
    partner_id INT NOT NULL,
    date TIMESTAMP NOT NULL,
    state VARCHAR(255) NOT NULL,
    FOREIGN KEY (partner_id) REFERENCES res_partner(id)
);

-- Crear la tabla sale_order_line
CREATE TABLE sale_order_line (
    id int PRIMARY KEY auto_increment,
    product_id INT NOT NULL,
    description VARCHAR(255),
    product_uom_qty NUMERIC NOT NULL,
    discount NUMERIC NOT NULL,
    price_unit NUMERIC NOT NULL,
    price_subtotal NUMERIC NOT NULL,
    order_id INT NOT NULL,
    state VARCHAR(255) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product_product(id),
    FOREIGN KEY (order_id) REFERENCES sale_order(id)
);

-- Crear la tabla stock_history
CREATE TABLE stock_history (
    id int PRIMARY KEY auto_increment,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    date TIMESTAMP NOT NULL,
    FOREIGN KEY (product_id) REFERENCES product_product(id)
);

CREATE USER 'IvanLeon'@'localhost' IDENTIFIED BY '1993';
GRANT ALL PRIVILEGES ON my_database.* TO 'IvanLeon'@'localhost';


select * from
