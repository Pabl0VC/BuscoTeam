from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.evento import Evento
from flask_app.models.user import User
from flask_app.models.deporte import Deporte

#CREAR..................................................
@app.route('/nuevo/evento', methods=['GET'])
def nuevo_evento():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('crear_evento.html',user=User.get_by_id(data),deportes=Deporte.get_all())


@app.route('/crear/evento',methods=['POST'])
def crear_evento():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Evento.validate_evento(request.form):
        return redirect('/nuevo/evento')
    data = {
        "fecha": request.form["fecha"],
        "hora_juego": request.form["hora_juego"],
        "edad_min": int(request.form["edad_min"]),
        "edad_max": request.form["edad_max"],
        "jugadores_requeridos": request.form["jugadores_requeridos"],
        "ubicacion": request.form["ubicacion"],
        "deporte_id" : request.form["deporte_id"],
        "user_id": session["user_id"],
        "creador_id":session["user_id"]
    }

    resultado=Evento.save(data)
    print(resultado)
    data2={
        'user_id': session["user_id"],
        'evento_id':resultado
    }
    Evento.add_user(data2)
    return redirect('/dashboard')



#MODIFICAR
@app.route('/editar/evento/<int:evento_id>')
def editar_evento(evento_id):#
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "deporte_id":evento_id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("editar_evento.html",editar=Evento.get_one(data),user=User.get_by_id(user_data),deportes=Deporte.get_all())



@app.route('/update/evento',methods=['POST'])
def update_evento():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Evento.validate_evento(request.form):
        return redirect('/editar/evento/<int:evento_id>')
    data = {
        "id": request.form["id"] ,
        "fecha": request.form["fecha"],
        "hora_juego": request.form["hora_juego"],
        "edad_min": int(request.form["edad_min"]),
        "edad_max": request.form["edad_max"],
        "jugadores_requeridos": request.form["jugadores_requeridos"],
        "ubicacion": request.form["ubicacion"],
        "deporte_id" : request.form["deporte_id"],
        "user_id": session["user_id"],
        "creador_id":session["user_id"]
    }


    resultados=Evento.update(data)
    print(resultados)
    data2={
        'user_id': session["user_id"],
        'evento_id':resultados
    }
    Evento.update_deporte(data2)
    return redirect('/dashboard')



#INGRESAR A EVENTO
@app.route('/ingresar/evento/<int:id>')
def ingresar_evento(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "evento_id" : id,
        "user_id": session["user_id"],
        "id":session["user_id"]

    }
    Evento.ingresar_a_evento(data)
    return render_template("mostrar_evento.html",evento=Evento.get_one(data),user=User.get_by_id(data))




#MOSTRAR EVENTO
@app.route('/evento/<int:id>')
def mostrar_evento(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "evento_id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("mostrar_evento.html",evento=Evento.get_one(data),user=User.get_by_id(user_data))





@app.route('/destroy/evento/<int:id>')
def destroy_evento(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Evento.destroy(data)
    return redirect('/dashboard')



