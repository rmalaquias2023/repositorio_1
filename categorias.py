def cria_categoria (valor):
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'insert into categorias (nome_categoria) values (?)'
    cursor.execute (sql, valor)
    conexao.commit ()
    conexao.close()
    mensagem = 'Categoria criada com sucesso!!!'    
    return mensagem

def atualiza_categoria (valor):
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'update tarefa set descricao = ?, where id = ?'
    cursor.execute (sql, valor)
    conexao.commit()
    conexao.close()
    mensagem = 'Categoria atualizada com sucesso!!! '
    return mensagem

def deleta_categoria (valor):
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'delete from categorias where id = ?'
    cursor.execute(sql,valor)
    conexao.commit()
    conexao.close()
    mensagem = 'Categoria apagada com sucesso!!! '
    return mensagem
   