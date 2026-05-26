FROM python:3.10-slim
RUN ln -snf /usr/share/zoneinfo/Europe/Kyiv /etc/localtime && echo Europe/Kyiv > /etc/timezone
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Нова команда для продакшену:
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "api:app"]
