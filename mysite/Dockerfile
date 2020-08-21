FROM python:3.8-alpine
RUN mkdir /code
WORKDIR /code
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
COPY Pipfile Pipfile.lock ${PROJECT_DIR}/
RUN pipenv install --system --deploy
COPY . /code/