print ('Bem vindo ao Gerenciador de tarefas')
print (''' 
    1 - CRIAR ATIVIDADES
    2 - ATUALIZAR ATIVIDADES
    3 - EXCLUIR UMA ATIVIDADE OU TODAS
    4 - LISTAR TODAS AS TAREFAS DE UM DIA
    5 - LISTAR TODAS AS CATEGORIAS
    6 - CRIAR UMA CATEGORIA
    7 - ATUALIZAR UMA CATEGORIA
    8 - EXCLUIR UMA CATEGORIA OU TODAS
    9 - MARCAR UMA TAREFA COMO CONCLUIDA
    ''')

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    from atividades import cria_tarefa
    categoria_id = int(input('Qual o ID da categoria? '))
    descricao = input('Digite a descrição da tarefa:  ')    
    data = input ('Qual a data da atividade? (dd/mm/aaaa) ')
    hora = input ('Qual o horario da tarefa? (hh:mm) ')
    concluida = input('Tarefa concluída? (S/N)' ) 
    valores = [categoria_id,descricao,data,hora,concluida] 
    tarefa_agendada = cria_tarefa (valores)

    print (tarefa_agendada)

   
if opcao == 2:
    from atividades import atualiza_tarefa
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'select * from tarefa'
    tarefas = cursor.execute(sql)

    print ('Tarefas criadas: ')
    for tarefa in tarefas:
        print ('ID:', tarefa [0], 'Categoria ID:' , tarefa [1], 'Descrição: ', tarefa [2],'Data: ', tarefa[3],
        'Hora: ', tarefa [4],'Concluída: ', tarefa [5])
    tarefa_id = int (input('Qual o ID da tarefa que deseja atualizar? '))
    nova_categoria_id = int (input('Qual o id da categoria? '))
    nova_descricao = (input('Digite a nova descrição: '))
    nova_data = input('Qual a nova data?  (dd/mm/aaaa)')
    nova_hora = input('Qual a nova hora? (hh:mm)')
    conclusão = input('A Tarefa foi concluida? (S/N)')
    valores = [nova_categoria_id, nova_descricao, nova_data,nova_hora, conclusão, tarefa_id]
    atualiza_atividades = atualiza_tarefa(valores)

    print (atualiza_atividades)

if opcao == 3:
    opcao_1 = input('Deseja apagar todas as atividades? (S/N)')

    if opcao_1 == 'S' or opcao_1 == 's':
        import sqlite3
        conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
        cursor = conexao.cursor()
        print('WARNING!!!! Ação irreversível após a conclusão')
        sql = 'delete from tarefa'
        cursor.execute (sql)
        conexao.commit()
        conexao.close()

        print('Tarefas apagadas com sucesso!!!')
    
    if opcao_1 == 'N' or 'n':
        from atividades import deleta_tarefa
        import sqlite3
        conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
        cursor = conexao.cursor()
        sql = 'select * from tarefa'
        tarefas = cursor.execute(sql)
        print ('Tarefas criadas: ')
        for tarefa in tarefas:
            print ('ID:', tarefa [0], 'Categoria ID:' , tarefa [1], 'Descrição: ', tarefa [2],'Data: ', tarefa[3],
            'Hora: ', tarefa [4],'Concluída: ', tarefa [5])
    tarefa_id = int (input('Qual o ID da tarefa que deseja deletar? '))
    valor = [tarefa_id] 
    deleta_atividade = deleta_tarefa(valor)

    print (deleta_atividade)

   
if opcao == 4: 
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    data_tarefa = [input('Qual a data você deseja listar as tarefas? ')]
    sql = '''
    select t.id, c.nome_categoria, t.descricao, t.data, t.hora, t.concluida as categorias from tarefa as t, 
    categorias as c where t.categoria_id = c.id and data == ?    
    '''
    tarefas = cursor.execute(sql, data_tarefa)
    print ('Tarefas criadas: ')
    for tarefa in tarefas:
        print ('ID:', tarefa [0], 'Categoria:', tarefa [1], 'Descrição: ', tarefa [2], 'Data: ', tarefa[3],
        'Hora: ', tarefa [4], 'Concluída: ', tarefa [5] )
    conexao.commit()
    conexao.close()

if opcao == 5:
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'select * from categorias'
    categorias = cursor.execute(sql)
    print ('Categorias criadas: ')
    for categoria in categorias:
        print ('ID:', categoria [0], 'Descrição: ',categoria[1])
    conexao.commit()
    conexao.close()
    
if opcao == 6:
    from categorias import cria_categoria
    descricao = input('Digite a descrição da categoria:  ')
    valor = [descricao]
    categoria_criada = cria_categoria(valor)
    print (categoria_criada)

if opcao == 7:
    from categorias import atualiza_categoria
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'select * from categorias'
    categoria = cursor.execute(sql)

    print ('Categorias criadas: ')
    for categorias in categoria:
        print ('ID:', categorias [0],'Descrição: ', categorias [1])

    categoria_id = int (input('Qual o id da categoria que deseja atualizar? '))
    nova_descricao = input ('Qual a nova descrição da categoria? ')
    
    valor = [nova_descricao, categoria_id]
    categoria_atualizada = atualiza_categoria(valor)

    print (categoria_atualizada)
    
if opcao == 8:
    opcao_1 = input('Deseja apagar todas as categorias? (S/N)')

    if opcao_1 == 'S' or opcao_1 == 's':
        import sqlite3
        conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
        cursor = conexao.cursor()
        print('WARNING!!!! Ação irreversível após a conclusão')
        sql = 'delete from categorias'
        cursor.execute (sql)
        conexao.commit()
        conexao.close()

        print('Categorias apagadas com sucesso!!!')

    if opcao_1 == 'N' or opcao_1 == 'n':
        from categorias import deleta_categoria
        import sqlite3
        conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
        cursor = conexao.cursor()
        sql = 'select * from categorias'
        categoria = cursor.execute(sql)

        print ('Categorias criadas: ')
        for categorias in categoria:
            print ('ID:', categorias [0],'Descrição: ', categorias [1])

        categoria_id = int (input('Qual o id da categoria que deseja deletar? '))
    
        valor = [categoria_id]
        categoria_deletada = deleta_categoria(valor)

        print (categoria_deletada)


if opcao == 9: 
    from atividades import concluir_tarefas
    import sqlite3
    conexao = sqlite3.connect ('gerenciador_tarefas.sqlite3')
    cursor = conexao.cursor()
    sql = 'select * from tarefa'
    tarefas = cursor.execute(sql)

    print ('Tarefas criadas: ')
    for tarefa in tarefas:
        print ('ID:', tarefa [0], 'Categoria ID:' , tarefa [1], 'Descrição: ', tarefa [2],'Data: ', tarefa[3],
        'Hora: ', tarefa [4],'Concluída: ', tarefa [5])
    tarefa_id = int (input('Qual o ID da tarefa que deseja marcar como concluida? '))
    valor = [tarefa_id]

    conclusao = concluir_tarefas (valor)

    print (conclusao)





    
    

