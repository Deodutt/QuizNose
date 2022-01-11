FROM python:3.10
COPY ./application /root/application
WORKDIR ./root/application/
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py


EXPOSE 5000
CMD flask run --host=0.0.0.0
