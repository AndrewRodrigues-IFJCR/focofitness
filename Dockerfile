FROM python:3.12-slim

RUN echo 'Configurando variveis de ambiente!'
ENV POETRY_VIRTUALENVS_CREATE=false

RUN echo 'Copiando artefatos do projeto!'
WORKDIR /app/
COPY . .

RUN echo 'Instalando o Poetry!'
RUN pip install poetry
RUN poetry install --no-interaction --no-ansii

RUN echo 'Rodando projeto!'
EXPOSE 8000
CMD poetry run uvicorn --host 0.0.0.0 focofitness.app:app

