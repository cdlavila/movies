FROM python:3.10

WORKDIR /code

COPY . /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# Commands
# docker build -t movies-app .
# docker run -d --name movies-app -p 80:80 movies-app
# remember the env variables