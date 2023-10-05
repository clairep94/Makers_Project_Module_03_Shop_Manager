DROP TABLE IF EXISTS "public"."items";
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."items" (
    "id" SERIAL,
    "name" text,
    "stock_quantity" int,
    "unit_price" NUMERIC(10, 2), --floats with 10 digits max, and decimal place with 2 digits to the right.
    PRIMARY KEY ("id")
);

DROP TABLE IF EXISTS "public"."items_orders"; -- Join table.
-- This script only contains the table creation statements and does not fully represent the table in the database. It's still missing: indices, triggers. Do not use it as a backup.

-- Table Definition
CREATE TABLE "public"."items_orders" (
    "item_id" int4,
    "order_id" int4
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

INSERT INTO "public"."items" ("name", "stock_quantity", "unit_price") VALUES
('apple', 50, 1.00),
('banana', 50, 2.50),
('orange', 60, 2.75),
('pear', 40, 3.50),
('lettuce', 50, 2.00),
('bread', 60, 3.00)
;

INSERT INTO "public"."orders" ("customer_name", "date", "total") VALUES
('First Customer', '2023-12-31', 5.50)
;

INSERT INTO "public"."items_orders" ("item_id", "order_id") VALUES
(1, 1),
(2, 1),
(3, 1)
;

ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("order_id") REFERENCES "public"."orders"("id");
ALTER TABLE "public"."items_orders" ADD FOREIGN KEY ("item_id") REFERENCES "public"."items"("id");
