FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install .
RUN sonicpyapp create-db
RUN sonicpyapp populate-db
RUN sonicpyapp add-user -u admin -p admin
EXPOSE 5000
CMD ["sonicpyapp", "run"]
