FROM python:3.10
COPY ../application/. /root/flask
WORKDIR ./root/flask
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
EXPOSE 5000
CMD flask run --host=0.0.0.0