FROM python:3.8

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)"
RUN apt-get install sqlite3
RUN sqlite3 scary_model_storage.db "create table models(id integer primary key autoincrement, name varchar(255) not null, model blob not null);"

COPY requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt

COPY ./jobs/24-hours.sh /home/24-hours.sh
COPY ./python /python