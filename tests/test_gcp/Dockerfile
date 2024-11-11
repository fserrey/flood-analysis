FROM python:3.10-slim

WORKDIR /app

COPY ../../requirements.txt app/requirements.txt
COPY read_files.py app/read_files.py

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "read_files.py"]