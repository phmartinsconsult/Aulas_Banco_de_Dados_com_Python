
# CRUDE = CREATE, READ, UPDATE, DELETE
# PROCEDIMENTOS QUE PODEMOS FAZER COM UM BANCO DE DADOS

import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    # Conectar-se ao servidor(e às tabelas do banco de dados).
    conexao = pymysql.connect\
            (
        host='127.0.0.1',
        user='root',
        password='ph173846',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
        )

    try:
        yield conexao
    finally:
        print('Conexão fechada')
        conexao.close()



#INSERIR 1 INFORMAÇÃO NOVA NO BANCO DE DADOS
#with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#              '(%s, %s, %s, %s)'
#        cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#        conexao.commit()

# INSERIR MUITAS INFORMAÇÕES DE UMA SÓ VEZ
#with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES' \
#              '(%s, %s, %s, %s)'
#        dados = [
#            ('MURIEL', 'FIGUEIREDO', 19, 55),
#            ('ROSE', 'FIGUEIREDO', 19, 55),
#            ('JOSE', 'FIGUEIREDO', 19, 55)
#        ]

#        cursor.executemany(sql, dados)
#        conexao.commit()

# APAGAR UM DOS REGISTROS
#with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'DELETE FROM clientes WHERE id=%s'
#        cursor.execute(sql, (6,))
#        conexao.commit()

# APAGAR VÁRIOS REGISTROS
#with conecta() as conexao:
#    with conexao.cursor() as cursor:
#        sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#        cursor.execute(sql, (7,8,9))
#        conexao.commit()

#ATUALIZAR UM REGISTRO
with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('JOANA',5))
        conexao.commit()



# SELECIONA OS DADOS DA BASE DE DADOS
# Esse é um Gerenciador de Contexto
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id DESC LIMIT 100')
        resultado = cursor.fetchall()

        for linha in resultado:
            print(linha)



