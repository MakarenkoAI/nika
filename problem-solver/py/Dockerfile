#Deriving the latest base image
FROM python:latest

COPY . ./
RUN pip install --requirement ./requirements.txt

ENTRYPOINT ["python", "./server.py"]