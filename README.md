# File-sharing-system



# Project Setup & Deployment strategy 

## Prerequisites

1. .env required variables
1. Python 3.x
2. Virtual Environment

## Environment Variables

 Add the following environment variables:

```env
HOST_EMAIL=test@gmail.com
HOST_EMAIL_APP_PASSWORD=xyz
FRONTEND_URL=example.com
DATABASE_NAME=name
DATABASE_USER=user
DATABASE_PASSWORD=passcode

##Create and activate virtual environment
python3 -m venv myenv
source myenv/bin/activate


##Install Project Dependencies
pip3 install -r requirements.txt

##Run server
then python manage.py runserver

#-----------------------------------------------------------
# My Deployment Strategy of the above project

For deploying this Django application to a production environment. I will use AWS for cloud services, Docker for containerization, and Nginx for the web server.

## Prerequisites

- AWS Account
- Docker installed 
- Command line terminal

## Steps

### Step 1: Dockerize the Application

1. Create a `Dockerfile` in your project root with the following content:

    ```Dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.x

    # Set the working directory in the container
    WORKDIR /app

    # Install project dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the current directory contents into the container at /app
    COPY . .

    # Make port 8000 available to the  outside of this container
    EXPOSE 8000

    # Run app.py when the container launches
    CMD ["gunicorn", "-b", "0.0.0.0:8000", "project.wsgi:application"]
    ```


3. Build the Docker image:

    ```bash
    docker build -t project_name .
    ```

### Step 2: Deploy to AWS

1. Log in to your AWS account and navigate to the EC2 dashboard.
2. Create a new EC2 instance.
3. Install Docker on the EC2 instance, pull docker image and run it:

    ```bash
    sudo apt update
    sudo apt install docker.io
........
    ```


### Step 3: Set Up Nginx

1. Install Nginx:

    ```bash
    sudo apt install nginx
    ```

2. Create a new Nginx configuration file:

    ```bash
    sudo nano /etc/nginx/sites-available/your_project
    ```

    Configure nginx to run the project on a particular domain

    ```nginx
    server {
        listen 80;
        server_name your_domain.com www.your_domain.com;

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
    ```

3. Enable the Nginx configuration and restart the service:

    ```bash
    sudo systemctl restart nginx
    ```





