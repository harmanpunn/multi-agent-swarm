INSERT INTO products (name, category, price) VALUES ('Laptop', 'Electronics', 1200.00);
INSERT INTO products (name, category, price) VALUES ('Smartphone', 'Electronics', 800.00);
INSERT INTO products (name, category, price) VALUES ('Tablet', 'Electronics', 300.00);
INSERT INTO products (name, category, price) VALUES ('Wireless Mouse', 'Accessories', 25.00);
INSERT INTO products (name, category, price) VALUES ('Office Chair', 'Furniture', 150.00);
INSERT INTO products (name, category, price) VALUES ('Espresso Machine', 'Home Appliances', 400.00);


INSERT INTO customers (name, age, location, gender) VALUES ('Alice', 34, 'New York', 'Female');
INSERT INTO customers (name, age, location, gender) VALUES ('Bob', 28, 'San Francisco', 'Male');
INSERT INTO customers (name, age, location, gender) VALUES ('Carol', 40, 'Los Angeles', 'Female');
INSERT INTO customers (name, age, location, gender) VALUES ('David', 45, 'Chicago', 'Male');
INSERT INTO customers (name, age, location, gender) VALUES ('Eve', 32, 'Houston', 'Female');
INSERT INTO customers (name, age, location, gender) VALUES ('Frank', 29, 'Austin', 'Male');

INSERT INTO sales (product_id, customer_id, quantity, total_revenue, date) VALUES (1, 1, 1, 1200.00, '2024-11-01');
INSERT INTO sales (product_id, customer_id, quantity, total_revenue, date) VALUES (2, 2, 2, 1600.00, '2024-11-02'); -- Bob bought 2 Smartphones
INSERT INTO sales (product_id, customer_id, quantity, total_revenue, date) VALUES (3, 3, 1, 300.00, '2024-11-03'); -- Carol bought 1 Tablet
INSERT INTO sales (product_id, customer_id, quantity, total_revenue, date) VALUES (4, 4, 3, 75.00, '2024-11-04'); -- David bought 3 Wireless Mice
INSERT INTO sales (product_id, customer_id, quantity, total_revenue, date) VALUES (5, 5, 1, 150.00, '2024-11-05'); -- Eve bought 1 Office Chair
INSERT INTO sales (product_id, customer_id, quantity, total_revenue, date) VALUES (6, 1, 2, 800.00, '2024-11-06'); -- Alice bought 2 Espresso Machines
INSERT INTO sales (product_id, customer_id, quantity, total_revenue, date) VALUES (1, 3, 1, 1200.00, '2024-11-07'); -- Carol bought 1 Laptop
INSERT INTO sales (product_id, customer_id, quantity, total_revenue, date) VALUES (3, 2, 4, 1200.00, '2024-11-08'); -- Bob bought 4 Tablets
INSERT INTO sales (product_id, customer_id, quantity, total_revenue, date) VALUES (5, 4, 1, 150.00, '2024-11-09'); -- David bought 1 Office Chair
