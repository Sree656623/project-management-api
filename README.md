# Project Management API

This is a Django-based API designed to manage projects, tasks, and user interactions within a project management system. The application includes features like user authentication, task assignments, project management, and comment tracking.

## Features

- *User Management*: Allows registration, login, and user profile management.
- *Project Management*: Create, update, delete, and view project details.
- *Task Management*: Assign tasks to users, update task statuses, and prioritize tasks.
- *Comments*: Add comments to tasks for discussions and updates.

## Technologies Used

- *Django*: Python web framework for building the API.
- *Django Rest Framework (DRF)*: Used for building RESTful APIs.
- *Swagger UI*: Used for automatic API documentation and testing.
- *PostgreSQL/MySQL*: Database for storing project and task data (depending on your setup).
- *JWT Authentication*: Secure API with JSON Web Token for user authentication.

## API Endpoints

### User Management

- *User Registration*:  
  *POST* /api/register/  
  Register a new user by providing username, email, and password.

- *Login*:  
  *POST* /api/login/  
  Login to the system using username and password to receive a JWT token.

- *Profile*:  
  *GET* /api/profile/  
  Retrieve the logged-in user's profile details. Requires authentication.

### Project Management

- *List Projects*:  
  *GET* /api/projects/  
  List all projects.

- *Create Project*:  
  *POST* /api/projects/  
  Create a new project by providing project details.

- *Update Project*:  
  *PUT* /api/projects/{id}/  
  Update a project by ID. Requires authentication.

- *Delete Project*:  
  *DELETE* /api/projects/{id}/  
  Delete a project by ID. Requires authentication.

### Task Management

- *List Tasks*:  
  *GET* /api/tasks/  
  List all tasks.

- *Create Task*:  
  *POST* /api/tasks/  
  Create a new task and assign it to a user.

- *Update Task*:  
  *PUT* /api/tasks/{id}/  
  Update a task by ID.

- *Delete Task*:  
  *DELETE* /api/tasks/{id}/  
  Delete a task by ID.

### Comment Management

- *List Comments*:  
  *GET* /api/comments/  
  List all comments on tasks.

- *Add Comment*:  
  *POST* /api/comments/  
  Add a comment to a task for updates or discussions.

## Setup Instructions

### Clone the Repository

To get started with the project, clone the repository:

git clone https://github.com/Sree656623/project-management-api

## Links

- *GitHub Repository*: [https://github.com/Sree656623/project-management-api](https://github.com/Sree656623/project-management-api)
- *Swagger UI*: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)