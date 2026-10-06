#REGRAS DO PROJETO
##ARQUITETURA:
-o projeto consiste de uma interface com pyside6 e QT
-a interface consiste principalmente de suas tab de um tabWidget, uma é usa para inserir os campos de dados e a outra mostra eles em uma tabela, analise os arquivos para compreender melhor
-o sistema usa o requests para buscar cnpj's em uma api da receita federal, para realizar um auto complete no campo nos outros campos
-quando o botão adicionar é clickado, ele pega os textos dos campos da interface para inseri-los num banco mysql Workbanch
-quando o programa é iniciado ele pega os registros do banco de dados para mostra-los na interface
-o programa possui todo CRUD principal junto a uma opção de exportar os registros que aparecem na interface para excel
##REGRAS:
-se for fazer alterações peça minha permissão
-se for baixar bibliotecas peça minha permissão
-o programa usa venv para baixar as dependencias
-o programa guarda as imagens usadas na interface na pasta imgs, e os arquivos excel na pasta arquivosExcel
##OUTRAS INFORMAÇÕES:
-o programa é de iniciativa didática, porém possui foco em projeto aplicados na vida real, então considere isso como um complemento em meu portfólio dev
-o projeto já está upado no github, com os devidos cuidados com o requirements.txt e o .gitignore ignorando o venv e outros arquivos
-de ideias do que adicionar ao projeto, isto considera formas de deixar o código mais enxuto, sugestões de praticidade ou segurança, também planejo usar um tempo para analisar o nome de variaveis, funcoes, classes, etc. Visando melhorar a minha ideia de boas práticas

##HISTÓRICO DE ALTERAÇÕES:
###[06/10/2026] - Limpeza, nomes PEP8 e correções de UX (tópicos 14-18 do importante.txt)
-.gitignore: removidos `ui_main.py`, `myrecursos_rc.py` e `agents.md` — os dois primeiros são gerados a partir de main_window.ui (pyside6-uic / pyside6-rcc) e precisam ir pro GitHub para um clone limpo rodar; o terceiro estava errado (o arquivo real é AGENTS.md maiúsculo, e no Windows o gitignore sem caixa também escondia o AGENTS.md correto)
-database.py: `acess` renomeado para `acesso` (PEP8); removido o método `disconnect`, que nunca era chamado (código morto)
-requisicoes.py: `requestCNPJ` renomeado para `request_cnpj` (PEP8)
-main.py: `insert_qtrows` renomeado para `insert_qt_rows` (PEP8); `requestCNPJ` atualizado na importação e na chamada
-main.py: `alterar_nome_empresa` agora passa o texto por `html.escape()` antes de injetar no HTML do QLabel — digitar `<` ou `&` não quebra mais o rich text
-main.py: removido o comentário morto no final do arquivo (linha que referenciava tabWidget.currentWidget sem parênteses)
-para regenerar os arquivos de UI após mudar main_window.ui: `pyside6-uic main_window.ui -o ui_main.py` e `pyside6-rcc main_window.ui -o myrecursos_rc.py` (confirmar o caminho do .qrc se necessário)
###[26/10/2026] - CRUD finalizado (função update)
-o CRUD principal (Create, Read, Update, Delete) está completo; o que faltava era o update, implementado com o botão "Alterar" que lê as células editadas da Table e persiste no MySQL
-database.py: a função update_empresa foi reescrita porque a versão anterior montava um SQL inválido (`update empresa set %s where cnpj = %s`); agora monta a cláusula SET dinamicamente a partir de um dicionário e o where continua parametrizado. os métodos da camada de dados passaram a retornar True/False para a interface saber se pode confirmar a alteração na tela. o parâmetro antes chamado `id` foi renomeado para `cnpj` em update_empresa e delete_empresa, pois `id` sombreia o built-in
-main.py: criada a constante global CAMPOS com os nomes das colunas do banco, alinhada com a ordem das colunas da Table (confirmado com SHOW COLUMNS na tabela empresa)
-main.py: a função insert_qtrows passou a receber *valores e preencher as células em loop, eliminando as 11 linhas repetidas de setItem. cada QTableWidgetItem guarda uma cópia do valor original em Qt.UserRole, que é a base da lógica de update: o UserRole é o valor "original" e o text() é o valor editado; a coluna 0 (cnpj) fica somente leitura para ninguém alterar a chave
-main.py: a função alter_database só envia ao banco os campos que realmente mudaram, usando o cnpj original guardado no UserRole como cláusula where. o UserRole só é atualizado depois que o banco confirma a alteração, evitando reenvios desnecessários
-main.py: show_registers_from_database agora limpa a tabela com setRowCount(0) antes de popular, corrigindo linhas duplicadas (ela é chamada no __init__ e também via currentChanged do tabWidget)
-main.py: delete_row recebeu guarda para quando não há linha selecionada (currentRow() == -1), que quebrava em self.table.item(-1, 0).text()
-convenção importante do projeto: os métodos de database.py já usam parâmetros nomeados com %s, nunca concatenar valores na query. colunas dinâmicas (do SET) são o único ponto onde há interpolação de string, e apenas com crase para evitar conflito com palavras reservadas
-ponto em aberto: os headers da Table continuam vazios no main_window.ui, então a exportação para Excel gera "Coluna 0" até "Coluna 10". com a constante CAMPOS existente, basta um self.ui.Table.setHorizontalHeaderLabels(list(CAMPOS)) no __init__ para resolver
-validações feitas em 26/10/2026: o UPDATE foi testado de verdade no MySQL dentro de uma transação com rollback (resultado idêntico ao esperado, zero linhas residuais), e a parte Qt foi testada com um banco stub cobrindo coluna 0 read-only, clique sem alteração não chamar o banco, diff correto dos campos, reenvio evitado, snapshot preservado quando o banco falha e delete sem seleção
