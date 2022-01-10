FROM python:3.10
COPY ../application/. /root/flask
WORKDIR ./root/flask
RUN pip install -r requirements.txt

ENV emailusername=quiznose.notification@gmail.com
ENV emailpassword=Kuralabs123

ENV host=database-1.cet4jo0trfys.us-east-1.rds.amazonaws.com
ENV db_user=admin
ENV db_pass=KuraLabs#123

ENV FLASK_APP=app.py
ENV FLASK_ENV=Production

ENV secret_key=testkey
ENV client_key=at_zmz5m4BQ9kegkMqfGaTujPCCUD135

EXPOSE 5000
CMD flask run --host=0.0.0.0
