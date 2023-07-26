# Redis-docker
This repository contains a 3-tier containerized Redis counter application.

Clone the repository
To clone this repository to your local machine, use the following command:
```
git clone https://github.com/manchal-02/redis-docker.git
```
### Build and Run the Application
After cloning the repository, navigate to the redis-docker directory using the terminal or command prompt. Then, run the following command to build and start the application using Docker Compose:
```
docker-compose up --build
```
The docker-compose up --build command will create and run three separate containers for Redis, Python app, and the frontend. The Python app will be accessible at http://localhost:8000, and the frontend will be accessible at http://localhost.

Feel free to interact with the application and test its functionalities.
