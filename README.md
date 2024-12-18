# Django REST API: App Management

## Overview
This project provides a simple REST API to manage app information. It includes endpoints for adding, retrieving, and deleting app records.

## Requirements
- Python 3.x
- Django
- Django REST Framework

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd myapi
   ```

2. **Install dependencies:**
   ```bash
   pip install django djangorestframework
   ```

3. **Apply database migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

The server will start at `http://127.0.0.1:8000/`.

## API Endpoints

### 1. Add an App
- **URL:** `/api/add-app`
- **Method:** `POST`
- **Description:** Adds a new app to the database.
- **Sample Request Body:**
   ```json
   {
     "app_name": "SampleApp",
     "version": "1.0.0",
     "description": "This is a test app."
   }
   ```
- **Response:**
   ```json
   {
     "id": 1,
     "app_name": "SampleApp",
     "version": "1.0.0",
     "description": "This is a test app."
   }
   ```

### 2. Get App by ID
- **URL:** `/api/get-app/{id}`
- **Method:** `GET`
- **Description:** Retrieves app details by ID.
- **Response Example:**
   ```json
   {
     "id": 1,
     "app_name": "SampleApp",
     "version": "1.0.0",
     "description": "This is a test app."
   }
   ```

### 3. Delete App by ID
- **URL:** `/api/delete-app/{id}`
- **Method:** `DELETE`
- **Description:** Deletes an app record by ID.
- **Response:**
   ```json
   {
     "message": "App deleted successfully"
   }
   ```

## Testing
Use tools like **Postman** or **cURL** to test the API endpoints.

### Example cURL Commands

1. **Add an App:**
   ```bash
   curl -X POST http://127.0.0.1:8000/api/add-app \
   -H "Content-Type: application/json" \
   -d '{"app_name": "TestApp", "version": "2.0", "description": "A sample application."}'
   ```

2. **Get App by ID:**
   ```bash
   curl http://127.0.0.1:8000/api/get-app/1
   ```

3. **Delete App by ID:**
   ```bash
   curl -X DELETE http://127.0.0.1:8000/api/delete-app/1
   ```

## Database Management
- The database schema is automatically managed using Django ORM.
- By default, SQLite is used as the database. You can configure PostgreSQL in `settings.py` if needed.

## Notes
- Ensure all required dependencies are installed.
- Make sure the development server is running before testing the endpoints.

## License
This project is licensed under the MIT License.