FROM python:3
WORKDIR /usr/src/app

## Install packages
COPY requirements.txt ./
RUN pip install -r requirements.txt

## Copy all src files
# COPY . .

## Run the application on the port 8080
EXPOSE 7000

# gunicorn 배포 명령어
# CMD ["gunicorn", "--bind", "허용하는 IP:열어줄 포트", "project.wsgi:application"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:7000"]
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "webapp.wsgi:visualize"]
