# Hello World Web Application

This is a simple 'Hello World' web application built with Python and Flask, containerized using Docker, and deployed to AWS using AWS CDK.

## Prerequisites

- AWS CLI configured with your credentials
- AWS CDK installed
- Docker installed
- GitHub repository with the application code

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your-github-username/your-repo-name.git
    cd your-repo-name
    ```

2. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Build the Docker image:
    ```sh
    docker build -t hello-world-app .
    ```

4. Run the Docker container:
    ```sh
    docker run -p 80:80 hello-world-app
    ```

5. Deploy the application to AWS:
    ```sh
    cdk deploy
    ```

## CI/CD Pipeline

The CI/CD pipeline is set up using AWS CodePipeline. It automatically builds and deploys the application when changes are pushed to the GitHub repository.
