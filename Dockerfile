# Dockerfile
FROM python:latest

# Çalışma dizini ayarlama
WORKDIR /app

# Gereksinimlerinizi kopyalayın

# Gereksinimleri yükleyin
RUN pip install django

# Uygulama kodunu kopyalayın
COPY . .

RUN python manage.py migrate

# Sunucuyu başlatma
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
