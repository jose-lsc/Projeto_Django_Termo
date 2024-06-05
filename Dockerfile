FROM python:3.12
RUN mkdir -p /opt/termo
COPY . /opt/termo/
RUN pip install django termcolor unidecode python-decouple dj-database-url psycopg2-binary
WORKDIR /opt/termo
RUN chmod +x entrypoint.sh
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
