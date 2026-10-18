# Bookstore — ViewSets em Django REST Framework

Atividade do Módulo 15 de Continuação Back-End Python da EBAC.

Implementei uma API de livraria com ViewSets baseados nos serializers de categorias, produtos e pedidos. As rotas são geradas pelo `DefaultRouter`, e os testes verificam as operações da API, as validações e os relacionamentos entre os modelos.

## Tecnologias

- Python
- Django
- Django REST Framework
- SQLite

## Funcionalidades

- Listar, consultar, cadastrar, atualizar e excluir categorias, produtos e pedidos.
- Validar os dados recebidos pelos serializers.
- Receber a categoria de um produto pelo campo `category_id`.
- Receber os produtos de um pedido pelo campo `product_ids`.
- Exibir os relacionamentos de forma aninhada nas respostas.
- Impedir preços inválidos, nomes de categoria repetidos e pedidos sem produtos.
- Retornar erros de validação para IDs relacionados inexistentes.
- Impedir a exclusão de categorias que tenham produtos vinculados.
- Restringir os endpoints de gestão a usuários da equipe, incluindo o superusuário.

## Executar no Windows

Com Python 3.10 ou mais recente instalado, abra a pasta que contém `manage.py` e execute no terminal:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
.\.venv\Scripts\python.exe manage.py runserver
```

Abra http://127.0.0.1:8000/api/ e clique em **Log in**. Entre com o superusuário criado para acessar os endpoints e os formulários da API navegável.

O painel administrativo também está disponível em http://127.0.0.1:8000/admin/.

O SQLite é criado localmente pelas migrações. As credenciais são definidas durante `createsuperuser`.

## Endpoints

| Recurso | Listagem e criação | Consulta, atualização e exclusão |
|---|---|---|
| Categorias | `/api/categories/` | `/api/categories/{id}/` |
| Produtos | `/api/products/` | `/api/products/{id}/` |
| Pedidos | `/api/orders/` | `/api/orders/{id}/` |

- `GET`: listar ou consultar.
- `POST`: cadastrar.
- `PUT`: atualizar os campos obrigatórios do recurso.
- `PATCH`: atualizar somente os campos enviados.
- `DELETE`: excluir.

## Exemplos de cadastro

### Categoria

Em `/api/categories/`, envie:

```json
{
  "name": "Programação",
  "description": "Livros de desenvolvimento de software"
}
```

### Produto

Em `/api/products/`, use o ID retornado no cadastro da categoria:

```json
{
  "name": "Python na prática",
  "description": "Exercícios de programação",
  "price": "89.90",
  "active": true,
  "category_id": 1
}
```

### Pedido

Em `/api/orders/`, informe o ID de um usuário cadastrado e os IDs dos produtos:

```json
{
  "user": 1,
  "product_ids": [1],
  "status": "pending"
}
```

Os IDs acima são exemplos. Utilize os IDs existentes no seu banco. Os usuários podem ser consultados no painel administrativo. O status do pedido pode ser `pending`, `completed` ou `cancelled`.

Para testar uma atualização parcial, envie `{"status": "completed"}` com `PATCH` ao endereço de um pedido existente.

## Testes

```powershell
.\.venv\Scripts\python.exe manage.py check
.\.venv\Scripts\python.exe manage.py makemigrations --check --dry-run
.\.venv\Scripts\python.exe manage.py test --verbosity 2
```

A suíte contém **52 testes**: 25 para serializers e 27 para ViewSets, rotas e permissões. Os testes utilizam um banco separado e verificam:

- Criação e representação dos objetos pelos serializers.
- Operações GET, POST, PUT, PATCH e DELETE.
- Persistência das alterações e dos relacionamentos.
- Dados inválidos e campos obrigatórios.
- Respostas 400, 403 e 404 nos cenários correspondentes.
- Atualizações parciais e campos somente de leitura.
- Comportamento da exclusão de categorias com produtos.
- Ação de ViewSet chamada diretamente com `APIRequestFactory`.

## Estrutura

```text
api/
  models.py
  serializers.py
  views.py
  urls.py
  admin.py
  migrations/
  tests/
    test_serializers.py
    test_viewsets.py
bookstore/
  settings.py
  urls.py
manage.py
requirements.txt
```

## Referências

- [ViewSets — Django REST Framework](https://www.django-rest-framework.org/api-guide/viewsets/)
- [Routers — Django REST Framework](https://www.django-rest-framework.org/api-guide/routers/)
- [Testes — Django REST Framework](https://www.django-rest-framework.org/api-guide/testing/)

## Autor

Bruno Costa Macedo de Almeida
