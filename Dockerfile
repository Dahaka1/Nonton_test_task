FROM python:3.9

WORKDIR usr/src/nonton

COPY ./requirements.txt /usr/src/nonton/requirements.txt
RUN pip install -r /usr/src/nonton/requirements.txt

COPY . /usr/src/nonton