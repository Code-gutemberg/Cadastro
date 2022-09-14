### Resumo versão 1.4:

Traduzir do português brasileiro para o inglês técnico as funções e variáveis do programa. Tornar o README em Português e Inglês e outras modificações.

**Escopo para versão 1.4:**

- [x] Tradução:
    - [x] Traduzir as funções.
    - [x] Traduzir as variáveis.
    - [x] Incluir o Inglês técnico nas versões anteriores.
- [x] Outras Modificações.
    - [x] Criar outro módulo chamado treatment para tratar entrada de dados pelo usuário.
    - [x] Inserir funções de acordo com o módulo criado.
    - [x] Otimizar código escrito anteriormente.
    - [x] Remover o tratamento de CPF e CNPJ nas funções query do módulo data para o módulo treatment.
    - [x] Criar função chamada read_cpf e read_cnpj no módulo treatment para fazer tratamento de entrada.
    - [x] Criar Função para substituição da biblioteca Random() para gerar id de forma sequencial.
    - [x] Otimizar as funções de leitura e gravação dos arquivos txt.
    - [x] Remover a colorização com códigos ANSCI do programa.
    - [x] informar o usuário logado no programa.
    - [x] Inserir Tags de erro e sucesso: [ERROR], [SUCESS].
    - [x] Inserir função para tratamento de CPF e CNPJ com a técnica expressão regular.
    - [x] Restringir o programa de acordo com o nível do usuário: Visitante e Super Usuário.



# English translation

### Summary version 1.4:

Translate from Brazilian Portuguese to technical English the program functions and variables. Make the README in Portuguese and English and other modifications.

**Scope for version 1.4:**

- [x] Translation:
     - [x] Translate the functions.
     - [x] Translate the variables.
     - [x] Include technical English in previous versions.
- [x] Other Modifications.
     - [x] Create another module called treatment to handle user input.
     - [x] Insert functions according to the created module.
     - [x] Optimize previously written code.
     - [x] Remove the treatment of CPF and CNPJ in the query functions of the data module for the treatment module.
     - [x] Create function called read_cpf and read_cnpj in the treatment module to handle input.
     - [x] Create Function to replace the Random() library to generate id sequentially.
     - [x] Optimize the functions of reading and writing txt files.
     - [x] Remove colorization with ANSCI codes from the program.
     - [x] inform the user logged into the program.
     - [x] Insert Error and Success Tags: [ERROR], [SUCESS].
     - [x] function for treatment CPF and CNPJ with the regular technical expression.
     - [x] Restrict the program according to user level: Guest and Super User.


---


### Resumo versão 1.3:

Modificar a __*versão 1.2*__ e criar funções QUERY de dados dos bancos.txt a partir da função ler_db.

**Escopo para versão 1.3:**

- [x] Modificações:
    - [x] Criar função para questionar os dados dos bancos.
    - [x] Modificar menu Proposta de Crédito.
        - [x] Criar sistemática de consulta por CPF.
        - [x] Caso CPF inexistente: iniciar cadastro de usuário.
        - [x] Caso CPF existente: iniciar análise de proposta.
            - [x] Criar regras de proposta de crédito.
        - [x] Criar sistemática de consulta por CNPJ.
        - [x] Caso CNPJ inexistente: iniciar cadastro de empresa.
        - [x] Caso CNPJ existente: iniciar análise de proposta.
            - [x] Criar regras de proposta de crédito.
    - [x] Modificar menu Cadastrar Usuário.
        - [x] Criar sistemática de consulta por CPF.
        - [x] Caso CPF inexistente: iniciar cadastro de usuário. 
        - [x] Caso CPF existente: informar que já existe.
        - [x] Criar sistemática de consulta por CNPJ.
        - [x] Caso CNPJ inexistente: iniciar cadastro da empresa. 
        - [x] Caso CNPJ existente: informar que já existe.
    - [x] Modificar menu Remover Usuário.
        - [x] Criar sistemática de consulta por CPF.
        - [x] Caso CPF inexistente: informar que usuário não existe. 
        - [x] Caso CPF existente: informar mensagem de confirmação.
            - [x] Caso resposta sim: remover usuário do banco de dados.
        - [x] Criar sistemática de consulta por CNPJ.
        - [x] Caso CNPJ inexistente: informar que a empresa não existe. 
        - [x] Caso CNPJ existente: informar mensagem de confirmação.
            - [x] Caso resposta sim: remover usuário do banco de dados.
    - [x] Criar Autenticação de usuário root e senha.
        - [x] Criar Banco de dados txt para usuário root.
        - [x] Criar função para autenticação de usuário root e senha.
        - [x] Modificar programa para aceitar só usuários permitidos.

