FROM python:3.9
WORKDIR /app
# Add MongoDB repository and install mongodb-org-tools
RUN apt-get update && apt-get install -y gnupg wget && \
    wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add - && \
    echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/debian bullseye/mongodb-org/6.0 main" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list && \
    apt-get update && apt-get install -y mongodb-org-tools
# Copy the script and the CSV file into the working directory
COPY . /app/
CMD ["python", "/app/import-csv-job.py"]