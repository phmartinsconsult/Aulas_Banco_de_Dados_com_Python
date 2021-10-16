import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()


# Execute = executa comandos no no meu banco de dados
# Criando uma tabela
cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
               'id INTEGER PRIMARY KEY AUTOINCREMENT,'
               'nome TEXT,'
               'peso REAL'
               ')')

#cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?,?)', ('Luis Otavio', 80.5))
cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?,?)', ('Maria', 50))
cursor.execute(
    'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
    {'nome':'Joãozinho', 'peso': 25}
)
cursor.execute(
    'INSERT INTO clientes VALUES (:id, :nome, :peso)',
    {'id': None, 'nome': 'Daniel', 'peso': 113}
)


conexao.commit() # Dizendo para ele inserir essa linha


#cursor.execute(
#    'DELETE clientes SET nome=:nome WHERE id=:id'
#    {'nome': 'Joana', 'id': 2}
#)

cursor.execute(
    'UPDATE clientes SET nome=:nome WHERE id=:id'
    {'nome': 'Joana', 'id': 2}
)

cursor.execute('SELECT * FROM clientes')
# cursor.execute('SELECT nome, peso FROM clientes WHERE peso > 50')

#cursor.fetchall()
#Esse método vai lá no DB e busca todos os valores para mim.

for line in cursor.fetchall():
    identificador, nome, peso = line

    print(identificador, nome, peso)

cursor.close()
conexao.close()
