import textwrap
import pyodbc

# Driver.
DRIVER = '{ODBC Driver 17 for SQL Server}'

# ServeName and Database Name.
server_name = 'INSERT'
database_name = 'INSERT'

# Serve URL AZURE.
server = '{server_name}.database.windows.net,1433'.format(server_name=server_name)

# Username & Password.
username = 'INSERT'
password = 'INSERT'

# Full Conection String.
connection_string = textwrap.dedent('''
    DRIVER={DRIVER};
    Server={server};
    Database={database};
    Uid={username};
    Pwd={password};
    Encrypt=yes;
    TrustServerCertificate-no;
    Connection Timeouy=30;
'''.format(
    DRIVER=DRIVER,
    server=server,
    database=database_name,
    username=username,
    password=password
))

# PYODBC Connection object.
cnxn: pyodbc.Connection = pyodbc.connect(connection_string)

# Cursor Object.
cursor: pyodbc.Cursor = cnxn.cursor()

# Define a Select Query.
#select_query = "SELECT * FROM [tradeview_db]"

# Make sure To Delete the signals < and >, Table Must Stand Alone After "DELETE FROM" Funtion
cursor.execute(''' DELETE FROM <INSERT TABLE NAME HERE>
                WHERE ID in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
                31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 
                41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 
                51, 52, 53, 54, 55, 56, 57, 58, 59, 60)
               ''')

# Define an Insert Query. / These are the Coluns From the Table
insert_query = "INSERT INTO [tradeview_db] (ID, CODE, ASSET, PRICE, VARIATION, VOLUME) VALUES (?, ?, ?, ?, ?, ?)"

# Define my Recordset. / Where you Put Your Data
records = [
   (1, 'TEST1', 'TEST2', 'TEST3', 'TEST4', 'TEST5'),
   (2, 'TEST1', 'TEST2', 'TEST3', 'TEST4', 'TEST5'),
   (3, 'TEST1', 'TEST2', 'TEST3', 'TEST4', 'TEST5'),
   (4, 'TEST1', 'TEST2', 'TEST3', 'TEST4', 'TEST5'),
   (5, 'TEST1', 'TEST2', 'TEST3', 'TEST4', 'TEST5'),
   (6, 'TEST1', 'TEST2', 'TEST3', 'TEST4', 'TEST5')
]

# Define the Data Types of the Input Values.
cursor.setinputsizes(
    [
        (pyodbc.SQL_VARCHAR, 50, 0),
        (pyodbc.SQL_VARCHAR, 50, 0),
        (pyodbc.SQL_VARCHAR, 50, 0),
        (pyodbc.SQL_VARCHAR, 50, 0),
        (pyodbc.SQL_VARCHAR, 50, 0),
        (pyodbc.SQL_VARCHAR, 50, 0)      
    ]
)

# Execute the Insert Statement.
cursor.executemany(insert_query, records)

# Commit the Transaction.
cursor.commit()

# Close Connection.
cnxn.close


