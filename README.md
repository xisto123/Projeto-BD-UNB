# Projeto de Banco de Dados - Sistema de Apostas
Objetivo do Projeto
Este projeto foi desenvolvido como parte da disciplina de Banco de Dados no curso de Ciência da Computação da Universidade de Brasília. O principal objetivo foi projetar e implementar um banco de dados funcional baseado no tema apostas, atendendo aos requisitos estabelecidos pela docente.

O projeto busca aplicar os conceitos fundamentais de banco de dados relacionais, desde a modelagem até a implementação, garantindo a normalização das tabelas, a realização de operações CRUD e a criação de procedimentos avançados, como views e procedures.

# Funcionalidades
- Modelagem do Banco de Dados: Criação dos modelos de Entidade-Relacionamento (ER) e Relacional utilizando ferramentas de modelagem profissional.
- Persistência de Dados: Implementação de um banco de dados relacional com, no mínimo, 10 entidades, contendo ao menos 5 registros em cada tabela.
- CRUD Completo: Construção de uma aplicação funcional capaz de realizar operações de Create, Read, Update e Delete em pelo menos 3 tabelas com relacionamentos entre elas.

# Recursos Avançados:
- Criação de views para simplificar consultas complexas.
- Implementação de procedures com comandos condicionais.
- Manipulação de dados binários, como imagens ou documentos PDF.

# Como Executar o Projeto
- Clone o repositório:
- git clone [link-do-repositorio]
- Execute os script SQL para criar o banco de dados.
- Execute o arquivo Main.py para a interação com o sistema.
- O Programa permite o CRUD das seguintes Entidades (Usuario, Partida, Aposta).
- CRUD Usuario (Qualquer um tem acesso para realizar).
- CRUD Partida (Apenas o Usuario Administrador pode realizar).
- CRUD Aposta  (Apenas o Usuario Apostador pode para realizar).

# Acessos para Login
- Administrador (cpf: 67890123456 // senha: senha123)
- Apostador (cpf: 01234567890 // senha: senha123)

# Comandos Importantes
- pip install psycopg2-binary ( Para fazer a conexão com o banco )
- pip install Pillow ( Imagens )

# Documentação do Projeto
1. Introdução
O Sistema de Apostas é uma aplicação que permite aos usuários realizarem apostas em partidas esportivas, 
gerenciando competições, eventos esportivos, carteiras financeiras e transações de apostas. 
O projeto utiliza uma arquitetura baseada em camadas e um banco de dados relacional PostgreSQL.

2. Estrutura do Projeto
Database/: Contém scripts SQL para criação de tabelas, triggers, procedures, views e inserts, bem como a configuração de conexão com o banco de dados.
Enums/: Define enumerações usadas no projeto, como tipos de status e categorias.
Interfaces/: Contém as interfaces gráficas para interação do usuário.
Models/: Contém o mapeamento das entidades do Bando de Dados.
Services/: Implementa a lógica de negócio e manipulação dos dados.
main.py: Ponto de entrada do sistema.
README.md: Documentação geral do projeto.