def cria_tarefa (valores):
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'insert into tarefa (categoria_id, descricao, data, hora, concluida) values (?,?,?,?,?)'
    cursor.execute (sql, valores)
    conexao.commit()
    conexao.close()

    mensagem = 'Tarefa agendada com sucesso'
    return mensagem
    

def atualiza_tarefa (valores):
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'update tarefa set categoria_id = ?, descricao = ?, data = ?, hora = ?, concluida = ?  where id = ?'
    cursor.execute (sql, valores)
    conexao.commit()
    conexao.close()
    mensagem = 'Tarefa atualizada com sucesso'
    return mensagem


def deleta_tarefa (valor):
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'delete from tarefa where id = ?'
    cursor.execute(sql,valor)
    conexao.commit()
    conexao.close()
    mensagem = 'Atividade deletada com sucesso!!' 
    return mensagem
    

def concluir_tarefas (valor):
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'update tarefa set concluida = "S" where id = ?'
    cursor.execute(sql,valor)
    conexao.commit()
    conexao.close()

    mensagem = 'Tarefa concluida com sucesso'
    return mensagem


    

 