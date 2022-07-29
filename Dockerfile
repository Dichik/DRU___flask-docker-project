FROM python:3.7

WORKDIR /DRU___flask-docker-project

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

RUN export PYTHONPATH='${PYTHONPATH}:/DRU___flask-docker-project'

COPY . .

CMD ["python", "./run.py"]