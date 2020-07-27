FROM python:3.7-alpine
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["app.py"]
