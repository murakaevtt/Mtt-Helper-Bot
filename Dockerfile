FROM python:3.12.6-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


CMD [ "python", "main.py" ]