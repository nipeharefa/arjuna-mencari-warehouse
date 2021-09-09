FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
EXPOSE 80
COPY . /app
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]