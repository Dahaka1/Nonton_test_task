FROM python:3.9

WORKDIR usr/src/nonton

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . usr/src/nonton

CMD ["python", "./usr/src/"]