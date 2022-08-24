from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Evento:
    db_name = 'busco_team'

    def __init__(self,db_data):
        self.id = db_data['id']
        self.fecha = db_data['fecha'] 
        self.hora_juego = db_data['hora_juego'] 
        self.edad_min = db_data['edad_min']
        self.edad_max = db_data['edad_max']  
        self.jugadores_requeridos = db_data['jugadores_requeridos']
        self.ubicacion = db_data['ubicacion']
        self.creador_id = db_data['creador_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.deporte_id = db_data['deporte_id']
        self.deporte = db_data['deporte']




#CREAR evento
    @classmethod
    def save(cls,data):
        query = """INSERT INTO eventos (fecha, hora_juego, edad_min, edad_max, jugadores_requeridos, ubicacion, deporte_id, creador_id)
        VALUES (%(fecha)s,%(hora_juego)s,%(edad_min)s,%(edad_max)s,%(jugadores_requeridos)s,%(ubicacion)s, %(deporte_id)s, %(creador_id)s);"""
        result = connectToMySQL(cls.db_name).query_db(query, data)
        print("crear evento", result)
        return result



#añadir un usuario  al evento
    @classmethod
    def add_user(cls,data):
        print(data)
        query = """INSERT INTO eventos_users (evento_id,user_id) values ( %(evento_id)s ,%(user_id)s );"""
        result= connectToMySQL(cls.db_name).query_db(query,data)
        return result



#INGRESAR A EVENTO
    @classmethod
    def ingresar_a_evento(cls,data):
        print(data)
        query = """INSERT INTO eventos_users (evento_id,user_id) values ( %(evento_id)s ,%(user_id)s );"""
        result= connectToMySQL(cls.db_name).query_db(query,data)
        return result





#LEER
    @classmethod
    def get_all(cls):
        # query = "SELECT * FROM eventos;"
        query = """SELECT c.*, u.nombre AS deporte
        FROM busco_team.eventos AS c
        JOIN busco_team.deportes AS u ON (c.deporte_id = u.id)
        WHERE fecha >= NOW() 
        ORDER BY fecha asc;""" #aca se debe hacer un JOIN con la tabla deporte para traer el nombre
        results =  connectToMySQL(cls.db_name).query_db(query)
        all_eventos = []
        for row in results:
            print(row['deporte'])
            all_eventos.append( cls(row) )
        return all_eventos




#MOSTRAR UN EVENTO
    @classmethod
    def get_one(cls,data):
        query = """SELECT c.*, u.nombre AS deporte
        FROM busco_team.eventos AS c
        JOIN busco_team.deportes AS u ON (c.deporte_id = u.id) 
        WHERE c.id = %(evento_id)s;"""
        results = connectToMySQL(cls.db_name).query_db(query,data)
        return cls( results[0] )




#MODIFICAR UN EVENTO
    @classmethod
    def update(cls, data):
        query = """UPDATE eventos SET fecha=%(fecha)s, hora_juego=%(hora_juego)s,
        edad_min=%(edad_min)s, edad_max=%(edad_max)s, jugadores_requeridos=%(jugadores_requeridos)s,
        ubicacion=%(ubicacion)s, updated_at=NOW(), deporte_id=%(deporte_id)s WHERE id = %(id)s;"""
        return connectToMySQL(cls.db_name).query_db(query,data)


    @classmethod
    def update_deporte(cls,data):
        query = """UPDATE eventos_users SET evento_id =%(evento_id)s WHERE id= %(id)s;"""
        return connectToMySQL(cls.db_name).query_db(query,data)



#INGRESAR A EVENTO
    @classmethod
    def ingresar_a_evento(cls,data):
        print(data)
        query = """INSERT INTO eventos_users (evento_id,user_id) values ( %(evento_id)s ,%(user_id)s );"""
        result= connectToMySQL(cls.db_name).query_db(query,data)
        return result











    #BORRAR
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM eventos WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)






#VALIDAR CREACION Evento
    @staticmethod
    def validate_evento(evento):
        is_valid = True
        

        # if evento['deporte_id'] == "":
        #     is_valid = False
        #     flash("Por favor ingrese un deporte.","evento")

        if evento['fecha'] == "":
            is_valid = False
            flash("Por favor ingrese una fecha.","evento")


#INGRESAR FECHA ACTUAL (no ingresar una fecha anterior)
        # if evento['fecha'] == "":
        #     is_valid = False
        #     flash("Por favor ingrese una fecha.","evento")


        if evento['hora_juego'] == "":
            is_valid = False
            flash("Por favor ingrese la hora del evento.","evento")


        # if evento['edad_min'] > int(18):
        #     is_valid = False
        #     flash("Por favor ingrese la edad minima de los participantes.","evento")


        if evento['edad_max'] == "":
            is_valid = False
            flash("Por favor ingrese la edad maxima de los participantes.","evento")


        if evento['ubicacion'] == "":
            is_valid = False
            flash("Por favor ingrese la ubicación del evento.","evento")



        # if float(sport['price']) < float (1):
        #     is_valid = False
        #     flash("El precio debe ser mayor a 0.","sport")


        # if sport['description'] == "":
        #     is_valid = False
        #     flash("Por favor ingrese una descripción.","sport")


        # if sport['make'] == "":
        #     is_valid = False
        #     flash("Por favor ingrese una marca.","sport")

        # if int(sport['year']) < int(1):
        #     is_valid = False
        #     flash("El año debe ser mayor a 0.","sport")

        return is_valid



