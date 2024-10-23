# Dockerfile
FROM python:latest

# Çalışma dizini ayarlama
WORKDIR /app

# Gereksinimlerinizi kopyalayın
COPY requirements.txt .
# Gereksinimleri yükleyin
RUN pip install -r requirements.txt

# Uygulama kodunu kopyalayın
COPY ./myproject .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
