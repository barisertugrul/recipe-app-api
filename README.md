# Recipe App API Source Code


This project is a Dockerized Python Django application for a recipe API. Follow the steps below to set up and run the project locally.

## Prerequisites

- Docker
- Docker Compose

## Setup Instructions

1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   cd <repository_directory>

2. **Create the .env file**:
Copy the .env.sample file to .env and update the environment variables as needed.  
cp .env.sample .env

3. **Build the Docker images**:
   ```sh
   docker-compose -f docker-compose-deploy.yml build --no-cache
   ```
4. **Run the containers**:
   ```sh
    docker-compose -f docker-compose-deploy.yml up
    ```
5. **Create a superuser**:
   ```sh
    docker-compose -f docker-compose-deploy.yml exec app sh -c "python manage.py createsuperuser"
    ```
6. **Access the API**:
Open your browser and navigate to http://127.0.0.1/api/swagger-ui/ to test the API.  

**Note**: If port 80 is already in use on your local machine, update line 37 in docker-compose-deploy.yml to - 8000:8000.
Then navigate to http://127.0.0.1:8000/api/swagger-ui/ to test the API.

7. **Development Environment**:
To run the project in a development environment:
***Update the Dockerfile***:
Open the Dockerfile and change the line ARG DEV=false to ARG DEV=True

***Build the Docker images***:
```sh
    docker-compose build
```

***Run the containers***:
```sh
    docker-compose up
```

### Additional Information
Course code for: [Build a Backend REST API with Python &amp; Django - Advanced](https://londonapp.dev/c2)

