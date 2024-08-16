# 7Dliving
# FastAPI CRUD User Service

## Overview

This project is a backend service built with FastAPI to handle CRUD (Create, Read, Update, Delete) operations for user details. It provides endpoints to add, retrieve, search, update, and delete user records. The project includes pagination for retrieving users and supports search functionality based on user name or email.

## Features

- Add a new user
- Retrieve user details with pagination
- Search for users by name or email
- Update user details
- Delete a user
- Error handling and validation

## Prerequisites

- Python VsCode must be installed on your system.
- **pip** (Python package installer) should be available.
- pip install fastapi uvicorn


## Create a virtual environment:
python -m venv venv

## Running the Application
uvicorn main:app --reload

## API Endpoints
1. Add a New User
Request:
{
    "name": "pranay k",
    "email": "pranay@gmail,com.com",
    "age": 30
}
Response:

{
    "user_id": "123254",
    "user": {
        "name": "pranay k",
        "email": "pranay@gmail.com",
        "age": 30
    }
}

## Retrieve Users with Pagination
GET
page: Page number (default: 1)
limit: Number of users per page (default: 10)
Response:

    {
        "name": "pranay k",
        "email": "pranay@gmail.com.com",
        "age": 30
    },
    {
        "name": "Arush ",
        "email": "arush@gmail.com.com",
        "age": 25
    }

## Search for Users

    {
        "name": "pranay k",
        "email": "pranay@gmail.com.com",
        "age": 30
    }
    
## Update User Details
{
    "name": "pranay kurangi",
    "email": "pranay.kurangi@gmail.com",
    "age": 31
}
## Delete a User
user_id: ID of the user to delete (required)
{
    "detail": "User deleted"
}

    
## Testing the API
FastAPI auto-generated documentation by navigating to http://127.0.0.1:8000/docs or http://127.0.0.1:8000/redoc



```bash
git clone https://github.com/pranay8k/7dliving.git
cd fastapi-crud-users
