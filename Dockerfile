FROM python:3.8.6
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN chmod u+x ./entrypoint.sh