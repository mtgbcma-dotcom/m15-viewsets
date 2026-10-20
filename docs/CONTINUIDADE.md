# Continuidade do Bookstore — módulos 13, 14 e 15

## Entregas de referência

| Módulo | Entrega | Commit consultado | Conteúdo |
|---|---|---|---|
| 13 | [bookstore — PR #1](https://github.com/mtgbcma-dotcom/bookstore/pull/1) | [`19ae2f7`](https://github.com/mtgbcma-dotcom/bookstore/commit/19ae2f7f238582e0fccf2eb4c58c3aecdf4df451) | Projeto Django `bookstore`, app `api`, DRF em `INSTALLED_APPS` e ambiente Poetry. |
| 14 | [m57-bookstore — PR #1](https://github.com/mtgbcma-dotcom/m57-bookstore/pull/1) | [`d48cbdf`](https://github.com/mtgbcma-dotcom/m57-bookstore/commit/d48cbdf242ff2342cc763f090c949b19b10525b5) | Modelos Category, Product e Order, migração, serializers e 25 testes. |
| 15 | [m15-viewsets — PR #1](https://github.com/mtgbcma-dotcom/m15-viewsets/pull/1) | Branch `viewsets` | ViewSets baseados nos serializers anteriores, rotas e mais 27 testes. |

Os repositórios têm nomes diferentes. A continuidade do código é demonstrada pela comparação dos arquivos abaixo; os links permitem consultar cada entrega anterior.

## Arquivos preservados do módulo 14

Os seguintes arquivos foram comparados com o commit `d48cbdf242ff2342cc763f090c949b19b10525b5` e são idênticos, incluindo a configuração Poetry restaurada nesta correção:

- `pyproject.toml`.
- `poetry.lock`.
- `api/models.py`.
- `api/serializers.py`.
- `api/migrations/0001_initial.py`.
- `api/admin.py` e `api/apps.py`.
- `manage.py`, `bookstore/asgi.py`, `bookstore/wsgi.py` e `bookstore/__init__.py`.

Os testes de `api/tests.py` do módulo 14 passaram para `api/tests/test_serializers.py`. As únicas alterações nesse conteúdo são os imports de `.models` e `.serializers` para `..models` e `..serializers`, necessários após a mudança para o pacote `api.tests`.

A estrutura do projeto Django continua sendo `bookstore`, com os modelos e serializers no app `api`. O nome `m57-bookstore` no `pyproject.toml`, as faixas de dependências e o lock do módulo anterior foram mantidos.

## Adições do módulo 15

- `CategoryViewSet`, `ProductViewSet` e `OrderViewSet` em `api/views.py`, usando os serializers anteriores.
- Rotas de categorias, produtos e pedidos registradas com `DefaultRouter` em `api/urls.py`.
- Inclusão das rotas da API, login da API navegável e redirecionamento inicial em `bookstore/urls.py`.
- Configuração de hosts locais em `bookstore/settings.py`.
- 27 testes em `api/tests/test_viewsets.py`, totalizando 52 com os testes de serializers.

## Conferência da entrega

Na pasta que contém `manage.py`:

```powershell
poetry check --lock
poetry install --no-root
poetry run python manage.py check
poetry run python manage.py makemigrations --check --dry-run
poetry run python manage.py test --verbosity 2
```

O banco SQLite e o ambiente virtual são gerados localmente. Os arquivos necessários para recriar o banco e instalar as dependências estão versionados: migrações, `pyproject.toml` e `poetry.lock`. Para acessar a API navegável, execute as migrações, crie um superusuário e inicie o servidor conforme o README.

## Validação da correção

Verificações realizadas em 20/10/2026, com Python 3.13, Poetry 2.5.1 e um ambiente virtual novo:

- `poetry check --lock`: manifesto e lock válidos.
- `poetry install --no-root --no-interaction`: dependências instaladas a partir do lock, sem atualizações.
- `poetry run python manage.py check`: nenhum problema identificado.
- `poetry run python manage.py makemigrations --check --dry-run`: nenhuma mudança de modelo pendente.
- `poetry run python manage.py test --verbosity 2`: 52 testes aprovados.
- `poetry run python manage.py migrate --noinput`: banco SQLite criado com as migrações existentes.
- Comparação com o módulo 14: os 11 arquivos listados como preservados são idênticos; os testes de serializers diferem apenas nos dois imports relativos.
