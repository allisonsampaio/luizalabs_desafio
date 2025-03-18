# LuizaLabs Desafio Técnico - Vertical Logística

Este projeto é uma solução para o desafio técnico da LuizaLabs, que consiste em processar um arquivo de pedidos desnormalizado e transformá-lo em um formato JSON normalizado. A aplicação é composta por um **backend** em FastAPI e um **frontend** em React, permitindo que os usuários façam upload de arquivos, consultem pedidos por ID ou intervalo de datas e visualizem o JSON processado.

## Tecnologias Utilizadas

O backend foi desenvolvido em **Python**, utilizando o framework **FastAPI** para construir a API REST. Para validação de dados e modelos, foi utilizado o **Pydantic**, enquanto o **Uvicorn** atua como servidor ASGI. O banco de dados escolhido foi o **MongoDB**, responsável por armazenar os pedidos. A aplicação foi containerizada com **Docker**, e os testes unitários foram implementados com o **Pytest**.

No frontend, a interface foi construída com **React**, utilizando componentes estilizados do **Material-UI (MUI)**. A tipagem estática foi garantida com **TypeScript**, e as chamadas à API foram feitas com o **Axios**.

## Arquitetura do Backend

O backend foi projetado seguindo boas práticas de arquitetura de software, com foco em **modularidade**, **escalabilidade** e **facilidade de manutenção**. A estrutura do projeto é organizada em camadas, separando responsabilidades e facilitando a evolução do código.

### **Estrutura do Backend**

```
app/
├── api/
│   ├── __init__.py
│   ├── orders.py
│   └── upload.py
│
├── database/
│   ├── __init__.py
│   └── mongo_db.py
│
├── models/
│   ├── __init__.py
│   ├── order.py
│   ├── product.py
│   └── user_orders.py
│
├── services/
│   ├── __init__.py
│   └── file_processing.py
│
├── utils/
│   ├── __init__.py
│   └── file_utils.py
│
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── test_services.py
│
├── __init__.py
└── main.py
```

### **Funcionamento do Backend**

1. **Upload de Arquivo**:
   - O usuário faz o upload de um arquivo `.txt` no formato especificado.
   - O backend processa o arquivo, extrai os dados e os armazena no MongoDB.
   - Os dados são retornados em formato JSON.

2. **Consulta de Pedidos**:
   - O usuário pode consultar pedidos por ID ou por intervalo de datas.
   - O backend busca os dados no MongoDB e os retorna em formato JSON.

3. **Banco de Dados (MongoDB)**:
   - Os pedidos são armazenados em uma coleção chamada `orders`.
   - Cada documento na coleção representa um usuário com seus pedidos e produtos.

### **Decisões de Projeto**

1. **Modularização**:
   - O projeto foi dividido em módulos (API, banco de dados, serviços, modelos e utilitários) para facilitar a manutenção e a escalabilidade.

2. **Validação de Dados**:
   - O Pydantic foi utilizado para validar os dados de entrada e garantir que estejam no formato correto.

3. **Testes**:
   - Foram implementados testes unitários para garantir a qualidade do código.

4. **Containerização**:
   - O uso de Docker e Docker Compose permite que a aplicação seja facilmente executada em qualquer ambiente.


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

### **Frontend**

1. **Acesse o Frontend**:
   - Abra `http://localhost:3000` no navegador.

2. **Faça o Upload de um Arquivo**:
   - Clique em "Escolher arquivo" e selecione um arquivo `.txt` no formato especificado.
   - Clique em "Processar Arquivo".
   - O JSON processado será exibido na tela.
   - Clique em "Baixar JSON" para salvar o arquivo.

3. **Consultar Pedido por ID**:
   - Na seção "Consultar Pedido por ID", insira o ID do pedido que deseja buscar.
   - Clique em "Buscar".
   - Os detalhes do pedido serão exibidos na tela.

4. **Consultar Pedidos por Intervalo de Datas**:
   - Na seção "Consultar Pedidos por Intervalo de Datas", insira a data de início e a data de fim no formato `YYYYMMDD`.
   - Clique em "Buscar".
   - A lista de pedidos dentro do intervalo especificado será exibida na tela.

5. **Resetar**:
   - Clique em "Resetar" para limpar o JSON e fazer um novo upload.

### **Exemplos de Uso**

#### **1. Upload de Arquivo**
- Selecione um arquivo `.txt` no formato:
  ```
  0000000070                              Palmer Prosacco00000007530000000003     1836.7420210308
  0000000075                                  Bobbie Batz00000007980000000002     1578.5720211116
  ```
- Após o processamento, o JSON será exibido:
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
    },
    {
      "user_id": 75,
      "name": "Bobbie Batz",
      "orders": [
        {
          "order_id": 798,
          "total": "1578.57",
          "date": "20211116",
          "products": [
            {
              "product_id": 2,
              "value": "1578.57"
            }
          ]
        }
      ]
    }
  ]
  ```

#### **2. Consultar Pedido por ID**
- Insira o ID do pedido, por exemplo, `753`.
- O resultado será:
  ```json
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
  ```

#### **3. Consultar Pedidos por Intervalo de Datas**
- Insira a data de início (`20210101`) e a data de fim (`20211231`).
- O resultado será:
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

### **Observações**
- Certifique-se de que o arquivo `.txt` esteja no formato correto.
- As datas devem ser inseridas no formato `YYYYMMDD`.
- Se não houver pedidos correspondentes à consulta, uma mensagem de erro será exibida.

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

### **GET `/orders/{order_id}`**

- **Descrição**: Retorna os detalhes de um pedido com base no ID.
- **Exemplo de Uso**:

  ```bash
  curl http://localhost:8000/orders/753
  ```

- **Resposta de Sucesso**:

  ```json
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
  ```

- **Resposta de Erro**:

  ```json
  {
    "detail": "Pedido não encontrado"
  }
  ```

### **GET `/orders/`**

- **Descrição**: Retorna os pedidos dentro de um intervalo de datas.
- **Exemplo de Uso**:

  ```bash
  curl "http://localhost:8000/orders/?start_date=20210101&end_date=20211231"
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
    "detail": "Nenhum pedido encontrado no intervalo de datas especificado"
  }
  ```

## Testes

### **Executando Testes no Container do Backend**

Para rodar os testes diretamente no container do backend, siga os passos abaixo:

1. **Acesse o container do backend**:

   ```bash
   docker exec -it luizalabs_desafio-backend-1 /bin/bash
   ```

2. **Navegue até a pasta de testes**:

   ```bash
   cd /app/tests
   ```

3. **Execute os testes**:

   ```bash
   pytest
   ```

   Isso vai rodar todos os testes unitários.

## Testes Implementados

### **Testes do `test_main.py`**:
1. **`test_upload_file_success`**:
   - Testa o endpoint `/upload` com um arquivo válido, verificando o status da resposta e a estrutura do JSON retornado.

2. **`test_get_order_by_id`**:
   - Testa o endpoint `/orders/{order_id}`, verificando se o pedido retornado contém o `order_id` correto.

3. **`test_get_orders_by_date_range`**:
   - Testa o endpoint `/orders/`, verificando se a lista de pedidos retornada não está vazia.

### **Testes do `test_services.py`**:
1. **`test_process_file`**:
   - Testa a função `process_file` com um arquivo válido, verificando se os dados são extraídos corretamente.

2. **`test_process_file_empty`**:
   - Testa a função `process_file` com um arquivo vazio, verificando se o resultado é uma lista vazia.

3. **`test_process_file_invalid_format`**:
   - Testa a função `process_file` com um arquivo de formato inválido, verificando se o resultado é uma lista vazia.