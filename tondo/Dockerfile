FROM python:3.9

WORKDIR /tondo

COPY . /tondo

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


