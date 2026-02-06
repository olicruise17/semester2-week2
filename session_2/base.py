import sqlite3
# you will need to pip install pandas matplotlib
import pandas as pd
import matplotlib as mpl

def get_connection(db_path="orders.db"):
    """
    Establish a connection to the SQLite database.
    Returns a connection object.
    """
    conn = sqlite3.connect(db_path)
    ##conn.row_factory = sqlite3.Row
    return conn

def main():

    db = get_connection()

    ## product categories
    # query = """
    # SELECT category 
    # FROM products"""

    ## number of customers
    # query = """
    # SELECT SUM(customer_id)
    # FROM customers;"""

#   select orders for a particular user
#     choice = "barkermohammad@example.com"
#     query = """
#     SELECT o.order_ID
#     FROM orders o
#     JOIN customers c
#     ON c.customer_id = o.customer_id
#     WHERE c.email = ?;"""


    # selects products under 2 pounds
    # choice = 2
    # query = """
    # SELECT name
    # FROM products
    # WHERE price <?"""

    # top 5 spenders
    # query = """
    # SELECT c.customer_id, o.total_amount
    # FROM customers c JOIN orders o
    # ON c.customer_id = o.customer_id
    # ORDER BY o.total_amount DESC LIMIT 5"""


    query = """
    SELECT p.category, COUNT(oi.product_id)
    FROM products p
    JOIN order_items oi
    ON p.product_id = oi.product_id
    ORDER BY COUNT(oi.product_id) DESC"""

    cursor = db.execute(query)

    # or
    for row in cursor:
        print(row)

    cursor.close()    
    db.close()


if __name__=="__main__":
    main()

# def total_sales():

#     conn = get_connection()

#     query = """
#     SELECT SUM(quantity)
#     FROM order_items;"""

#     cursor = conn.execute(query)

#     student = cursor.fetchone()
#     # or
#     for row in cursor:
#         print(row)