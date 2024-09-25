#checkov:skip=CKV_DOCKER_2
#checkov:skip=CKV_DOCKER_3
FROM python:3.12-alpine

WORKDIR /checker

COPY pyproject.toml poetry.lock ./
RUN pip install --no-cache-dir poetry==1.8.3 \
  && poetry install --no-dev

COPY checker ./checker

CMD [ "python", "-m", "checker" ]
