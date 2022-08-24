from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Deporte:
    db_name = 'busco_team'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.nombre = db_data['nombre']
        # self.user_id = db_data['user_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']


#LEER
    @classmethod
    def get_all(cls):
        query = """SELECT *FROM deportes;"""""
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_actividades = []
        for row in results:
            print(row['nombre'])
            all_actividades.append( cls(row) )
        return all_actividades




    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM deportes WHERE id = %(evento_id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )


