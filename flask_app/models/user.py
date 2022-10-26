from flask_app.config.mysqlconnection import connectToMySQL
import re	

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #a esto se le llama ""Expresión regular"
from flask import flash

class User:
    db_name = "busco_team"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#CREAR.........
    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,age,email,password) VALUES(%(first_name)s,%(last_name)s,%(age)s,%(email)s,%(password)s)"
        return connectToMySQL(cls.db_name).query_db(query,data)


#LEER.....
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query,data)
        print(results, "GETBYID")
        print(cls(results[0]), "GETBYID")
        return cls(results[0])


#VALIDACIONES
    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db_name).query_db(query,user)

        if len(results) >= 1:
            flash("El email ya está registrado.","register")
            is_valid=False

        if not EMAIL_REGEX.match(user['email']):
            flash(" Email inválido.","register")
            is_valid=False

        if len(user['first_name']) < 3:
            flash("Nombre debe contener más de 3 caracteres.","register")
            is_valid= False

        if len(user['last_name']) < 3:
            flash("Apellido debe contener más de 3 caracteres.","register")
            is_valid= False

        if len(user['password']) < 8:
            flash("La contraseña debe contener mínimo 8 caracteres.","register")
            is_valid= False

        if user['password'] != user['confirm']:
            flash("Contraseñas no coinciden.","register")
        return is_valid