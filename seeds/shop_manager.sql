DROP TABLE IF EXISTS "public"."items";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."items" (
    "id" SERIAL,
    "name" text,
    "unit_price" NUMERIC(10, 2), --floats with 10 digits max, and decimal place with 2 digits to the right.
    "stock_quantity" int,
    PRIMARY KEY ("id")
);

DROP TABLE IF EXISTS "public"."orders_items"; -- Join table.
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."orders_items" (
    "order_id" int4,
    "item_id" int4,
    "quantity" int,
    "unit_price" NUMERIC(10, 2),
    "total_price" NUMERIC(10, 2)
);

DROP TABLE IF EXISTS "public"."orders";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."orders" (
    "id" SERIAL,
    "customer_name" text,
    "date" date,
    "total" NUMERIC(10, 2),
    PRIMARY KEY ("id")
);

INSERT INTO "public"."items" ("name", "unit_price", "stock_quantity") VALUES
('apple', 1.00, 50), --1
('banana', 2.50, 50), --2
('orange', 2.75, 60), --3
('pear', 3.50, 40), --4
('lettuce', 2.00, 50), --5
('bread', 3.00, 60) --6
;

INSERT INTO "public"."orders" ("customer_name", "date", "total") VALUES
('First Customer', '2023-10-05', 5.50),
('John Doe', '2023-10-06', 14.50)
;

-- INSERT INTO "public"."orders_items" ("order_id", "item_id", "item_name", "quantity", "unit_price", "total_price") VALUES
-- (1, 1),
-- (1, 2),
-- (1, 4)
-- ;

-- ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("order_id") REFERENCES "public"."orders"("id");
-- ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("item_id") REFERENCES "public"."items"("id");
