FROM python:3.6.1-alpine
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 5000
EXPOSE 5001
ENV FLASK_ENV=development
ENV FLASK_APP=flaskr
CMD ["flask", "run"]
