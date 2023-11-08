FROM python:3.10.13-slim

RUN apt-get update && apt-get install -y gcc

RUN pip install --upgrade pip

RUN pip install pipenv

RUN mkdir app/ && cd app/

WORKDIR /app

RUN mkdir model/
RUN mkdir datasets/

COPY ["Pipfile", "Pipfile.lock", "*.py", "datasets/*", "./"] /app/

RUN pipenv install --system --deploy

CMD [ "pipenv","shell" ]  
RUN python train.py

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0", "predict:app"]

# ENTRYPOINT ["pipenv", "run", "gunicorn", "app:app"]