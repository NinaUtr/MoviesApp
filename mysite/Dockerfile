FROM python:3.8-slim-buster
RUN mkdir /code
WORKDIR /code
ENV PYTHONUNBUFFERED 1
RUN pip install pipenv
COPY Pipfile Pipfile.lock ${PROJECT_DIR}/
RUN pipenv install --system --deploy
COPY . /code/
COPY ./wait-for-it.sh /var/wait-for-it.sh
RUN chmod +x /var/wait-for-it.sh