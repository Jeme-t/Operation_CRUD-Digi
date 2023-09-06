from tkinter import *
import mysql.connector
from tkinter import messagebox
from tkcalendar import DateEntry
from hashlib import sha512
import creation_database
#import os
#os.chdir("")

def pdf_creator():
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    def create_pdf(file_name):
        c = canvas.Canvas(file_name, pagesize=letter)
        c.drawString(100, 750, "Hello, World!")
        c.save()

    if __name__ == "__main__":
        create_pdf("exemple.pdf")

def hasher(valeur):
    mdp = valeur
    mdp = mdp.encode()
    mdp_sign = sha512(mdp).hexdigest()
    return mdp_sign

#var=input("Password : ")
#print(f"Le hash est : \n \t {hasher(var)}")

def ad(x):
    x+=2
    return x

icon="C://Users//emery//Desktop//TP_DigiWeb//site.ico"

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="commerce"
)
id=1
fen=0
fen_p=0
cadre=0
ent_1=0
ent_2=0
ent_3=0
ent_4=0
ent_5=0
ent_6=0
ent_7=0
liste=0

add=0
confirm=0
"""
def confirm_passw(id):
    global fen
    global cadre
    print(id)
    
    cadre=Frame(fen, width= 300, height= 250,bg="#dbbe92")
    cadre.pack(expand=1)
    
    text=Label(cadre, text="Entrez votre mot de passe ")
    text.pack(expand=1, fill='y', side='top')
    pass_w=Entry(cadre)
    pass_w.pack(expand=1, fill='x', side='top')
    
    def next_p(pass_w):
        pass_w=pass_w.get()
        check=db.cursor()
        sql="SELECT pass_w FROM utilisateur WHERE id='%s'" %id
        check.execute(sql)
        pass_w_fb=check.fetchone()
        print(pass_w_fb[0])
        if pass_w!=pass_w_fb[0]:
            resp=Label(cadre, text="Incorrecte", bg="#e5382b")
            resp.pack(expand=1, fill='x', side='top')
            var=False
        else :
            resp=Label(cadre, text="Correcte", bg="#32ea44")
            resp.pack(expand=1, fill='x', side='top')
            var=True
        return var
    
    send=Button(cadre, text="Valider", command=lambda pass_w=pass_w : next_p(pass_w))
    send.pack(expand=1, fill='y', side='top')
    
    cadre_p=Frame(fen, width= 240, height= 100,bg="#dbbe92")
    cadre_p.pack(side="left", padx=0, pady=0, )
    text=Label(cadre_p, text="Entrez votre mot de passe ")
    text.pack(expand=1, fill='y', side='top')
    pass_w=Entry(cadre_p)
    pass_w.pack(expand=1, fill='x', side='top')
    send=Button(cadre_p, text="Valider", command=1)#lambda pass_w=pass_w : next_p(pass_w))
    send.pack(expand=1, fill='y', side='top')
"""

def reset():
    cadre.pack_forget()
    home()

def before_buy(id):
    lambda id=id: buy(id)
    cadre.pack_forget()
    buy(id)

def consult(id):
        global cadre
        cadre.pack_forget()
            
        cadre=Frame(fen, width= 630, height=10000,bg="silver")
        cadre.pack(expand=1)
        
        adds=Button(cadre ,text="+",bg="#ffd177" ,font=("times new roman", 14) ,bd=3 ,command=lambda id=id : before_buy(id), relief="solid")
        adds.place(x=2, y=2)
        
        button=Button(cadre,text="Deconnexion" ,bg="#ffd177" ,font=("times new roman", 14) ,bd=3 ,command=reset, relief="solid")
        button.place(x=510 , y=0)
        
        title_1=Label(cadre,text="Nombre", bg="#8D857B", fg="black", font=("Times new roman", 13) , width=11)
        title_1.place(x=73,y=0)
            
        title_1=Label(cadre,text="Libellé", bg="#8D857B", fg="black", font=("Times new roman", 13) , width=12)
        title_1.place(x=180,y=0)
                
        title_1=Label(cadre,text="Prix Unitaire", bg="#8D857B", fg="black", font=("Times new roman", 13) , width=17)
        title_1.place(x=280,y=0)
            
        title_1=Label(cadre,text="Qte", bg="#8D857B", fg="black", font=("Times new roman", 13) , width=10)
        title_1.place(x=410,y=0)
        
        print(id)
        cursor=db.cursor()
        cursor.execute("SELECT * FROM produits WHERE user_id='%s'" %(id))
        contain=cursor.fetchall()
        #for x in contain:
        z=2
        for num , val in enumerate(contain):
            z+=24
            #print(f"{num+1} \t {val[1]} ")
            
            id_list=Label(cadre, text=f"{num+1}", bg="silver", font=("Times new roman", 13), width=2)
            id_list.place(x=117, y=z)
        
            list=Label(cadre,text=f"{val[1]}", bg="silver", fg="black", font=("Times new roman", 13) , width=12)
            list.place(x=190,y=z)
        
            list=Label(cadre,text=f"{val[2]}", bg="silver", fg="black", font=("Times new roman", 13) , width=10)
            list.place(x=290,y=z)
        
            list=Label(cadre,text=f"{val[3]}", bg="silver", fg="black", font=("Times new roman", 13) , width=10)
            list.place(x=410,y=z)

