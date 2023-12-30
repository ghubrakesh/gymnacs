# Gymnacs

This repository contains a CRUD API for a gym management system built using Django REST Framework. The API allows users to manage gyms, trainers, clients, and workout sessions.

## Test the APIs with Postman
- [Projetct's Postman Collection](https://www.postman.com/payload-geologist-61696866/workspace/gym-mgmt)  (public)

- [Postman Documentation](https://github.com/ghubrakesh/gymnacs) (to be completed yet)


## Structure

The project structure is organized as follows:

- `api`: Contains URL configurations for the API.
- `gym`: Main project settings, URL configurations, and deployment files.
- `app`: Core application logic, including models, views, serializers, and custom authentication.

## Key Components

### Models (`models.py`)
- Defines database structure for Gym, Trainer, Client, and WorkoutSession entities.
- Establishes relationships between entities.

### Serializers (`serializers.py`)
- Converts data types (models) into JSON format and vice versa using Django REST Framework's ModelSerializer.
- Handles serialization/deserialization for API endpoints.

### Views and ViewSets (`views.py`)
- Manages CRUD operations for each model using Django REST Framework's ModelViewSet.
- Customizes error handling and permissions for specific endpoints.

### URLs (`urls.py`)
- Defines URL patterns for API endpoints.
- Routes requests to corresponding views and ViewSets.

### Other Components
- `settings.py`: Project-level configurations for database, middleware, installed apps, authentication, etc.
- `admin.py`: Registers models with Django's admin interface.
- `auth.py`: Contains custom permission classes for authentication.

---

## To install and test the APIs locally
1. Clone the repository:
  ```
  git clone https://github.com/sachin-404/gym-management-system-api.git
  ```
3. Create a virtual environment:
  ```
  python3 -m venv venv
  ```

5. Activate the virtual environment:
- linux:
  ```
  source venv/bin/activate
  ```
- Windows:
  ```
  venv\Scripts\activate
  ```

4. Install dependencies:
  ```
  pip install -r requirements.txt
  ```

6. Apply migrations:
  ```
  python manage.py migrate
  ```

8. Run the development server:
  ```
  python manage.py runserver
  ```
## API Endpoints

- `/gyms/`: CRUD operations for gyms.
- `/trainers/`: CRUD operations for trainers.
- `/clients/`: CRUD operations for clients.
- `/workouts/`: CRUD operations for workout sessions.

---
## My Work

### Model Implementations
- Implemented Gym, Trainer, Client, and WorkoutSession models as per the requirements.
- Established appropriate relationships between the models.

### Serializers
- Created GymSerializer, TrainerSerializer, ClientSerializer, WorkoutSessionSerializer for data validation and JSON conversion.

### API Views
- Implemented API views using Django REST Framework's ModelViewSet.
- Defined queryset and serializer classes for each view.

### API Endpoints
- Configured API URLs for CRUD operations on gyms, trainers, clients, and workout sessions.
- Named the API URLs appropriately.

### Documentation
- Created comprehensive API documentation detailing available endpoints, request/response formats, and authentication (if any).

### Authentication and Permissions (Bonus)
- Implemented token-based authentication for the API.
- Configured permissions to restrict access to specific endpoints based on roles (e.g., trainers modifying workout sessions).

### Handling Edge Cases
- Implemented robust error handling, returning appropriate HTTP status codes and error messages for various scenarios (e.g., invalid input, non-existent resources).

### Postman Collection
- Provided a Postman collection containing requests for all API endpoints.
- Shared the Postman collection to facilitate testing and validation of the API endpoints.

This project's analogy considers the Gym as the blog platform, Trainers as Authors, Clients as Users, and WorkoutSessions as Posts. The relationship between Trainer and Gym represents a 1:1 relationship, while the relationship between Client and WorkoutSession represents a 1:n relationship.


---
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](link-to-license).
