import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()


    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()


    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

    def buscar(self, valor):
        consulta2 = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta2, (f'%{valor}%',))
        #qualquer coisa para cá ou qualquer coisa para lá

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')
    agenda.inserir('Luis Otávio', '1111112')
    agenda.inserir('Rose Luisa', '1111211')
    agenda.inserir('Guilherme meio do caminho Luis', '1211111')
    agenda.inserir('Vivi', '1111311')
    agenda.listar()
    agenda.editar('Francisco','134576', 1)
    agenda.excluir(5)
    agenda.buscar('Luis')
    agenda.listar()
