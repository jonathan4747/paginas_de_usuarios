from usuario_app.config.mysqlconnection import MySQLConnection, connectToMySQL

class Usuario:
    def __init__(self,id,nombre,apellido,email,created_at,updated_at):
        self.id = id
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.created_at=created_at
        self.updated_at=updated_at
        
    @classmethod
    def agregarUsuario(cls,nuevoUsuario):
        query = "insert into usuario(nombre,apellido,email,created_at,updated_at) VALUES (%(nombre)s,%(apellido)s,%(email)s,NOW(),NOW());"
        resultado = connectToMySQL("usuario").query_db(query,nuevoUsuario)
        return resultado

    @classmethod
    def listaUsuario(self):
        query = "SELECT* FROM usuario;"
        resultado=connectToMySQL("usuario").query_db(query)
        listaUsuarios = []
        for usuarios in resultado:
            listaUsuarios.append( Usuario( usuarios["id"],usuarios["nombre"], usuarios["apellido"], usuarios["email"],usuarios["created_at"],usuarios["updated_at"]))
        return listaUsuarios
    
    @classmethod
    def obtenerDatosUsuario( cls, usuario ):
        query = "SELECT * FROM usuario WHERE id = %(id)s;"
        resultado = connectToMySQL( "usuario" ).query_db( query, usuario )
        return resultado
    
    @classmethod
    def editarUsuario(cls,editaUsuario):
        query = "UPDATE usuario SET nombre=%(nombre)s ,apellido=%(apellido)s,email=%(email)s WHERE id= %(id)s;"
        #print("Verificar si llega al metodo editarUsuario",query)
        resultado = connectToMySQL( "usuario" ).query_db( query, editaUsuario )
        return resultado
        
    @classmethod
    def eliminarUsuario(cls,eliminaUsuario):
        query = "DELETE FROM usuario WHERE id= %(id)s;"
        resultado = connectToMySQL( "usuario" ).query_db( query, eliminaUsuario )
        print("Verificar si llega al metodo editarUsuario",query)
        return resultado
        