def buy(id):
    global ent_1
    #ent_1=ent_1.get()
    print(ent_1)

    global ent_2
    #ent_2=ent_2.get()
    print(ent_2)

    global ent_3
    #ent_3=ent_3.get()
    print(ent_3)

    global ent_4
    #ent_4=ent_4.get()
    print(ent_4)

    global add
    global confirm
    global cadre
    
    cadre=Frame(fen, width= 485, height= 215,bg="#dbbe92")
    cadre.pack(expand=1)
    
    fiche_1=Label(cadre, bg="#9BC2E6", font=("Times New Roman",23), text="  COMMANDES  ", bd=3,relief="solid")
    fiche_1.place(x=150, y=15)

    lib_1=Label(cadre,text="Libellé", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=70)

    lib_1=Label(cadre,text="Prix Unitaire", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=90)

    lib_1=Label(cadre,text="Quantité", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=110)

    lib_1=Label(cadre,text="Description", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=130)
    
    description_text="Fromage"
    text=StringVar(value=description_text)

    ent_1=Entry(cadre,textvariable=text , font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_1.place(x=205, y=70)
    
    description_text="200"
    text=StringVar(value=description_text)

    ent_2=Entry(cadre,textvariable=text , font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_2.place(x=205, y=90)
    
    description_text="12"
    text=StringVar(value=description_text)

    ent_3=Entry(cadre,textvariable=text , font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_3.place(x=205, y=110)

    description_text="None"
    text=StringVar(value=description_text)
    
    ent_4=Entry(cadre,textvariable=text ,font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_4.place(x=205, y=130)
    
    #pff=["Secteur","Liste","Orbe","Caprice","Gym"]
    
    #ent_opt=Listbox()
    #ent_opt.place(x=0,y=0)

    def next_adds(id):
        
        global ent_1
        global ent_2
        global ent_3
        global ent_4
        print("Done_1")
        cadre.pack_forget()
        print("Done_2")
        
        ent_1=ent_1.get()
        ent_2=ent_2.get()
        ent_3=ent_3.get()
        ent_4=ent_4.get()
        print("Get Done")
        
        #def adds_f(id):
        print(f"C'est {ent_1}")
        print("Ok")
        print(f"C'est {id}")
        cursor=db.cursor()
        sql="INSERT INTO produits (libelle, prix_u, qte, description, user_id) VALUES (%s, %s, %s, %s, %s)"
        val=( ent_1, ent_2, ent_3, ent_4, id)
        cursor.execute(sql,val)
        buy(id)

    adds=Button(cadre, text=" Ajouter ", width=14, bd=2, relief="solid", font=("Times new Roman", 13), bg="#7a7a7a", command=lambda id=id: next_adds(id))
    adds.place(x=60,y=165)

    button=Button(cadre, text=" Afficher ", width=14, bd=2, relief="solid", font=("Times new Roman", 13), bg="#7a7a7a", command=lambda id=id: consult(id))
    button.place(x=260,y=165)

def edit_user(id):
    id
    print(id)
    
    global cadre
    
    cursor=db.cursor()
    cursor.execute("SELECT nom, prenom, num, date, id FROM utilisateur WHERE id='%s'" %(id))
    liste=cursor.fetchone()
    
    
    cadre=Frame(fen, width= 485, height= 215,bg="#dbbe92")
    cadre.pack(expand=1)

    fiche_1=Label(cadre, bg="#9BC2E6", font=("Times New Roman",23), text="  MODIFICATIONS  ", bd=3,relief="solid")
    fiche_1.place(x=150, y=15)
    
    
    var=liste[0]
    var_0=StringVar(value=var)
    
    var=liste[1]
    var_1=StringVar(value=var)
    
    var=liste[2]
    var_2=StringVar(value=var)
    
    var=liste[3]
    var_3=StringVar(value=var)
    
    var=liste[4]
    var_4=StringVar(value=var)

    lib_1=Label(cadre,text=f"NOM ", font=("calibri",10), width=20, bd=2,  bg="#dbbe92", justify="right")
    lib_1.place(x=60, y=70)

    lib_1=Label(cadre,text="PRENOM", font=("calibri",10), width=20, bd=2,  bg="#dbbe92", justify="right")
    lib_1.place(x=60, y=90)

    lib_1=Label(cadre,text="N Telephone", font=("calibri",10), width=20, bd=2,  bg="#dbbe92", justify="right")
    lib_1.place(x=60, y=110)

    lib_1=Label(cadre,text="DATE DE NAISSANCE", font=("calibri",10), width=20, bd=2,  bg="#dbbe92", justify="right")
    lib_1.place(x=60, y=130)

    ent_1_1=Entry(cadre,textvariable=var_0 , font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_1_1.place(x=205, y=70)

    ent_2_1=Entry(cadre, textvariable=f"{var_1}" , font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_2_1.place(x=205, y=90)
    
    ent_3_1=Entry(cadre,textvariable=f"{var_2}" , font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_3_1.place(x=205, y=110)

    ent_4_1=DateEntry(cadre,textvariable=f"{var_3}" , font=("calibri",10), width=25, bd=2,borderwidth=4 , relief="solid", background="#faebd7", foreground='grey')
    ent_4_1.place(x=205, y=130)
    
    id_info=Label(cadre,text="ID", font=("calibri",10), width=4, bd=2,  bg="#dbbe92", justify="right")
    id_info.place(x=440, y=70)
    
    id_ent=Entry(cadre,textvariable=f"{var_4}" , font=("calibri",10), width=4, bd=2,  bg="#faebd7", justify="center")
    id_ent.place(x=440, y=90)
    
    #confirm=Button(cadre, text=" Modifier ", width=30, bd=2, relief="solid", font=("Times new Roman", 16), bg="#7a7a7a", command=lambda liste=liste : update(liste))
    #confirm.place(x=60,y=165)

    def set_new_data():
        nom=ent_1_1.get()
        prenom=ent_2_1.get()
        num=ent_3_1.get()
        date=ent_4_1.get()
        
        cursor=db.cursor()
        sql = "UPDATE utilisateur SET nom='%s', prenom='%s', num='%s', date='%s' WHERE id='%s'"%(nom, prenom, num, date, id)
        cursor.execute(sql)
        db.commit()
        
        print(f"OK {nom}\t {prenom}\t {num}\t {date} ")
    
    def next_edit():
        set_new_data()
        cadre.pack_forget()
        old_user()

    confirm=Button(cadre, text=" Modifier ", width=30, bd=2, relief="solid", font=("Times new Roman", 16), bg="#7a7a7a", command=next_edit)
    confirm.place(x=60,y=165)

def delete_on(id):
    id
    print("Alors",id)
    cursor=db.cursor()
    sql=" DELETE  FROM utilisateur WHERE id='%s' "%(id)
    
    cursor.execute(sql)
    print("Done")
    db.commit()

def confirm_del(id):
    response = messagebox.askyesno("Question", "Voulez-vous continuer?")
    if response:
        cadre.pack_forget()
        lambda id=id : delete_on(id)
        print("Deleting...")
        delete_on(id)
        old_user()
    else:
        print("Ouf")

def next_valid_edit(id):
        print(f"L'id est {id} ")
        #lambda id=id: next_valid_edit(id)
        cadre.pack_forget()
        lambda id=id: edit_user(id)
        edit_user(id)

def nexx(id):
    cadre.pack_forget()
    print("C'est",id)
    lambda id=id: edit_user(id)
    edit_user(id)

def profil(id):
    cursor=db.cursor()
    sql="SELECT * FROM utilisateur WHERE id='%s'"%id
    cursor.execute(sql)
    x=cursor.fetchone()
    global cadre
    cadre=Frame(fen, width= 485, height= 192,bg="#dbbe92")
    cadre.pack(expand=1)

    fiche_1=Label(cadre, bg="#dbcb92", font=("Times New Roman",23), text=f"  Profil utilisateur {x[1]}  ", bd=3,relief="solid")
    fiche_1.place(x=1, y=1)

    lib_1=Label(cadre,text=f"NOM :  {x[2]} ", font=("times new roman",12), bd=2,  bg="#dbbe92")
    lib_1.place(x=10, y=50)

    lib_1=Label(cadre,text=f"PRENOM :  {x[3]} ", font=("times new roman",12), bd=2,  bg="#dbbe92", justify="left")
    lib_1.place(x=10, y=75)

    lib_1=Label(cadre,text=f"N°Telephone :  {x[4]} ", font=("times new roman",12), bd=2,  bg="#dbbe92", justify="left")
    lib_1.place(x=10, y=100)

    lib_1=Label(cadre,text=f"DATE DE NAISSANCE :  {x[5]} ", font=("times new roman",12), bd=2,  bg="#dbbe92", justify="left")
    lib_1.place(x=10, y=125)
    
    lib_1=Label(cadre,text=f"Modifier : ", font=("times new roman",15), width=10, bd=2,  bg="#dbbe92", justify="left")
    lib_1.place(x=0, y=155)
    
    def next_e_p():
        cadre.pack_forget()
        #confirm_passw(id)
        #wait=confirm_passw(id)
        #print(wait)
        #if wait==True:
        #cadre.pack_forget()
        next_valid_edit(id)
    
    def next_e_pw():
        cadre.pack_forget()
        edit_p(id)
    
    button_1=Button(cadre,text="Profil" ,bg="#ffd1aa" ,font=("times new roman", 14) ,bd=3 ,command=next_e_p, relief="ridge")
    button_1.place(x=100, y=150)
    
    button_2=Button(cadre,text="Mot de passe" ,bg="#ffd1aa" ,font=("times new roman", 14) ,bd=3 ,command=next_e_pw, relief="ridge")
    button_2.place(x=190, y=150)
    
    button_3=Button(cadre,text="Deconnection" ,bg="#ffd177" ,font=("times new roman", 14) ,bd=3 ,command=reset, relief="solid")
    button_3.place(x=365 , y=150)
    
    button_4=Button(cadre,text="Consulter \n mon Panier" ,bg="#ffd1aa" ,font=("times new roman", 14) ,bd=3 ,command=lambda id= id : consult(id), relief="ridge")
    button_4.place(x=380 , y=50)

def edit_p(id):
    global cadre
    global ent_1
    global ent_2
    global ent_3

    cadre=Frame(fen, width= 485, height= 215,bg="#dbbe92")
    cadre.pack(expand=1)
    
    fiche_1=Label(cadre, bg="#9BC2E6", font=("Times New Roman",23), text="  PASSWORD  ", bd=3,relief="solid")
    fiche_1.place(x=150, y=15)

    lib_1=Label(cadre,text="Ancien Mot de Passe", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=70)

    lib_1=Label(cadre,text="Nouveau Mot de Passe", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=100)

    lib_1=Label(cadre,text="Confirmer Nouveau \n Mot de Passe", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=130)
    
    ent_1=Entry(cadre, font=("times new roman", 12), width=28, bd=2, relief="solid", bg="#faebd7", show="*")
    ent_1.place(x=205, y=70)

    ent_2=Entry(cadre, font=("times new roman", 12), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_2.place(x=205, y=100)
    
    ent_3=Entry(cadre, font=("times new roman", 12), width=28, bd=2, relief="solid", bg="#faebd7", show="*")
    ent_3.place(x=205, y=130)
    
    def next_edit_p(id):
        cursor=db.cursor()
        sql="SELECT pass_w FROM utilisateur WHERE id='%s'"%id
        cursor.execute(sql)
        old_p_l=cursor.fetchone()
        old_p_fb=old_p_l[0]
        if old_p_fb==ent_1.get() and ent_2.get()==ent_3.get():
            pass_w=(ent_3.get())
            sql="UPDATE utilisateur SET pass_w='%s' WHERE id='%s'"%(pass_w, id)
            cursor.execute(sql)
            db.commit()
            cadre.pack_forget()
            profil(id)
        else :
            error=messagebox.showwarning("","Faites attention aux mots de passe")
    
    button_1=Button(cadre,text="Envoyer" ,bg="#ffd1aa" ,font=("times new roman", 14) ,bd=3 ,command=lambda id=id : next_edit_p(id), relief="ridge")
    button_1.place(x=270, y=170)

def new_user():
    nom=ent_1.get()
    prenom=ent_2.get()
    pseudo=ent_3.get()
    num=ent_4.get()
    date=ent_5.get()
    pass_w=ent_7.get()
    pass_w=hasher(pass_w)
    #id=0
    check=db.cursor()
    
    sql= "SELECT COUNT(*) FROM utilisateur WHERE nom= '%s' AND prenom= '%s' AND pseudo='%s' AND num='%s' AND date='%s' AND pass_w= '%s' " % (nom, prenom, pseudo, num ,date , pass_w)
    #val=(nom, prenom, num, pass_w)
    check.execute(sql)
    m= check.fetchone()
    nbre_row=m[0]
    
    pseudo_sql="SELECT COUNT(*) FROM utilisateur WHERE pseudo='%s'" %pseudo
    check.execute(pseudo_sql)
    pseudo_contain=check.fetchone()
    if nbre_row==0 :
        cursor=db.cursor()
        sql="INSERT INTO utilisateur (pseudo, nom, prenom, num, date,pass_w) VALUES (%s , %s ,%s ,%s ,%s , %s)"
        val= (pseudo, nom, prenom, num, date, pass_w)
        cursor.execute(sql, val)
        #inscrits()
        #lambda pseudo=pseudo, pass_w=pass_w : check_id(pseudo, pass_w)
        check_id(pseudo, pass_w)

    elif pseudo_contain!=0:
        existant=messagebox.askokcancel("Message","Nom d'utilisateur existant, veillez en choisir un autre")

    else :
        existant=messagebox.askokcancel("Message","Utilisateur existant, veillez vous connecter")
        if existant:
            #cadre.pack_forget()
            home()
            #cadre.pack()

def old_user():
    print(ent_1)
    pseudo=ent_1.get()
    print(pseudo)
    #prenom=ent_2.get()
    #num=ent_3.get()
    #date=ent_4.get()
    pass_w=ent_2.get()
    pass_w=hasher(pass_w)
    check=db.cursor()
    
    sql= "SELECT COUNT(*) FROM utilisateur WHERE pseudo= '%s' AND pass_w= '%s' " % (pseudo, pass_w)
    #val=(nom, prenom, pass_w)
    check.execute(sql)
    m= check.fetchone()
    nbre_row=m[0]
    
    if nbre_row!=0 :
        print(pseudo, pass_w)
        check_id(pseudo, pass_w)
    else :
        inexistant=messagebox.askokcancel("Message","Utilisateur inexistant, veillez vous inscrire \ Identifiants incorrects")
        if inexistant:
            #cadre.pack_forget()
            home()
        else :
            fen.destroy()

def check_id(pseudo, pass_w):
    check=db.cursor()
    sql= "SELECT id FROM utilisateur WHERE pseudo= '%s' AND pass_w= '%s' " % (pseudo, pass_w)
    check.execute(sql)
    id_1=check.fetchone()
    id=id_1[0]
    lambda id=id : profil(id)
    profil(id)

def inscrits():
    global cadre
    global liste
    
    cursor=db.cursor()
    cursor.execute("SELECT nom, prenom, num, date, id FROM utilisateur")
    liste=cursor.fetchall()
    
    cadre=Frame(fen, width= 630, height=10000,bg="silver")
    cadre.pack(expand=1)
        
    title_1=Label(cadre,text="ID", bg="#8D857B", fg="black", width=3)
    title_1.place(x=0,y=0)
        
    title_1=Label(cadre,text="Nom", bg="#8D857B", fg="black", width=12)
    title_1.place(x=20,y=0)
            
    title_1=Label(cadre,text="Prenom", bg="#8D857B", fg="black", width=17)
    title_1.place(x=100,y=0)
        
    title_1=Label(cadre,text="Numero", bg="#8D857B", fg="black", width=10)
    title_1.place(x=220,y=0)
        
    title_1=Label(cadre,text=f"Date\ Naissance", bg="#8D857B", fg="black", width=15)
    title_1.place(x=290,y=0)
        
    action=Label(cadre, text="Actions", bg="#528488", width=34, bd=2, relief="solid")
    action.place(x=390,y=0)
    
    z=0
    for x in liste :
        z+=22
        id=f"{x[4]}"
        id_list=Label(cadre, text=f"{x[4]}", bg="silver", width=2)
        id_list.place(x=0, y=z)
    
        list=Label(cadre,text=f"{x[0]}", bg="silver", fg="black", width=12)
        list.place(x=20,y=z)
    
        list=Label(cadre,text=f"{x[1]}", bg="silver", fg="black", width=10)
        list.place(x=130,y=z)
    
        list=Label(cadre,text=f"{x[2]}", bg="silver", fg="black", width=10)
        list.place(x=220,y=z)
    
        list=Label(cadre,text=f"{x[3]}", bg="silver", fg="black", width=15)
        list.place(x=290,y=z)
            
        edit=Button(cadre, bg="#FFD778", text=f"Modifier {id}", width=10, bd=2, relief="solid", command=lambda id=id: nexx(id))
        edit.place(x=390, y=z)
            
        delete=Button(cadre, bg="#FF5E79", text="Supprimer ", width=10, bd=2, relief="solid", command=lambda id=id: confirm_del(id))
        delete.place(x=550, y=z)

        #delete=Button(cadre, bg="#FF5E79", text="Supprimer ", width=10, bd=2, relief="solid", command=lambda id=id : delete_on(id))
        #delete.place(x=550, y=z)
            
        buy_b=Button(cadre, bg="#FFD778", text="Commander", width=10, bd=2, relief="solid", command=lambda id=id: before_buy(id))
        buy_b.place(x=470, y=z)

def sub():
    global cadre
    global ent_1
    global ent_2
    global ent_3
    global ent_4
    global ent_5
    global ent_6
    global ent_7
    cadre=Frame(fen, width= 485, height= 300,bg="#dbbe92")
    cadre.pack(expand=1)

    fiche_1=Label(cadre, bg="#9BC2E6", font=("Times New Roman",23), text="  INSCRIPTION  ", bd=3,relief="solid")
    fiche_1.place(x=150, y=15)

    lib_1=Label(cadre,text="NOM", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=70)

    lib_1=Label(cadre,text="PRENOM", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=90)
    
    lib_1=Label(cadre,text="Nom d'utilisateur", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=110)

    lib_1=Label(cadre,text="N Telephone", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=130)

    lib_1=Label(cadre,text="DATE DE NAISSANCE", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=150)
    
    lib_1=Label(cadre,text="Mot De Passe", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=170)

    lib_1=Label(cadre,text="Confirmez le Mot De Passe", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=190)

    vari_car="TEST 1st WORD"
    var=StringVar(value=vari_car)

    ent_1=Entry(cadre,textvariable=var, font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_1.place(x=205, y=70)

    ent_2=Entry(cadre, font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_2.place(x=205, y=90)

    ent_3=Entry(cadre, font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_3.place(x=205, y=110)
    
    ent_4=Entry(cadre, font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_4.place(x=205, y=130)
    
    ent_5=DateEntry(cadre, font=("calibri",10), width=25, bd=2,borderwidth=4 , relief="solid", background="#faebd7", foreground='grey')
    ent_5.place(x=205, y=150)
    
    ent_6=Entry(cadre, font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7", show="*")
    ent_6.place(x=205, y=170)
    
    ent_7=Entry(cadre, font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7", show="*")
    ent_7.place(x=205, y=190)

    def next():
        ent1=ent_1.get()
        ent2=ent_2.get()
        ent3=ent_3.get()
        ent4=ent_4.get()
        ent5=ent_5.get()
        ent6=ent_6.get()
        ent7=ent_7.get()
        print(ent6, ent7)
        
        cursor=db.cursor()
        check_pseudo="SELECT COUNT(*) FROM utilisateur WHERE pseudo='%s'"%ent3
        cursor.execute(check_pseudo)
        nbr=cursor.fetchone()
        print(nbr)
        
        if ent1=="" or ent2=="" or ent3=="" or ent4=="" or ent5=="" or ent6=="" or ent7=="":
            error=messagebox.showwarning("","Chaque case est obligatoire !!!")
        
        elif nbr[0]!=0:
            error=messagebox.showwarning("","Nom d'Utilisateur déjà pris !!!")
        
        elif ent6==ent7:
            cadre.pack_forget()
            new_user()
        
        elif ent6!=ent7:
            
            error=messagebox.showwarning("","Les mots de passe ne sont pas identiques")
            
        else:
            print(1)

    confirm=Button(cadre, text=" Inscrire   ", width=30, bd=2, relief="solid", font=("Times new Roman", 16), bg="#7a7a7a", command=next)
    confirm.place(x=60,y=235)

def con():
    global cadre
    global ent_1
    global ent_2
    global ent_3
    global ent_4
    global ent_5
    global ent_7
    cadre=Frame(fen, width= 485, height= 215,bg="#dbbe92")
    cadre.pack(expand=1)

    fiche_1=Label(cadre, bg="#9BC2E6", font=("Times New Roman",23), text="  CONNECTION  ", bd=3,relief="solid")
    fiche_1.place(x=150, y=15)

    lib_1=Label(cadre,text="Nom d'utilisateur", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=70)

    lib_1=Label(cadre,text="Mot de Passe", font=("calibri",10), width=20, bd=2,  bg="#dbbe92")
    lib_1.place(x=60, y=90)

    vari_car="TEST 1st WORD"
    var=StringVar(value=vari_car)

    ent_1=Entry(cadre,textvariable=var, font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7")
    ent_1.place(x=205, y=70)

    ent_2=Entry(cadre, font=("calibri",10), width=28, bd=2, relief="solid", bg="#faebd7", show="*")
    ent_2.place(x=205, y=90)

    def next():
        cadre.pack_forget()
        old_user()

    confirm=Button(cadre, text=" Se Connecter ", width=30, bd=2, relief="solid", font=("Times new Roman", 16), bg="#7a7a7a", command=next)
    confirm.place(x=60,y=165)

def home():
    global cadre
    
    cadre=Frame(fen, width= 450, height= 215,bg="#dbbe92")
    #cadre.place(x=10,y=15)
    cadre.pack(expand=1)
    cadre['relief']=('solid')
        
    fiche_1=Label(cadre, bg="#dbbe92", font=("Times New Roman",29), text="  BIENVENUE  ")
    fiche_1.place(x=90, y=30)
    #fiche_1.pack(expand=1)

    def next_sub():
        cadre.pack_forget()
        sub()

    subscribe=Button(cadre, text=" S'Inscrire ", width=18, bd=2, relief="solid", font=("Times new Roman", 12), bg="#7a7a7a", command=next_sub)
    subscribe.place(x=20,y=130)

    def next_con():
        cadre.pack_forget()
        con()

    connect=Button(cadre, text=" Se Connecter ", width=18, bd=2, relief="solid", font=("Times new Roman", 12), bg="#7a7a7a", command=next_con)
    connect.place(x=270,y=130)

def window():
    global fen
    global cadre
    fen=Tk()
    fen.iconbitmap(icon)
    fen.geometry("800x450")
    fen.title("Gestion")
    fen.minsize(width= 800, height= 380)
    fen['bg']='#b3b3a2'
    #fen['backgroundimage']=icon
    button=Button(fen,text="Retour à l'acceuil" ,command=reset)
    button.pack(padx=10, pady=10,fill='both', side="bottom" )
    home()
#    confirm_passw(id)
    #edit_p(id)
    
    fen.mainloop()

connect=creation_database.database_creator()

window()

"""
import all 

ans=all.somme(2,3)
print(ans)
"""