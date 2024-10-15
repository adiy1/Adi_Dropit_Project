FROM python:3.9
WORKDIR /app
COPY . /app/
RUN pip install requests
CMD ["python", "/app/create-and-export-posts-job.py"]