import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='your_db_name',
    user='postgres',
    password='your_pass',
    port=5432
)

cur = conn.cursor()

cur.execute("""
  CREATE TABLE customer (
    national_id INT PRIMARY KEY UNIQUE,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL,
    is_seller BOOLEAN
  );
""")

cur.execute("""
  CREATE TABLE seller (
    seller_id SERIAL PRIMARY KEY UNIQUE,
    company_name VARCHAR(255)  NULL,
    person_name VARCHAR(255)  NULL,
    shop_name VARCHAR(255)  NULL,
    FOREIGN KEY(seller_id) REFERENCES customer(national_id)
  );
""")
cur.execute("""
  CREATE TABLE estate_sell_type (
    id SERIAL PRIMARY KEY UNIQUE,
    rent VARCHAR(255)  NULL,
    sale VARCHAR(255)  NULL,
    mortgage VARCHAR(255) NULL
  );
""")

cur.execute("""
  CREATE TABLE estate_type (
    id SERIAL PRIMARY KEY UNIQUE,
    villa VARCHAR(255) NULL,
    apartment VARCHAR(255) NULL,
    garden_house VARCHAR(255) NULL
  );
""")
cur.execute("""
  CREATE TABLE Estate (
    estate_id SERIAL PRIMARY KEY UNIQUE,
    title VARCHAR(255),
    description TEXT NULL,
    location VARCHAR(255) NOT NULL,
    meterage INT NOT NULL CHECK(meterage > 0),
    n_rooms INT NOT NULL CHECK(n_rooms > 0),
    price INT DEFAULT NULL CHECK(price > 0),
    build_date DATE,
    sell_type SMALLINT,
    estate_type SMALLINT,
    sellers_id SMALLINT,
    has_parking BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (sell_type) REFERENCES estate_sell_type(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (sellers_id) REFERENCES seller(seller_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (estate_type) REFERENCES estate_type(id) ON DELETE CASCADE ON UPDATE CASCADE
  );
""")

cur.execute("""
  CREATE TABLE Buy (
    national_id INT,
    estate_id INT,
    PRIMARY KEY (national_id , estate_id),
    FOREIGN KEY (national_id) REFERENCES customer(national_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (estate_id) REFERENCES Estate(estate_id) ON DELETE CASCADE ON UPDATE CASCADE
  );
""")

cur.execute("""
  CREATE TABLE has (
    seller_id INT,
    estate_id INT,
    PRIMARY KEY (seller_id, estate_id),
    FOREIGN KEY (seller_id) REFERENCES seller(seller_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (estate_id) REFERENCES estate(estate_id) ON DELETE CASCADE ON UPDATE CASCADE
  );
""")

def create_at_least_one_not_null_trigger(table_name, column_names):
    trigger_func = f"""
    CREATE OR REPLACE FUNCTION enforce_at_least_one_not_null()
    RETURNS TRIGGER AS $$
    BEGIN
        IF {' AND '.join([f'NEW.{col} IS NULL' for col in column_names])} THEN
            RAISE EXCEPTION 'At least one of {', '.join(column_names)} must be provided.';
        END IF;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
    """
    return trigger_func

estate_type_columns = ["villa", "apartment", "garden_house"]
estate_sell_type_columns = ["rent", "sale", "mortgage"]
cur.execute(create_at_least_one_not_null_trigger("estate_type", estate_type_columns))
cur.execute(create_at_least_one_not_null_trigger("estate_sell_type", estate_sell_type_columns))

print("Triggers created successfully!")

cur.execute("""
  CREATE TABLE doc (
    doc_id SERIAL PRIMARY KEY,
    upload_date DATE,
    doc_url_path VARCHAR(255),
    estate_id INT,
    FOREIGN KEY (estate_id) REFERENCES estate(estate_id)
  );
""")

cur.execute("""
  CREATE TABLE images (
    image_id SERIAL PRIMARY KEY,
    image_url VARCHAR(255) NOT NULL
  );
""")

cur.execute("""
  CREATE TABLE estate_images (
    estate_id INT,
    image_id INT,
    PRIMARY KEY (estate_id, image_id),
    FOREIGN KEY (estate_id) REFERENCES estate(estate_id) ON DELETE CASCADE,
    FOREIGN KEY (image_id) REFERENCES images(image_id) ON DELETE CASCADE
  );
""")

conn.commit()
cur.close()
conn.close()
