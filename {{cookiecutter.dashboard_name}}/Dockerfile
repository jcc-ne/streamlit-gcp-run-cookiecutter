FROM python:3.8-slim

EXPOSE 8080

RUN apt update && apt install gcc -y && rm -rf /var/lib/apt/lists/*
RUN pip install -U pip

COPY requirements.txt app/requirements.txt
RUN pip install -r app/requirements.txt

COPY main_dashboard.py /app
COPY db_utils /app/db_utils
WORKDIR /app

ENTRYPOINT ["streamlit", "run", "main_dashboard.py", "--server.port=8080", "--server.address=0.0.0.0"]
