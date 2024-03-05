# official Python runtime as a parent image
FROM python:3.10-slim

# Setting the working directory in the container
WORKDIR /app

# Installing non-Python dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends $(cat apt-packages.txt) && \
    rm -rf /var/lib/apt/lists/*

# Copying the current directory contents into the container at /app
COPY . /app

# Installing needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exposing the port on which the application will run
EXPOSE 3333

# Environment variable for PDF path
ENV PDF_PATH /app/pdfs

# Running the script when the container launches
CMD ["python", "main.py"]