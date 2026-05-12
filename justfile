default:
  just --list

run *args:
  uvicorn src.main:app --reload {{args}}

restart server:
  sudo systemctl restart fastapi

mm *args:
  alembic revision --autogenerate -m "{{args}}"

migrate:
  alembic upgrade head

downgrade *args:
  alembic downgrade {{args}}

ruff *args:
  ruff check {{args}} src

lint:
  ruff format src
  just ruff --fix

# docker
up:
  docker-compose up -d

kill *args:
  docker-compose kill {{args}}

build:
  docker-compose build

ps:
  docker-compose ps

pre-commit:
  git add .
  pre-commit run --all-files

# test (local) — requires local uv
test *args:
  docker compose -f docker-compose.test.yml up -d --wait
  -uv run --group test pytest {{args}}
  docker compose -f docker-compose.test.yml down

test-cov *args:
  docker compose -f docker-compose.test.yml up -d --wait
  -uv run --group test pytest --cov=src --cov-report=term-missing {{args}}
  docker compose -f docker-compose.test.yml down

# test (docker)
test-docker *args:
  docker compose -f docker-compose.test.yml run --build --rm test_runner uv run --group test pytest {{args}}
  docker compose -f docker-compose.test.yml down

test-docker-cov *args:
  docker compose -f docker-compose.test.yml run --build --rm test_runner uv run --group test pytest --cov=src --cov-report=term-missing {{args}}
  docker compose -f docker-compose.test.yml down
