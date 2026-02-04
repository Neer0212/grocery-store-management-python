import sqlite3

def connect():
    con = sqlite3.connect("grocery.db")
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        quantity INTEGER,
        threshold INTEGER
    )
    """)

    con.commit()
    return con, cur


def add_product(name, price, quantity, threshold):
    con, cur = connect()
    cur.execute("INSERT INTO products (name, price, quantity, threshold) VALUES (?, ?, ?, ?)",
                (name, price, quantity, threshold))
    con.commit()
    con.close()


def get_products():
    con, cur = connect()
    cur.execute("SELECT * FROM products")
    rows = cur.fetchall()
    con.close()
    return rows


def delete_product(product_id):
    con, cur = connect()
    cur.execute("DELETE FROM products WHERE id=?", (product_id,))
    con.commit()
    con.close()


def update_quantity(product_id, new_qty):
    con, cur = connect()
    cur.execute("UPDATE products SET quantity=? WHERE id=?", (new_qty, product_id))
    con.commit()
    con.close()


def make_sale(product_id, quantity):
    con, cur = connect()
    cur.execute("SELECT price, quantity FROM products WHERE id=?", (product_id,))
    price, stock = cur.fetchone()

    if quantity > stock:
        con.close()
        return None

    total = price * quantity
    new_stock = stock - quantity

    cur.execute("UPDATE products SET quantity=? WHERE id=?", (new_stock, product_id))
    con.commit()
    con.close()
    return total


def search_product(name):
    con, cur = connect()
    cur.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + name + '%',))
    rows = cur.fetchall()
    con.close()
    return rows
