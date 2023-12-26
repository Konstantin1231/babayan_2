FROM python:3.10
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:flask_app

#docker build -t welcome-app .

#docker images

# docker run -p 5000:5000 welcome-app

# docker ps (see what containers are runnung)

#docker stop {container id}


# docker login

#(before we should delete last docker image and create new one usinf name conventions)
#docker image rm -f welcome-app

# (new name) docker build -t koq1231/welcome-app .
# (other way, we can simple change name ) docker tag koq1231/welcome-app koq1231/misha

#(push docker) docker push koq1231/misha:lastest