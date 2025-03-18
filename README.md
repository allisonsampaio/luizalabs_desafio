# LuizaLabs Desafio Técnico - Vertical Logística

Este projeto é uma solução para o desafio técnico da LuizaLabs, que consiste em processar um arquivo de pedidos desnormalizado e transformá-lo em um formato JSON normalizado. A aplicação é composta por um **backend** em FastAPI e um **frontend** em React, permitindo que os usuários façam upload de arquivos e visualizem o JSON processado.

## Tecnologias Utilizadas

O backend foi desenvolvido em **Python** com **FastAPI** para a API REST, utilizando **Pydantic** para validação de dados e **Uvicorn** como servidor. Para o frontend, foi usado **React** com **Material-UI (MUI)** para a interface, **TypeScript** para tipagem estática e **Axios** para chamadas à API. A aplicação é containerizada com **Docker** e orquestrada com **Docker Compose**.

## Como Executar o Projeto

### **Pré-requisitos**

- **Docker**: [Instruções para instalar o Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Instruções para instalar o Docker Compose](https://docs.docker.com/compose/install/)

### **1. Usando Docker (Recomendado)**

#### Passos:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/allisonsampaio/luizalabs_desafio.git
   cd luizalabs_desafio
   ```

2. **Construa e rode os containers**:

   ```bash
   sudo docker-compose up --build
   ```

   Isso vai:
   - Construir as imagens do backend e do frontend.
   - Iniciar os containers.

3. **Acesse a aplicação**:
   - **Backend**: Disponível em `http://localhost:8000`.
     - Documentação da API (Swagger): `http://localhost:8000/docs`.
   - **Frontend**: Disponível em `http://localhost:3000`.

4. **Parar os containers**:

   ```bash
   docker-compose down
   ```

## Como Usar a Aplicação

1. **Acesse o Frontend**:
   - Abra `http://localhost:3000` no navegador.

2. **Faça o Upload de um Arquivo**:
   - Clique em "Escolher arquivo" e selecione um arquivo `.txt` no formato especificado.
   - Clique em "Processar Arquivo".

3. **Visualize o JSON**:
   - O JSON processado será exibido.
   - Clique em "Baixar JSON" para salvar o arquivo.

4. **Resetar**:
   - Clique em "Resetar" para limpar o JSON e fazer um novo upload.

## Endpoints da API (Backend)

### **POST `/upload`**

- **Descrição**: Recebe um arquivo `.txt` e retorna os dados processados em formato JSON.
- **Exemplo de Uso**:

  ```bash
  curl -X POST -F "file=@caminho/para/arquivo.txt" http://localhost:8000/upload
  ```

- **Resposta de Sucesso**:

  ```json
  [
    {
      "user_id": 70,
      "name": "Palmer Prosacco",
      "orders": [
        {
          "order_id": 753,
          "total": "1836.74",
          "date": "20210308",
          "products": [
            {
              "product_id": 3,
              "value": "1836.74"
            }
          ]
        }
      ]
    }
  ]
  ```

- **Resposta de Erro**:

  ```json
  {
    "detail": "O arquivo deve ser um .txt"
  }
  ```

## Testes

### **Backend**:
Para rodar os testes do backend, siga os seguintes passos:

1. **Crie e ative o ambiente virtual**:
   Se ainda não tiver criado o ambiente virtual, faça isso com o comando:

   ```bash
   python3 -m venv venv
   ```

   Ative o ambiente virtual:

   - No Linux/Mac:

     ```bash
     source venv/bin/activate
     ```

   - No Windows:

     ```bash
     .\venv\Scripts\activate
     ```

2. **Instale as dependências**:
   Com o ambiente virtual ativado, instale os pacotes necessários com:

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute os testes**:
   Agora, para rodar os testes do backend, basta executar o comando:

   ```bash
   cd app
   pytest
   ```

Certifique-se de estar no ambiente virtual e com as dependências instaladas para garantir que os testes sejam executados corretamente.

#### Testes Implementados:

##### **Testes do `test_main.py`**:
1. **`test_upload_file_success`**:
   - Testa o endpoint `/upload` com um arquivo válido.
   - Verifica se o JSON retornado está no formato correto.

2. **`test_upload_file_invalid_format`**:
   - Testa o endpoint `/upload` com um arquivo de formato inválido (não é `.txt`).
   - Verifica se a API retorna um erro `400`.

3. **`test_upload_file_empty`**:
   - Testa o endpoint `/upload` com um arquivo vazio.
   - Verifica se a API retorna um erro `400`.

##### **Testes do `test_services.py`**:
1. **`test_process_file`**:
   - Testa a função `process_file` para garantir que um arquivo válido seja processado corretamente.
   - Verifica se o arquivo é processado e os dados são extraídos corretamente, incluindo a verificação dos atributos dos objetos `UserOrders`, `Order`, e `Product`.

2. **`test_process_file_empty`**:
   - Testa a função `process_file` com um arquivo vazio.
   - Verifica se o resultado da função é uma lista vazia.

3. **`test_process_file_invalid_format`**:
   - Testa a função `process_file` com um arquivo de formato inválido.
   - Verifica se o resultado da função é uma lista vazia.
