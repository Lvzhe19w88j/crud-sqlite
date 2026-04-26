import sqlite3

conn = sqlite3.connect('entrada_dados_while/datebase.db')
cursor = conn.cursor()

def criar_tabela():
        cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER
            )
        """
    )
        
criar_tabela()

def criar():
    nome = input("digite seu nome:")
    try:
        idade = int(input("digite sua idade: "))
    except ValueError:
         print("este campo aceita apenaas numeros!" )
         return
    
    cursor.execute(
         """
                INSERT INTO usuarios (nome, idade)
                VALUES (?, ?)
        """, (nome, idade,))
    conn.commit()

def listar():
     cursor.execute(
          "SELECT * FROM usuarios"
     )

     dados = cursor.fetchall()
     
     for d in dados:
          print(d)

def buscar():
     nome = input("digite o nome: ")
     
     cursor.execute(
        """
                SELECT * FROM usuarios 
                WHERE nome 
                LIKE ?
        """, (f"%{nome}%",))
     
     dados = cursor.fetchall()
     for d in dados:
          print(d)

def editar():
     try:
        id_user = int(input("digite o id do usuario: "))
     except ValueError:
          print("id errado tente novamente!")
          return
     
     nv_nome = input("digite seu novo nome: ")

     try:
        nv_idade = int(input("digite sua nova idade: "))
     except ValueError:
          print("este campo recebe apenas numeros!")
          return
         
     cursor.execute(
        """
            UPDATE usuarios 
            SET nome = ?, idade = ?
            WHERE id = ?
        """,
            (
                 nv_nome,
                 nv_idade,
                 id_user
            )
        )

def deletar():
     id_user = int(input("digite o id: "))

     cursor.execute(
        """
            DELETE FROM usuarios
            WHERE id = ?
        """, (id_user,))
     conn.commit()

while True:

    print("--- MENU ---")
    print("1- adicionar")
    print("2- listar")
    print("3- buscar usuario")
    print("4- editar usuario")
    print("5- deletar usuario")
    print("6- sair")

    try:
        escolha = int(input("Escolha: "))
    except ValueError:
         print("digite apenas numeros!")
         continue
    
    if escolha == 1:
        criar()
    elif escolha == 2:
        listar()
    elif escolha == 3:
         buscar()
    elif escolha == 4:
         editar()
    elif escolha == 5:
         deletar()
    elif escolha == 6:
        print("saindo...")
        conn.commit()
        conn.close()
        break
    else:
        print("tente novamente...")
