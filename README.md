
# Finance API

This project is a role-based financial management backend API built using Django REST Framework.
It allows users to manage financial records (income/expenses) with role-based access control and provides dashboard analytics.



## Setup Process

1. Clone the repository

```bash
git clone <https://github.com/vishwasferwani/Finance-API>
cd finance_project
```

2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Create superuser
```bash
python manage.py createsuperuser
```
6. Run the server
```bash
python manage.py runserver
```



## API Explanation
### Authentication
-  Session-based authentication is used

- Login via /login/

```bash
Json Format
{
  "username": "analyst1",
  "password": "12345"
}
```
## User APIs

| Method | Endpoint                  | Description              |
| ------ | ------------------------- | ------------------------ |
| POST   | `/api/users/create/`      | Create user (Admin only) |
| GET    | `/api/users/list/`        | List all users           |
| PUT    | `/api/users/update/<id>/` | Update user (Admin only)    |
| DELETE | `/api/users/delete/<id>/` | Delete user (Admin only)    |

### Create User (JSON)
``` 
{
  "username": "analyst1",
  "password": "12345", 
  "role": "analyst", 
  "is_active": true
}
```
| Field     | Required |
| --------- | -------- |
| username  | ✅        |
| password  | ✅        |
| role      | ✅        |
| is_active | ❌        |

### Update User (JSON)
```
{
  "username": "analyst1",
  "password": "12345",
  "role": "admin",
  "is_active": true
}
```
### Delete User (JSON)
```DELETE /api/users/delete/1/```

## Record APIs

| Method | Endpoint            | Description                                     |
| ------ | ------------------- | ----------------------------------------------- |
| POST   | `/api/records/create/`      | Create record (Admin only)                      |
| GET    | `/api/records/list/`        | List records (with filters, search, pagination) |
| PUT    | `/api/records/update/<id>/` | Update record    (Admin only)                               |
| DELETE | `/api/records/delete/<id>/` | Delete record      (Admin only)                             |

### Create Record (JSON)
```
{
  "amount": 500,
  "type": "expense",
  "category": "Food",
  "date": "2026-04-02",
  "note": "Lunch"
}
```
### ⚠️ Notes
- Password is write-only and not returned in response
- Type must be either "income" or "expense"
- Date format must be YYYY-MM-DD
### Update Record (JSON)
```
{
  "amount": 700,
  "type": "expense",
  "category": "Food",
  "date": "2026-04-02",
  "note": "Dinner"
}
```
### Delete Record
``` DELETE /api/records/delete/1/ ```

## Dashboard API
| Method | Endpoint          | Description                            |
| ------ | ----------------- | -------------------------------------- |
| GET    | `/api/dashboard/` | Returns summary, category data, trends (Admin/Analyst only) |

##  🎯Filtering
```bash
/api/records/list/?category=Food
/api/records/list/?type=expense
/api/records/list/?start_date=2026-04-01&end_date=2026-04-30
```

## 🔍search
```bash
/api/records/list/?search=food
```

## 🧑‍💻 Role-Based Access
| Role    | Permissions             |
| ------- | ----------------------- |
| Viewer  | Read-only access        |
| Analyst | Read + dashboard access |
| Admin   | Full CRUD + dashboard access     |


## 🧪 Testing

### Unit tests for serializer validation (e.g., negative amount, missing fields)

To run tests, run the following command

```bash
  python manage.py test
```

## 🚀 Future Improvements
Add JWT Authentication

Use django-filter for advanced filtering

Add pagination customization

Add frontend (React)
