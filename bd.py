import sqlite3
conn = sqlite3.connect('example.db')

class bd {

    c = conn.cursor()

    # Create table

    def crearTabla():
        c.execute('''CREATE TABLE stocks
                    (date text, trans text, symbol text, qty real, price real)''')

    def insertarProducto():

        # Insert a row of data
        c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

    def insertarProductos():

        purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                    ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                    ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                    ]
        c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

        # Save (commit) the changes
        conn.commit()

    def leerCarta():
        for row in c.execute('SELECT * FROM stocks ORDER BY price'):
            print(row)

    def cerrarBD():
        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    }