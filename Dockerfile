FROM python:3.11

WORKDIR /app
COPY requierements.txt /app/requierements.txt

RUN pip install --no-cache-dir --upgrade -r app/requirements.txt

COPY . /app/

CMD bash -c "while true; do sleep 1; done"