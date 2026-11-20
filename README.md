# Student Management REST API

A beginner-friendly REST API project built using **Python and Flask** to perform CRUD (Create, Read, Update, Delete) operations on student records using HTTP methods.

## About the Project

This project demonstrates how REST APIs work using Flask. It provides API endpoints to create, retrieve, update, partially update, and delete student information.

## Technologies Used

- Python
- Flask
- REST API
- JSON
- Postman
- Git & GitHub

## HTTP Methods Implemented

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/students` | Retrieve all students |
| POST | `/students` | Create a new student |
| PUT | `/students/<student_id>` | Update complete student details |
| PATCH | `/students/<student_id>` | Update specific student fields |
| DELETE | `/students/<student_id>` | Delete a student |

## Project Structure

```text
student-management-rest-api/
│
├── http_get_method/
│   └── app.py
│
├── http_post_method/
│   └── app.py
│
├── http_put_method/
│   └── app.py
│
├── http_patch_method/
│   └── app.py
│
├── http_delete_method/
│   └── app.py
│
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Prasanna-20740/student-management-rest-api.git
```

### 2. Navigate to the project folder

```bash
cd student-management-rest-api
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Flask

```bash
pip install flask
```

## Running the Application

Each HTTP method has a separate practice folder containing an `app.py` file.

Example: To run the PATCH API:

```bash
cd http_patch_method
python app.py
```

The Flask development server runs at:

```text
http://127.0.0.1:5000
```

Follow the same steps for the other HTTP method folders.

## API Testing with Postman

Use Postman to test the API endpoints.

### 1. GET – Retrieve Students

**Method:** GET

```text
http://127.0.0.1:5000/students
```

Returns the list of all students.

### 2. POST – Create Student

**Method:** POST

```text
http://127.0.0.1:5000/students
```

**Request Body (JSON):**

```json
{
    "name": "Rahul",
    "course": "Django"
}
```

Expected status: `201 Created`

### 3. PUT – Update Student

**Method:** PUT

```text
http://127.0.0.1:5000/students/1
```

**Request Body (JSON):**

```json
{
    "name": "Prasanna P",
    "course": "Python Full Stack"
}
```

Expected status: `200 OK`

### 4. PATCH – Partially Update Student

**Method:** PATCH

```text
http://127.0.0.1:5000/students/1
```

**Request Body (JSON):**

```json
{
    "name": "Prasanna P"
}
```

Only the provided field is updated. Other fields remain unchanged.

Expected status: `200 OK`

### 5. DELETE – Delete Student

**Method:** DELETE

```text
http://127.0.0.1:5000/students/1
```

Deletes the student with the specified ID.

Expected status: `200 OK`

## HTTP Status Codes

| Status Code | Description |
|---|---|
| 200 | OK – Request successful |
| 201 | Created – New student created |
| 400 | Bad Request – Invalid request data |
| 404 | Not Found – Student does not exist |
| 415 | Unsupported Media Type – Incorrect content type |
| 500 | Internal Server Error |

## Key Learning Outcomes

- Understanding REST API concepts.
- Working with HTTP methods: GET, POST, PUT, PATCH and DELETE.
- Creating API endpoints using Flask.
- Handling JSON request and response data.
- Understanding HTTP status codes.
- Testing REST APIs using Postman.
- Managing projects using Git and GitHub.

## Important Note

This is a beginner practice project. Student records are stored in a Python list (in-memory storage), not in a database. Therefore, changes are reset when the Flask server restarts.

## Author

**Prasanna P**

GitHub: https://github.com/Prasanna-20740

Project Repository: https://github.com/Prasanna-20740/student-management-rest-api
