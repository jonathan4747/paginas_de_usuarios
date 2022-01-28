from flask import Flask, render_template, request, redirect, session
from usuario_app import app
from usuario_app.modelos.modelo_usuarios import Usuario

@app.route('/')
def paginablanca():
    return redirect('/user')


@app.route('/user',methods=['GET'])
def paginaUsuario():
        listaUsuarios=Usuario.listaUsuario()
        return render_template("index.html", usuarios=listaUsuarios)
    
@app.route('/user/new' , methods=['GET'])
def paginaRegistor():
    return render_template("plataforma.html")

@app.route('/añadir',methods=['GET'])
def botonAñadir():
    return redirect('/user/new')

@app.route('/registro',methods=['POST'])
def añadirRegistro():
    nuevoUsuario = {
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    resultado = Usuario.agregarUsuario(nuevoUsuario)
    return redirect('/user')

@app.route('/user/<int:id>', methods=['GET'])
def verUsuario(id):
    obtenerUsuario={
        "id": id
    }
    resultado = Usuario.obtenerDatosUsuario(obtenerUsuario)
    return render_template( "usuario.html", usuario=resultado[0] )

@app.route('/user/edit/<int:id>',methods=['GET'])
def editarUsuario(id):
    usuario_editar={
        "id": id
    }
    resultado=Usuario.obtenerDatosUsuario(usuario_editar)
    print(resultado)
    return render_template ("editar.html", usuario=resultado[0])
    
@app.route( '/usuario/edit/<int:id>', methods=["POST"] )
def cambiodeDatos( id ):
    #print("llega id", id)
    usuarioEditar = {
         "id" : id,
        "nombre" : request.form["nombre"],
        "apellido" : request.form["apellido"],
        "email" : request.form["email"]
    }
    #print("datos a ser editados", usuarioEditar)
    resultado = Usuario.editarUsuario(usuarioEditar)
    return redirect( '/' )

@app.route( '/salir', methods=["GET"] )
def logoutUsuario():
    session.clear()
    return redirect( '/' )

@app.route( '/usuario/eliminar/<int:id>', methods=["POST"] )
def eliminarUsuario( id ):
    eliminado= {
        "id" : id
    }
    resultado = Usuario.eliminarUsuario(eliminado)
    print(eliminado)
    print(resultado)
    return redirect( '/' )
    
    


