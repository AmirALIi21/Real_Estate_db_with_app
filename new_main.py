import tkinter as tk
from tkinter import messagebox
import psycopg2

DB_PARAMS = {
    'host': 'localhost',
    'dbname': 'real_estate_v01',
    'user': 'postgres',
    'password': '13801380',
    'port': 5432
}

def connect_db():
    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    return conn

def update_customer():
    def get_customer_data(national_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM customer WHERE national_id = %s", (national_id,))
        customer = cur.fetchone()
        cur.close()
        conn.close()
        return customer

    def update_customer_fields(national_id):
        customer = get_customer_data(national_id)
        if customer:
            tk.Label(new_window, text="Name:").grid(row=2, column=0)
            entry_name = tk.Entry(new_window, insertwidth=100)
            entry_name.insert(0, customer[1])
            entry_name.grid(row=2, column=1)

            tk.Label(new_window, text="Email:").grid(row=3, column=0)
            entry_email = tk.Entry(new_window, insertwidth=100)
            entry_email.insert(0, customer[2])
            entry_email.grid(row=3, column=1)

            tk.Label(new_window, text="Location:").grid(row=4, column=0)
            entry_location = tk.Entry(new_window, insertwidth=100)
            entry_location.insert(0, customer[3])
            entry_location.grid(row=4, column=1)

            tk.Label(new_window, text="Phone Number:").grid(row=5, column=0)
            entry_phone_number = tk.Entry(new_window, insertwidth=100)
            entry_phone_number.insert(0, customer[4])
            entry_phone_number.grid(row=5, column=1)

       
            tk.Label(new_window, text="Is Seller:").grid(row=6, column=0)
            check_is_seller = tk.BooleanVar()
            check_is_seller.set(customer[5])  
            tk.Checkbutton(new_window, text="Yes", variable=check_is_seller, command=lambda: update_seller_info(check_is_seller.get())).grid(row=6, column=1)

            tk.Label(new_window, text="Seller Type:").grid(row=7, column=0)
            seller_type_var = tk.StringVar()
            seller_type_menu = tk.OptionMenu(new_window, seller_type_var, "Company", "Person", "Shop")
            seller_type_menu.grid(row=7, column=1)

           
            if customer[5]:
                seller_type_var.set(get_customer_data(national_id)[6])
                update_seller_info(True) 

            tk.Label(new_window, text="Company Name:").grid(row=8, column=0)
            entry_company_name = tk.Entry(new_window, insertwidth=100)
            if customer[5] and get_customer_data(national_id)[6] == "Company":
                entry_company_name.insert(0, get_customer_data(national_id)[7])
            entry_company_name.grid(row=8, column=1)

            tk.Label(new_window, text="Person Name:").grid(row=9, column=0)
            entry_person_name = tk.Entry(new_window, insertwidth=100)
            if customer[5] and get_customer_data(national_id)[6] == "Person":
                entry_person_name.insert(0, get_customer_data(national_id)[8])
            entry_person_name.grid(row=9, column=1)

            tk.Label(new_window, text="Shop Name:").grid(row=10, column=0)
            entry_shop_name = tk.Entry(new_window, insertwidth=100)
            if customer[5] and get_customer_data(national_id)[6] == "Shop":
                entry_shop_name.insert(0, get_customer_data(national_id)[9])
            entry_shop_name.grid(row=10, column=1)

            def submit_update_customer():
        
                national_id = entry_national_id.get()
                name = entry_name.get()
                email = entry_email.get()
                location = entry_location.get()
                phone_number = entry_phone_number.get()
                is_seller = check_is_seller.get()

                conn = connect_db()
                cur = conn.cursor()
                cur.execute("""
                UPDATE customer
                SET name = %s, email = %s, location = %s, phone_number = %s, is_seller = %s
                WHERE national_id = %s
                    """, (name, email, location, phone_number, is_seller, national_id))
                conn.commit()
                cur.close()
                conn.close()
                messagebox.showinfo("Success", "Customer information updated successfully.")

            def update_seller_info(is_seller):
                if is_seller:
                    seller_type_menu.grid()
                    entry_company_name.grid()
                    entry_person_name.grid()
                    entry_shop_name.grid()
                else:
                    seller_type_menu.grid_remove()
                    entry_company_name.grid_remove()
                    entry_person_name.grid_remove()
                    entry_shop_name.grid_remove()
            tk.Button(new_window, text="Submit Update", command=submit_update_customer).grid(row=11, columnspan=2)
        else:
            messagebox.showerror("Error", "Customer not found.")

   



    new_window = tk.Toplevel(root)
    new_window.title("Update Customer")

    # Search for customer by national ID
    tk.Label(new_window, text="National ID:").grid(row=0, column=0)
    entry_national_id = tk.Entry(new_window)
    entry_national_id.grid(row=0, column=1)

    tk.Button(new_window, text="Search Customer", command=lambda: update_customer_fields(entry_national_id.get())).grid(row=1, columnspan=2)


def update_estate():
    def get_estate_data(estate_id):
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM estate WHERE estate_id = %s", (estate_id,))
        estate = cur.fetchone()
        cur.close()
        conn.close()
        return estate

    def update_estate_fields(estate_id):
        estate = get_estate_data(estate_id)
        if estate:
            tk.Label(new_window, text="Title:").grid(row=2, column=0)
            entry_title = tk.Entry(new_window, insertwidth=100)
            entry_title.insert(0, estate[1])
            entry_title.grid(row=2, column=1)

            tk.Label(new_window, text="Description:").grid(row=3, column=0)
            entry_description = tk.Entry(new_window, insertwidth=100)
            entry_description.insert(0, estate[2])
            entry_description.grid(row=3, column=1)

            tk.Label(new_window, text="Location:").grid(row=4, column=0)
            entry_location = tk.Entry(new_window, insertwidth=100)
            entry_location.insert(0, estate[3])
            entry_location.grid(row=4, column=1)

            tk.Label(new_window, text="Meterage:").grid(row=5, column=0)
            entry_meterage = tk.Entry(new_window, insertwidth=100)
            entry_meterage.insert(0, estate[4])
            entry_meterage.grid(row=5, column=1)

            tk.Label(new_window, text="Number of Rooms:").grid(row=6, column=0)
            entry_n_rooms = tk.Entry(new_window, insertwidth=100)
            entry_n_rooms.insert(0, estate[5])
            entry_n_rooms.grid(row=6, column=1)

            tk.Label(new_window, text="Price:").grid(row=7, column=0)
            entry_price = tk.Entry(new_window, insertwidth=100)
            entry_price.insert(0, estate[6])
            entry_price.grid(row=7, column=1)

            tk.Label(new_window, text="Build Date:").grid(row=8, column=0)
            entry_build_date = tk.Entry(new_window, insertwidth=100)
            entry_build_date.insert(0, estate[7])
            entry_build_date.grid(row=8, column=1)

            tk.Label(new_window, text="Sell Type:").grid(row=9, column=0)
            entry_sell_type = tk.Entry(new_window, insertwidth=100)
            entry_sell_type.insert(0, estate[8])
            entry_sell_type.grid(row=9, column=1)

            tk.Label(new_window, text="Estate Type:").grid(row=10, column=0)
            entry_estate_type = tk.Entry(new_window, insertwidth=100)
            entry_estate_type.insert(0, estate[9])
            entry_estate_type.grid(row=10, column=1)

            tk.Label(new_window, text="Has Parking:").grid(row=11, column=0)
            var_has_parking = tk.BooleanVar()
            var_has_parking.set(estate[11])
            tk.Checkbutton(new_window, text="Yes", variable=var_has_parking).grid(row=11, column=1)

            def submit_update_estate():
                title = entry_title.get()
                description = entry_description.get()
                location = entry_location.get()
                meterage = entry_meterage.get()
                n_rooms = entry_n_rooms.get()
                price = entry_price.get()
                build_date = entry_build_date.get()
                sell_type = entry_sell_type.get()
                estate_type = entry_estate_type.get()
                has_parking = var_has_parking.get()

                conn = connect_db()
                cur = conn.cursor()
                cur.execute("""
                    UPDATE estate
                    SET title = %s, description = %s, location = %s, meterage = %s, n_rooms = %s, 
                        price = %s, build_date = %s, sell_type = %s, estate_type = %s, has_parking = %s
                    WHERE estate_id = %s
                """, (title, description, location, meterage, n_rooms, price, build_date, sell_type, estate_type, has_parking, estate_id))
                conn.commit()
                cur.close()
                conn.close()
                messagebox.showinfo("Success", "Estate information updated successfully.")

            tk.Button(new_window, text="Submit Update", command=submit_update_estate).grid(row=12, columnspan=2)
        else:
            messagebox.showerror("Error", "Estate not found.")

    new_window = tk.Toplevel(root)
    new_window.title("Update Estate")

    tk.Label(new_window, text="Estate ID:").grid(row=0, column=0)
    entry_estate_id = tk.Entry(new_window)
    entry_estate_id.grid(row=0, column=1)

    tk.Button(new_window, text="Fetch Estate", command=lambda: update_estate_fields(entry_estate_id.get())).grid(row=1, columnspan=2)


def insert_customer():
    def toggle_seller_fields():
        if check_is_seller.get():
            seller_type_menu.grid()
        else:
            seller_type_menu.grid_remove()
            entry_company_name.grid_remove()
            entry_person_name.grid_remove()
            entry_shop_name.grid_remove()

    def show_seller_fields(*args):
        selected_type = seller_type_var.get()
        if selected_type == 'Company':
            entry_company_name.grid()
            entry_person_name.grid_remove()
            entry_shop_name.grid_remove()
        elif selected_type == 'Person':
            entry_company_name.grid_remove()
            entry_person_name.grid()
            entry_shop_name.grid_remove()
        elif selected_type == 'Shop':
            entry_company_name.grid_remove()
            entry_person_name.grid_remove()
            entry_shop_name.grid()

    new_window = tk.Toplevel(root)
    new_window.title("Insert Customer")

    tk.Label(new_window, text="National ID:").grid(row=0, column=0)
    entry_national_id = tk.Entry(new_window)
    entry_national_id.grid(row=0, column=1)

    tk.Label(new_window, text="Name:").grid(row=1, column=0)
    entry_name = tk.Entry(new_window)
    entry_name.grid(row=1, column=1)

    tk.Label(new_window, text="Email:").grid(row=2, column=0)
    entry_email = tk.Entry(new_window)
    entry_email.grid(row=2, column=1)

    tk.Label(new_window, text="Location:").grid(row=3, column=0)
    entry_location = tk.Entry(new_window)
    entry_location.grid(row=3, column=1)

    tk.Label(new_window, text="Phone Number:").grid(row=4, column=0)
    entry_phone_number = tk.Entry(new_window)
    entry_phone_number.grid(row=4, column=1)

    tk.Label(new_window, text="Is Seller:").grid(row=5, column=0)
    check_is_seller = tk.BooleanVar()
    check_is_seller.set(False)
    tk.Checkbutton(new_window, text="Yes", variable=check_is_seller, command=toggle_seller_fields).grid(row=5, column=1)

    tk.Label(new_window, text="Seller Type:").grid(row=6, column=0)
    seller_type_var = tk.StringVar()
    seller_type_menu = tk.OptionMenu(new_window, seller_type_var, "Company", "Person", "Shop")
    seller_type_menu.grid(row=6, column=1)
    seller_type_menu.grid_remove()  

    tk.Label(new_window, text="Company Name:").grid(row=7, column=0)
    entry_company_name = tk.Entry(new_window)
    entry_company_name.grid(row=7, column=1)
    entry_company_name.grid_remove()

    tk.Label(new_window, text="Person Name:").grid(row=8, column=0)
    entry_person_name = tk.Entry(new_window)
    entry_person_name.grid(row=8, column=1)
    entry_person_name.grid_remove()

    tk.Label(new_window, text="Shop Name:").grid(row=9, column=0)
    entry_shop_name = tk.Entry(new_window)
    entry_shop_name.grid(row=9, column=1)
    entry_shop_name.grid_remove()

    seller_type_var.trace('w', show_seller_fields)

    def submit_insert_customer():
        national_id = entry_national_id.get()
        name = entry_name.get()
        email = entry_email.get()
        location = entry_location.get()
        phone_number = entry_phone_number.get()
        is_seller = check_is_seller.get()

        if not national_id or not name or not email or not location or not phone_number:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        conn = connect_db()
        cur = conn.cursor()

        try:
            cur.execute("""
                INSERT INTO customer (national_id, name, email, location, phone_number, is_seller)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (national_id, name, email, location, phone_number, is_seller))

            
            if is_seller:
                seller_type = seller_type_var.get()
                company_name = entry_company_name.get() if seller_type == 'Company' else None
                person_name = entry_person_name.get() if seller_type == 'Person' else None
                shop_name = entry_shop_name.get() if seller_type == 'Shop' else None

                cur.execute("""
                    INSERT INTO seller (seller_id, company_name, person_name, shop_name)
                    VALUES (%s, %s, %s, %s)
                """, (national_id, company_name, person_name, shop_name))

            conn.commit()
            messagebox.showinfo("Success", "Customer inserted successfully.")

        except psycopg2.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")

        finally:
            cur.close()
            conn.close()

    tk.Button(new_window, text="Submit", command=submit_insert_customer).grid(row=10, columnspan=2)

def insert_estate():
    def submit_estate():
        estate_id = entry_estate_id.get()
        title = entry_title.get()
        description = entry_description.get()
        location = entry_location.get()
        meterage = entry_meterage.get()
        n_rooms = entry_n_rooms.get()
        price = entry_price.get()
        build_date = entry_build_date.get()
        sell_type = entry_sell_type.get()
        estate_type = entry_estate_type.get()
        sellers_id = entry_sellers_id.get()
        has_parking = var_has_parking.get()

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""INSERT INTO Estate (estate_id, title, description, location, meterage, N_rooms, price, build_date, sell_type, estate_type, sellers_id, has_parking)
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)""",
                    (estate_id, title, description, location, meterage, n_rooms, price, build_date, sell_type, estate_type,sellers_id, has_parking))
        conn.commit()
        cur.close()
        conn.close()
        messagebox.showinfo("Success", "Estate inserted successfully")

    new_window = tk.Toplevel(root)
    new_window.title("Insert Estate")

    tk.Label(new_window, text="Estate ID:").grid(row=0, column=0)
    entry_estate_id = tk.Entry(new_window)
    entry_estate_id.grid(row=0, column=1)

    tk.Label(new_window, text="Title:").grid(row=1, column=0)
    entry_title = tk.Entry(new_window)
    entry_title.grid(row=1, column=1)

    tk.Label(new_window, text="Description:").grid(row=2, column=0)
    entry_description = tk.Entry(new_window)
    entry_description.grid(row=2, column=1)

    tk.Label(new_window, text="Location:").grid(row=3, column=0)
    entry_location = tk.Entry(new_window)
    entry_location.grid(row=3, column=1)

    tk.Label(new_window, text="Meterage:").grid(row=4, column=0)
    entry_meterage = tk.Entry(new_window)
    entry_meterage.grid(row=4, column=1)

    tk.Label(new_window, text="Number of Rooms:").grid(row=5, column=0)
    entry_n_rooms = tk.Entry(new_window)
    entry_n_rooms.grid(row=5, column=1)

    tk.Label(new_window, text="Price:").grid(row=6, column=0)
    entry_price = tk.Entry(new_window)
    entry_price.grid(row=6, column=1)

    tk.Label(new_window, text="Build Date:").grid(row=7, column=0)
    entry_build_date = tk.Entry(new_window)
    entry_build_date.grid(row=7, column=1)

    tk.Label(new_window, text="Sell Type:").grid(row=8, column=0)
    entry_sell_type = tk.Entry(new_window)
    entry_sell_type.grid(row=8, column=1)

    tk.Label(new_window, text="Estate Type:").grid(row=9, column=0)
    entry_estate_type = tk.Entry(new_window)
    entry_estate_type.grid(row=9, column=1)

    tk.Label(new_window, text="Seller ID:").grid(row=10, column=0) 
    entry_sellers_id = tk.Entry(new_window)  
    entry_sellers_id.grid(row=10, column=1)

    var_has_parking = tk.BooleanVar()
    tk.Checkbutton(new_window, text="Has Parking?", variable=var_has_parking).grid(row=11, columnspan=2)

    tk.Button(new_window, text="Submit", command=submit_estate).grid(row=12, columnspan=2)

'''
def insert_into_has_table(seller_id, estate_id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
         INSERT INTO has (seller_id, estate_id)
         VALUES (%s, %s);
        """, (seller_id, estate_id))
        conn.commit()
        messagebox.showinfo("Success", "Seller associated with Estate successfully.")
    except psycopg2.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")
    finally:
        cur.close()
        conn.close()
'''

def associate():
    def submit_association():
        try:
            estate_id = int(estate_var.get().split(' - ')[0])
            seller_id = int(seller_var.get().split(' - ')[0])

            conn = connect_db()
            cur = conn.cursor()
            cur.execute("INSERT INTO has (estate_id, seller_id) VALUES (%s, %s)", (estate_id, seller_id))
            conn.commit()
            cur.close()
            conn.close()
            messagebox.showinfo("Success", "Association created successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create association: {e}")

    new_window = tk.Toplevel(root)
    new_window.title("Associate Estate and Seller")

    tk.Label(new_window, text="Select Estate:").grid(row=0, column=0)
    tk.Label(new_window, text="Select Seller:").grid(row=1, column=0)

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT estate_id, title , location FROM estate")
    estates = cur.fetchall()
    cur.execute("SELECT national_id, name FROM customer where national_id IN (SELECT seller_id FROM seller)")
    sellers = cur.fetchall()
    cur.close()
    conn.close()

    estate_options = [f"{estate[0]} - {estate[1]} - {estate[2]}" for estate in estates]
    estate_var = tk.StringVar(new_window)
    estate_menu = tk.OptionMenu(new_window, estate_var, *estate_options)
    estate_menu.grid(row=0, column=1)

    seller_options = [f"{seller[0]} - {seller[1] or 'None'}" for seller in sellers]
    seller_var = tk.StringVar(new_window)
    seller_menu = tk.OptionMenu(new_window, seller_var, *seller_options)
    seller_menu.grid(row=1, column=1)

    tk.Button(new_window, text="Submit", command=submit_association).grid(row=2, columnspan=2)

def delete_customer():
    def submit_delete_customer():
        national_id = entry_national_id.get()
        

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM seller WHERE seller_id = %s", (national_id,))
        cur.execute("DELETE FROM customer WHERE national_id = %s", (national_id,))
        cur.execute("DELETE FROM Estate WHERE sellers_id = %s", (national_id,))
        conn.commit()
        cur.close()
        conn.close()
        messagebox.showinfo("Success", "Customer or seller deleted successfully")

    new_window = tk.Toplevel(root)
    new_window.title("Delete Customer")

    tk.Label(new_window, text="National ID:").grid(row=0, column=0)
    entry_national_id = tk.Entry(new_window)
    entry_national_id.grid(row=0, column=1)

    tk.Button(new_window, text="Submit", command=submit_delete_customer).grid(row=1, columnspan=2)

def delete_estate():
    def submit_delete_estate():
        estate_id = entry_estate_id.get()

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM Estate WHERE estate_id = %s", (estate_id,))
        conn.commit()
        cur.close()
        conn.close()
        messagebox.showinfo("Success", "Estate deleted successfully")

    new_window = tk.Toplevel(root)
    new_window.title("Delete Estate")

    tk.Label(new_window, text="Estate ID:").grid(row=0, column=0)
    entry_estate_id = tk.Entry(new_window)
    entry_estate_id.grid(row=0, column=1)

    tk.Button(new_window, text="Submit", command=submit_delete_estate).grid(row=1, columnspan=2)

def search_estates():
    def submit_search_estates():
        location = entry_location.get()
        meterage = entry_meterage.get()
        n_rooms = entry_n_rooms.get()
        price = entry_price.get()

        query = "SELECT * FROM Estate WHERE 1=1"
        params = []

        if location:
            query += " AND location = %s"
            params.append(location)
        if meterage:
            query += " AND meterage = %s"
            params.append(meterage)
        if n_rooms:
            query += " AND N_rooms = %s"
            params.append(n_rooms)
        if price:
            query += " AND price = %s"
            params.append(price)

        conn = connect_db()
        cur = conn.cursor()
        cur.execute(query, tuple(params))
        estates = cur.fetchall()
        for estate in estates:
            print(estate)

        cur.close()
        conn.close()

    new_window = tk.Toplevel(root)
    new_window.title("Search for Estates")

    tk.Label(new_window, text="Location:").grid(row=0, column=0)
    entry_location = tk.Entry(new_window)
    entry_location.grid(row=0, column=1)

    tk.Label(new_window, text="Meterage:").grid(row=1, column=0)
    entry_meterage = tk.Entry(new_window)
    entry_meterage.grid(row=1, column=1)

    tk.Label(new_window, text="Number of Rooms:").grid(row=2, column=0)
    entry_n_rooms = tk.Entry(new_window)
    entry_n_rooms.grid(row=2, column=1)

    tk.Label(new_window, text="Price:").grid(row=3, column=0)
    entry_price = tk.Entry(new_window)
    entry_price.grid(row=3, column=1)

    tk.Button(new_window, text="Search", command=submit_search_estates).grid(row=4, columnspan=2)

def search_customers():
    def submit_search_customers():
        national_id = entry_national_id.get()
        name = entry_name.get()
        location = entry_location.get()
        email = entry_email.get()

        query = "SELECT * FROM customer WHERE 1=1"
        params = []

        if national_id:
            query += " AND national_id = %s"
            params.append(national_id)
        if name:
            query += " AND name = %s"
            params.append(name)
        if location:
            query += " AND location = %s"
            params.append(location)
        if email:
            query += " AND email = %s"
            params.append(email)
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(query, tuple(params))
        customers = cur.fetchall()

        results_window = tk.Toplevel(new_window)
        results_window.title("Customer Search Results")

        for i, customer in enumerate(customers):
            tk.Label(results_window, text=f"Customer {i+1}:").grid(row=i, column=0, sticky="w")
            tk.Label(results_window, text=f"National ID: {customer[0]}").grid(row=i, column=1, sticky="w")
            tk.Label(results_window, text=f"Name: {customer[1]}").grid(row=i, column=2, sticky="w")
            tk.Label(results_window, text=f"Email: {customer[2]}").grid(row=i, column=3, sticky="w")
            tk.Label(results_window, text=f"Location: {customer[3]}").grid(row=i, column=4, sticky="w")
            tk.Label(results_window, text=f"Phone Number: {customer[4]}").grid(row=i, column=5, sticky="w")
            tk.Label(results_window, text=f"Is Seller: {customer[5]}").grid(row=i, column=6, sticky="w")

            if customer[5]: 
                cur.execute("SELECT * FROM seller WHERE seller_id = %s", (customer[0],))
                seller = cur.fetchone()
                tk.Label(results_window, text=f"Seller ID: {seller[0]}").grid(row=i, column=7, sticky="w")
                tk.Label(results_window, text=f"Seller Type Name: {seller[1]}").grid(row=i, column=8, sticky="w")

        cur.close()
        conn.close()

    new_window = tk.Toplevel(root)
    new_window.title("Search for Customers")

    tk.Label(new_window, text="National ID:").grid(row=0, column=0)
    entry_national_id = tk.Entry(new_window)
    entry_national_id.grid(row=0, column=1)

    tk.Label(new_window, text="Name:").grid(row=1, column=0)
    entry_name = tk.Entry(new_window)
    entry_name.grid(row=1, column=1)

    tk.Label(new_window, text="Location:").grid(row=2, column=0)
    entry_location = tk.Entry(new_window)
    entry_location.grid(row=2, column=1)

    tk.Label(new_window, text="Email:").grid(row=3, column=0)
    entry_email = tk.Entry(new_window)
    entry_email.grid(row=3, column=1)

    tk.Button(new_window, text="Search", command=submit_search_customers).grid(row=4, columnspan=2)

def show_customers():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM customer")
    customers = cur.fetchall()
    cur.close()
    conn.close()
    
    new_window = tk.Toplevel(root)
    new_window.title("All Customers")

    for index, customer in enumerate(customers):
        tk.Label(new_window, text=f"ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}, Location: {customer[3]}, Phone: {customer[4]}, Is Seller: {customer[5]}").grid(row=index, column=0)

def show_estates():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM estate")
    estates = cur.fetchall()
    cur.close()
    conn.close()

    new_window = tk.Toplevel(root)
    new_window.title("All Estates")

    for index, estate in enumerate(estates):
        tk.Label(new_window, text=f"ID: {estate[0]}, Title: {estate[1]}, Description: {estate[2]}, Location: {estate[3]}, Meterage: {estate[4]}, Rooms: {estate[5]}, Price: {estate[6]}, Build Date: {estate[7]}, Sell Type: {estate[8]}, Estate Type: {estate[9]}, Seller ID: {estate[10]}, Parking: {estate[11]}").grid(row=index, column=0)

def show_page():
    new_window = tk.Toplevel(root)
    new_window.title("show options")

    tk.Button(new_window, text="show customers", command=show_customers).grid(row=0, column=0)
    tk.Button(new_window, text="show estates", command=show_estates).grid(row=1, column=0)

def insert_page():
    new_window = tk.Toplevel(root)
    new_window.title("Insert Options")

    tk.Button(new_window, text="Insert to Customer", command=insert_customer).grid(row=0, column=0)
    tk.Button(new_window, text="Insert to Estates", command=insert_estate).grid(row=1, column=0)

def delete_page():
    new_window = tk.Toplevel(root)
    new_window.title("Delete Options")

    tk.Button(new_window, text="Delete from Customers", command=delete_customer).grid(row=0, column=0)
    tk.Button(new_window, text="Delete from Estates", command=delete_estate).grid(row=1, column=0)

def update_page():
    new_window = tk.Toplevel(root)
    new_window.title("Update Options")
    tk.Button(new_window, text="Update Customer", command=update_customer).grid(row=0, column=0)
    tk.Button(new_window, text="Update Estate", command=update_estate).grid(row=1, column=0)

def search_page():
    new_window = tk.Toplevel(root)
    new_window.title("Search Options")

    tk.Button(new_window, text="Search for Estates", command=search_estates).grid(row=0, column=0)
    tk.Button(new_window, text="Search for Customers", command=search_customers).grid(row=1, column=0)

root = tk.Tk()
root.title("Database GUI")

tk.Button(root, text="Associate Seller with Estate", command=associate).pack(pady=10)
tk.Button(root, text="Inserting", command=insert_page).pack(pady=5)
tk.Button(root, text="Deleting", command=delete_page).pack(pady=5)
tk.Button(root, text="Search", command=search_page).pack(pady=5)
tk.Button(root, text="Update", command=update_page).pack(pady=5)
tk.Button(root, text="show", command=show_page).pack(pady=5)

root.mainloop()

