FROM python:3.12
 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
WORKDIR /getgig

# Copy all files into the container
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
 

EXPOSE 8000
 

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]