def database_creator():
    import mysql.connector

    print("Pour l'instant je gere juste l'acces à la base de données ")
    host_name=input("Enter the host name (It must be 'localhost' 🤓) : ")
    user_name=input("Et le nom de l'hote (Par defaut c'est 'root') : ")
    pass_w=input("Et le mot de passe (Par defaut il n'y en a pas, t'auras qu'a valider à ce niveau) : ")

    db=mysql.connector.connect(
        host=host_name,
        user=user_name,
        password=pass_w,
        database="commerce"
    )

    cursor=db.cursor()
    sql=("CREATE DATABASE IF NOT EXISTS commerce")
    cursor.execute(sql)

    cursor=db.cursor()
    sql="CREATE TABLE IF NOT EXISTS utilisateur (id INT AUTO_INCREMENT PRIMARY KEY, pseudo VARCHAR(700) ,nom VARCHAR(255),prenom VARCHAR(255), num INT, date VARCHAR(20), pass_w VARCHAR(400))"
    cursor.execute(sql)

    cursor=db.cursor()
    sql=("CREATE TABLE IF NOT EXISTS produits (id_comm INT AUTO_INCREMENT PRIMARY KEY,libelle VARCHAR(255),prix_u int , qte INT, description VARCHAR(1000), user_id INT)")
    cursor.execute(sql)