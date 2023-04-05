# Fraud-Detection-MLops-Project-
The following files are present in the repository:

**.gitignore**
A file that specifies which files and directories should be ignored by Git when committing changes to the repository.

**Dockerfile**
A file specifying the steps to build a Docker container for the application. The file sets up the container with the necessary dependencies, copies over the application code, and specifies the command to run the Flask application.

**main.py**
The main Python file for the Flask application, containing the prediction code.

**requirements.txt**
A file specifying the required Python packages for the application, which can be installed with pip.

**.gitlab-ci.yml**
A configuration file for GitLab CI/CD, which specifies the stages of the pipeline, the Docker image to use, and the steps to build and deploy the application.

**GitLab Setup**
To set up the project on GitLab and run the CI/CD pipeline, follow these steps:

Create a new project on GitLab.
Clone the repository to your local machine.
Add the .gitlab-ci.yml file to the root directory of the project.
Push the changes to the GitLab repository.
Navigate to the project's CI/CD settings on GitLab and ensure that CI/CD is enabled.
Create a new Docker registry on GitLab and add the login credentials to the CI/CD settings.
Push a new commit to the repository to trigger the CI/CD pipeline.
The pipeline will build a Docker image of the application and push it to the GitLab registry. You can then deploy the image to a server or container platform of your choice.
