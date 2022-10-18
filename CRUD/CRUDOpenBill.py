from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

try:
    client = MongoClient(MONGO_URI)
    db = client['OpenBill']
    collection = db['Users']
    collection2 = db['Empresas']
    # ---------------- INICIO DE LA CRUD ---------------- 
    # ---------------- CREATE ---------------- 
    # collection.insert_one({"nombreUsuario": "David", "apellidoUsuario": "Madrid", "telefono": 3196188077, "tipoUsuario": "admin"})
    
    # ---------------- READ ---------------- 
    print("Usuarios.")
    for usuarios in collection.find():
        print(f'Nombre: {usuarios["nombreUsuario"]} | Apellido: {usuarios["apellidoUsuario"]} | Teléfono: {usuarios["telefono"]} | Tipo de Usuario: {usuarios["tipoUsuario"]}')
    # print(collection.find())
    # print(collection.find_one({"nombreUsuario": "Sebastian"})) ---> Solo trae un resultado
    
    print()
    print("Empresas.")
    
    for empresas in collection2.find():
        print(f'Nombre Empresa: {empresas["nombreEmpresa"]} | Direccion: {empresas["direccion"]} | Ciudad: {empresas["ciudad"]}')
    
    # ---------------- UPDATE ---------------- 
    # collection.update_one({"apellidoUsuario": "Agudelo"}, {"$set": {"telefono": "3226403046"}})
    
    # ---------------- DELETE ----------------
    #collection.delete_one({"apellidoUsuario": "Agudelo"})
    #collection.delete_many({...})

    # cliente.server_info()
    # print('Conexion exitosa con mongo')
    
    client.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print('Tiempo excedido ' + errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print('Error a la conexion ' + errorConexion)