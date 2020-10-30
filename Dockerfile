FROM python:3.8

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.1/zsh-in-docker.sh)"
RUN apt-get install sqlite3

COPY requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt

COPY ./jobs/24-hours.sh /home/24-hours.sh