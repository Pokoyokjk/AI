# Install Docker
https://docs.docker.com/engine/install/

# Download the following
- Dockerfile, uploaded to dockerfile/Dockerfile
 
- requirements.txt, uploaded to dependencies/requirements.txt

 - apt-packages.txt, uploaded to dependencies/apt-packages.txt
 
# Open Docker (to run it)

# Open your teminal
- Navigate to the directory containing Dockerfile, requirements.txt and apt-packages.txt
  
# Run the following commands 
- To build the Docker image:

$ docker build -t myapp .

- To run the Docker image:

$ docker run -v /path/to/pdfs:/app/pdfs -p 3333:3333 myapp

- To access the app:

http://localhost:3333
