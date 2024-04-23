FROM python:3.11-rc-slim

WORKDIR /api

COPY ./req.txt /api/req.txt

RUN pip install --no-cache-dir --upgrade -r /api/req.txt

COPY . /api

CMD ["python3.11", "app.py"]