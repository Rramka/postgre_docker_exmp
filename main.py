from sqlalchemy import create_engine
import psycopg2
import pandas as pd
import time


# /////////////     panda      /////////////////

# data = {
#   "Name": ["Alice", "Bob", "Charlie"],
#   "Age": [25, 30, 28],
#   "City": ["New York", "Los Angeles", "Chicago"]
# }

# # Create a DataFrame from the dictionary
# df = pd.DataFrame(data)


# print(df)


# time.sleep(30)


# /////////////     posgres      /////////////////

# DB_HOST = "0.0.0.0"
# DB_PORT = 7777
# DB_USER = "postgres"
# DB_PASSWORD = "postgres"
# DB_NAME = "postgres"

# connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# engine = create_engine(connection_string,pool_pre_ping=True)
# conn = engine.connect()

conn = psycopg2.connect(database = "postgres", 
                        user = "postgres", 
                        host= 'postgres_db',
                        password = "postgres",
                        port = 7777)


# # Open a cursor to perform database operations
cur = conn.cursor()
# # Execute a command: 
cur.execute("""select * from pg_catalog.pg_tables ; """)
print(cur.fetchall())
# cur.execute("create table test(id int)")
# cur.execute("insert into test values(1)")
# cur.execute("select * from test")
# print(cur.fetchall())



# # Make the changes to the database persistent
conn.commit()
# # Close cursor and communication with the database
cur.close()
conn.close()


# def getConnection(dbname):
#     user='postgres'
#     password='postgres'
#     host ='localhost'
#     port='5432'
#     return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')  

# , dst_dbname, schema, tablename, insertiontype

# def fillPosgres( df):
#         df.to_sql("client", getConnection("postgres-db") , schema="default", if_exists="replace", index=False)
        


# fillPosgres(df)
