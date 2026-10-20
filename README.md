# Bookstore — ViewSets em Django REST Framework

Atividade do Módulo 15 de Continuação Back-End Python da EBAC.

Implementei uma API de livraria com ViewSets baseados nos serializers de categorias, produtos e pedidos. As rotas são geradas pelo `DefaultRouter`, e os testes verificam as operações da API, as validações e os relacionamentos entre os modelos.

## Continuidade do projeto

Esta entrega continua o Bookstore dos módulos 13 e 14:

- [Módulo 13 — configuração do Django REST Framework com Poetry](https://github.com/mtgbcma-dotcom/bookstore/pull/1).
- [Módulo 14 — modelos, serializers e testes](https://github.com/mtgbcma-dotcom/m57-bookstore/pull/1).
- Módulo 15 — ViewSets, rotas e testes da API adicionados à mesma base.

Os arquivos `api/models.py`, `api/serializers.py` e `api/migrations/0001_initial.py` são idênticos aos da entrega do módulo 14. Os 25 testes de serializers foram preservados em `api/tests/test_serializers.py`, com ajuste apenas dos imports relativos para a organização em pacote.

`pyproject.toml` e `poetry.lock` foram recuperados integralmente do módulo 14. O nome `m57-bookstore` no manifesto foi mantido para preservar a identificação do projeto anterior. O Poetry é a forma principal de instalar e executar o projeto. Veja os commits e a comparação dos arquivos em [Continuidade e validação](docs/CONTINUIDADE.md).

## Tecnologias

- Python
- Django
- Django REST Framework
- Poetry
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

Com Python 3.10 ou mais recente e Poetry 2.5.1 instalado, abra a pasta que contém `manage.py`, `pyproject.toml` e `poetry.lock` e execute no terminal:

```powershell
poetry check --lock
poetry install --no-root
poetry run python manage.py migrate
poetry run python manage.py createsuperuser
poetry run python manage.py runserver
```

O comando de instalação utiliza as versões registradas em `poetry.lock`. Não é necessário executar `poetry update` para avaliar a entrega. `requirements.txt` permanece como alternativa para instalação com pip, com as mesmas faixas de dependências diretas do manifesto.

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
poetry check --lock
poetry run python manage.py check
poetry run python manage.py makemigrations --check --dry-run
poetry run python manage.py test --verbosity 2
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
pyproject.toml
poetry.lock
requirements.txt
docs/
  CONTINUIDADE.md
```

## Referências

- [ViewSets — Django REST Framework](https://www.django-rest-framework.org/api-guide/viewsets/)
- [Routers — Django REST Framework](https://www.django-rest-framework.org/api-guide/routers/)
- [Testes — Django REST Framework](https://www.django-rest-framework.org/api-guide/testing/)

## Autor

Bruno Costa Macedo de Almeida
