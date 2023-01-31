import psycopg2
class DBConnection:
    conn = None
    cur = None
    def __init__(self):
        pass
    @classmethod
    def connect_db(cls):
        cls.conn  = psycopg2.connect(dbname='postgres', user='postgres', password='Finserv@2023')
        cls.cur = cls.conn.cursor()
    @classmethod
    def create_table(cls):
        cls.cur.execute(f"create table if not exists pet(pet_id serial primary key,pet_name varchar , pet_owner varchar,pet_breed varchar) ;")
    @classmethod
    def display_records(cls):
        try:
            cls.cur.execute(f"select * from pet ;")
            data  =cls.cur.fetchall()
            return data
        except Exception as e:
            print(e)

    @classmethod
    def insert_data(cls,pet_name,pet_owner,pet_breed):
        cls.cur.execute(f"insert into pet(pet_name,pet_owner,pet_breed) values ('{pet_name}','{pet_owner}','{pet_breed}') ;")
        cls.conn.commit()
    @classmethod
    def update_data(cls,pet_id,pet_name,pet_owner,pet_breed):
        cls.cur.execute(f"update pet set pet_name ='{pet_name}', pet_owner='{pet_owner}', pet_breed ='{pet_breed}' where pet_id = {pet_id};")
        cls.conn.commit()
    @classmethod
    def delete_row(cls,pet_id):    
        try:
            cls.cur.execute(f"delete from pet where pet_id={pet_id};")
            cls.conn.commit()
        except Exception as e:
            print(e)
    @classmethod
    def close_db(cls):
        cls.conn.close()
