Disciplina: Programação I – Python
Tema: Estruturas de Repetição e Estruturas de Dados

⸻

🧩 Projeto 1 – Sistema de Cadastro de Produtos (Mini Controle de Estoque)

📘 Contexto

Uma pequena loja precisa informatizar o controle de seus produtos. O sistema permite cadastrar, listar, buscar, atualizar e excluir produtos do estoque.

⚙️ Funcionalidades
	•	Cadastrar novos produtos
	•	Listar todos os produtos
	•	Buscar produto pelo código
	•	Atualizar informações (preço, nome, quantidade etc.)
	•	Excluir produto
	•	Sair do sistema

🧱 Estrutura de dados usada
	•	Lista → armazena todos os produtos
	•	Dicionário → cada produto tem as chaves:
{"codigo": 101, "nome": "Arroz", "preco": 7.99, "quantidade": 10}
	•	Set → controla os códigos já cadastrados (evita duplicatas)
	•	Tupla → armazena as categorias disponíveis (ex: ("Alimentos", "Limpeza", "Bebidas"))
  
  🎓 Projeto 2 – Sistema de Controle de Alunos e Notas

📘 Contexto

Uma escola deseja automatizar o registro de alunos, notas e médias para facilitar a consulta do desempenho da turma.

⚙️ Funcionalidades
	•	Cadastrar aluno
	•	Registrar notas
	•	Listar alunos e médias
	•	Buscar aluno específico
	•	Mostrar aprovados e reprovados
	•	Gerar relatórios

🧱 Estrutura de dados usada
	•	Dicionário principal: guarda os alunos e suas notas
  •	Listas temporárias: usadas para registrar notas antes de transformá-las em tuplas
	•	Sets: controlam alunos já cadastrados (sem duplicatas)
	•	Loops: percorrem as estruturas e calculam médias
  💾 Entrega
	•	Arquivos principais:
	•	projeto1.py
	•	projeto2.py
	•	Arquivo de documentação:
	•	README.md (este arquivo)

⸻

👨‍💻 Observações
	•	Foram utilizadas estruturas de repetição (while, for) e validação de entradas incorretas.
	•	O projeto foi feito com foco em praticar lógica e organização de dados em Python.