**Técnicas utilizadas:**

* importações de bibliotecas
* modularização
* condicionais
* loops While e For
* colorização com códigos ANSCI
* leitura e gravação de arquivos txt
* Funções
* Tratamento de erros Try, except, else, Finally
* Dicionário
* Lista
* Cálculos de juros simples

**Telas do Programa:**

[Tela autenticação](https://user-images.githubusercontent.com/109303611/185231467-c81c9810-74c7-49d7-94cb-25142aaafb6c.JPG)

[Tela Emprestimo Pessoa Física](https://user-images.githubusercontent.com/109303611/185231567-959b8219-5d92-42ba-b056-e33c78394631.JPG)

[Tela Emprestimo Pessoa Jurídica](https://user-images.githubusercontent.com/109303611/185231653-95ce425a-b21e-4218-afc9-7cb9892aa89d.JPG)

[Tela de Consulta Por CPF/CNPJ](https://user-images.githubusercontent.com/109303611/185231725-32fe6d70-211c-48ab-a269-32aacab761b4.JPG)


# English translation

### Summary version 1.3:

Modify __*version 1.2*__ and create QUERY functions from databases.txt from the function read_db.

**Scope for version 1.3:**

- [x] Modifications:
    - [x] Create a function to query bank data.
    - [x] Modify Credit Proposal menu.
        - [x] Create a consultation system by CPF.
        - [x] If CPF does not exist: start user registration.
        - [x] If CPF exists: start analysis of proposal.
            - [x] Create credit proposal rules.
        - [x] Create a consultation system by CNPJ.
        - [x] If CNPJ does not exist: start company registration.
        - [x] Existing CNPJ case: start proposal analysis.
            - [x] Create credit proposal rules.
    - [x] Modify the Register User menu.
        - [x] Create a consultation system by CPF.
        - [x] If CPF does not exist: start user registration.
        - [x] If CPF exists: inform that it already exists.
        - [x] Create a consultation system by CNPJ.
        - [x] If CNPJ does not exist: start company registration.
        - [x] If existing CNPJ: inform that it already exists.
    - [x] Modify menu Remove User.
        - [x] Create a consultation system by CPF.
        - [x] If CPF does not exist: inform that the user does not exist.
        - [x] If CPF exists: inform confirmation message.
            - [x] If yes: remove user from database.
        - [x] Create a consultation system by CNPJ.
        - [x] If CNPJ does not exist: inform that the company does not exist.
        - [x] If existing CNPJ: inform confirmation message.
            - [x] If yes: remove user from database.
    - [x] Create Root User Authentication and Password.
        - [x] Create txt database for root user.
        - [x] Create role for root user authentication and password.
        - [x] Modify program to accept only allowed users.

**Techniques used:**

* library imports
* modularization
* conditionals
* While and For loops
* colorization with ANSCI codes
* reading and writing txt files
* Functions
* Try, except, else, Finally error handling
* Dictionary
* List
* Simple interest calculations

**Program Screens:**

[Authentication screen](https://user-images.githubusercontent.com/109303611/185231467-c81c9810-74c7-49d7-94cb-25142aaafb6c.JPG)

[Individual Loan Screen](https://user-images.githubusercontent.com/109303611/185231567-959b8219-5d92-42ba-b056-e33c78394631.JPG)

[Corporate Loan Screen](https://user-images.githubusercontent.com/109303611/185231653-95ce425a-b21e-4218-afc9-7cb9892aa89d.JPG)

[Inquiry Screen By CPF/CNPJ](https://user-images.githubusercontent.com/109303611/185231725-32fe6d70-211c-48ab-a269-32aacab761b4.JPG)


___


### Resumo versão 1.2:

Modificar a __*versão 1.1*__ e melhorar o sistema de análise de crédito.

**Escopo para versão 1.2:**

- [x] Modificações:
    - [x] Alterar a moeda de saída para Real Brasileiro ignorando a pontuação padrão do python.
    - [x] Cadastrar o ID de usuários ao banco de dados pela com números aleatórios com a biblioteca random() para manipulação futura.
    - [x] Alterar o nome do menu Cadastrar para Cadastrar Usuário.
    - [x] Alterar o nome do menu Banco de Dados para Consultar Usuário.
    - [x] Criar um menu para remover usuários cadastrados.
    - [x] Otimizar funções.
    - [x] Alterar as ordens do Menu Principal.
        - [x] 1 para Proposta de Crédito.
        - [x] 2 para Cadastrar Usuário.
        - [x] 3 para Remover Usuário.
        - [x] 4 para Sair do Sistema.
    - [x] Alterar a sistemática de consultar usuários no menu. Inserindo dentro do menu Proposta de Crédito e Remover Usuário.

**Técnicas utilizadas:**

* importações de bibliotecas
* modularização
* condicionais
* loops While e For
* colorização com códigos ANSCI
* leitura e gravação de arquivos txt
* Funções
* Tratamento de erros Try, except, else, Finally
* Dicionário
* Lista

**Telas do Programa:**

[Tela Principal](https://user-images.githubusercontent.com/109303611/183923377-df639a48-7412-4868-ad3a-cb071c113737.JPG)

[Tela Proposta de Crédito](https://user-images.githubusercontent.com/109303611/183923474-acabc12a-b057-4951-9d29-c95e50639949.JPG)

[Tela Consulta de usuario dentro de Proposta de Crédito](https://user-images.githubusercontent.com/109303611/183923625-bc3c4db1-568d-4aa5-ad1d-52ca91cf2f26.JPG)

[Tela de Remover Usuário](https://user-images.githubusercontent.com/109303611/183923752-3098e190-ffbb-43cf-9b05-5c82d5ef4dd7.JPG)

[Tela Consulta de usuario dentro de Remover Usuario](https://user-images.githubusercontent.com/109303611/183923845-93024dab-c60a-4044-9266-8213af62fe01.JPG)


# English translation

### Summary version 1.2:

Modify __*version 1.1*__ and improve the credit analysis system.

**Scope for version 1.2:**

- [x] Modifications:
    - [x] Change the output currency to Brazilian Real ignoring the default python punctuation.
    - [x] Register the user ID to the database by using random numbers with the random() library for future manipulation.
    - [x] Change the name of the Register menu to Register User.
    - [x] Change the name of the Database menu to Query User.
    - [x] Create a menu to remove registered users.
    - [x] Optimize functions.
    - [x] Change Main Menu orders.
        - [x] 1 for Credit Proposal.
        - [x] 2 to Register User.
        - [x] 3 for Remove User.
        - [x] 4 for Exit System.
    - [x] Change the method of consulting users in the menu. Inserting into the menu Credit Proposal and Remove User.

**Techniques used:**

* library imports
* modularization
* conditionals
* While and For loops
* colorization with ANSCI codes
* reading and writing txt files
* Functions
* Try, except, else, Finally error handling
* Dictionary
* List

**Program Screens:**

[Main Screen](https://user-images.githubusercontent.com/109303611/183923377-df639a48-7412-4868-ad3a-cb071c113737.JPG)

[Credit Proposal Screen](https://user-images.githubusercontent.com/109303611/183923474-acabc12a-b057-4951-9d29-c95e50639949.JPG)

[User Inquiry screen within Credit Proposal](https://user-images.githubusercontent.com/109303611/183923625-bc3c4db1-568d-4aa5-ad1d-52ca91cf2f26.JPG)

[Remove User Screen](https://user-images.githubusercontent.com/109303611/183923752-3098e190-ffbb-43cf-9b05-5c82d5ef4dd7.JPG)

[User Query screen inside Remove User](https://user-images.githubusercontent.com/109303611/183923845-93024dab-c60a-4044-9266-8213af62fe01.JPG)


___


### Resumo versão 1.1:

Modificar a __*versão 1.0*__ para sistema de análise de crédito de pessoa física e pessoa jurídica.

**Escopo para versão 1.1:**

- [x] Modificações
    - [x] Alterar o nome da opção 01 e 02
    - [x] Incluir nome do sistema acima do Menu Principal
    - [x] Alterar menu de pessoas cadastradas
    - [x] Alterar menu de cadastro
        
- [x] Cadastro de Pessoa Física
    - [x] Cadastro de CPF
    - [x] Melhora do cadastro de idade
    - [x] Cadastro de Renda Liquida

- [x] Cadastro de Pessoa Jurídica
    - [x] Cadastro Nome da Empresa
    - [x] Cadastro de CNPJ
    - [x] Cadastro de Porte da empresa
    - [x] Cadastro do Capital imobilizado
    - [x] Cadastro do Fluxo de caixa dos últimos 3 meses
    - [x] Cadastro do D.R.E do último ano

- [x] Cadastro de Menu Proposta de crédito
    - [x] Análise Pessoa física
    - [x] Análise Pessoa Jurídica

**Técnicas utilizadas:**

* importações de bibliotecas
* modularização
* condicionais
* loops While e For
* colorização com códigos ANSCI
* leitura e gravação de arquivos txt
* Funções
* Tratamento de erros Try, except, else, Finally
* Dicionário
* Lista

**Telas do Programa:**

[Tela Principal](https://user-images.githubusercontent.com/109303611/183444915-c5446a8f-d05c-4f4d-a1f5-97349923137d.JPG)

[Tela Banco de Dados Pessoa fisica](https://user-images.githubusercontent.com/109303611/183444934-cd663dc5-8add-4897-be1e-d7ff03238900.JPG)

[Tela Banco de Dados Pessoa jurídica](https://user-images.githubusercontent.com/109303611/183444968-366dcbc2-9afc-48e4-85e2-00f5044ba12e.JPG)

[Tela análise de proposta](https://user-images.githubusercontent.com/109303611/183444983-6f3ca69f-c53c-4428-9814-5616e0cf0cb9.JPG)


# English translation

### Summary version 1.1:

Modify __*version 1.0*__ for individual and legal entity credit analysis system.

**Scope for version 1.1:**

- [x] Modifications
    - [x] Change the name of option 01 and 02
    - [x] Include system name above Main Menu
    - [x] Change registered people menu
    - [x] Change registration menu
        
- [x] Individual Registration
    - [x] CPF Registration
    - [x] Improved age registration
    - [x] Net Income Registration

- [x] Registration of Legal Entities
    - [x] Company Name Registration
    - [x] CNPJ Registration
    - [x] Company Size Register
    - [x] Register of Fixed Capital
    - [x] Cash Flow Record for the last 3 months
    - [x] Registration of the D.R.E of the last year

- [x] Menu Registration Credit Proposal
    - [x] Individual Analysis
    - [x] Legal Entity Analysis

**Techniques used:**

* library imports
* modularization
* conditionals
* While and For loops
* colorization with ANSCI codes
* reading and writing txt files
* Functions
* Try, except, else, Finally error handling
* Dictionary
* List

[Main screen](https://user-images.githubusercontent.com/109303611/183444915-c5446a8f-d05c-4f4d-a1f5-97349923137d.JPG)

[Individual Database screen](https://user-images.githubusercontent.com/109303611/183444934-cd663dc5-8add-4897-be1e-d7ff03238900.JPG)

[Legal Entity Database screen](https://user-images.githubusercontent.com/109303611/183444968-366dcbc2-9afc-48e4-85e2-00f5044ba12e.JPG)

[Proposal analysis screen](https://user-images.githubusercontent.com/109303611/183444983-6f3ca69f-c53c-4428-9814-5616e0cf0cb9.JPG)


___


### Cadastro + DB.txt

### Resumo versão 1.0:

Sistema simples **(prompt command)** que cadastra pessoas e a idade, escrito em Python tendo como base de dados arquivo com extenção txt. 

**Técnicas utilizadas:**

* importações de bibliotecas
* modularização
* condicionais
* loops While e For
* colorização com códigos ANSCI
* leitura e gravação de arquivos txt
* Funções
* Tratamento de erros Try, except, else, Finally
* Dicionário

**Telas do Programa:**

[Tela principal](https://user-images.githubusercontent.com/109303611/183476531-02f29dea-5e8a-4b7d-888d-41907baaaf25.JPG)

[Tela de Cadastro](https://user-images.githubusercontent.com/109303611/183476540-4c30a0f4-c7ed-406d-87ff-4c5937feefa3.JPG)

[Tela do banco de dados](https://user-images.githubusercontent.com/109303611/183476552-8922fefd-189e-4462-a068-807f6f96cf09.JPG)


# English translation

### Summary version 1.0:

Simple system **(command prompt)** that registers people and age, written in Python with a file with txt extension as a database.

**Techniques used:**

* library imports
* modularization
* conditionals
* While and For loops
* colorization with ANSCI codes
* reading and writing txt files
* Functions
* Try, except, else, Finally error handling
* Dictionary

**Telas do Programa:**

[Main screen](https://user-images.githubusercontent.com/109303611/183476531-02f29dea-5e8a-4b7d-888d-41907baaaf25.JPG)

[Registration screen](https://user-images.githubusercontent.com/109303611/183476540-4c30a0f4-c7ed-406d-87ff-4c5937feefa3.JPG)

[Database screen](https://user-images.githubusercontent.com/109303611/183476552-8922fefd-189e-4462-a068-807f6f96cf09.JPG)

---
