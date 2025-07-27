# Vita Data - Healthcare Backend API


### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/vita-data-backend.git
   cd vita-data-backend
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   # Using conda (recommended)
   conda create -n vitadata python=3.10
   conda activate vitadata
   
   # Or using venv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

### Default Credentials

- **Superuser**: admin@test.com / admin123
- **Sample Doctor**: doctor1@example.com (role: DOCTOR)

## Authentication

The API uses JWT (JSON Web Token) authentication. Most endpoints require authentication except for user registration and login.

### Login

```http
POST /api/users/login/
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "password123"
}
```

**Response:**
```json
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Using Authentication

Include the access token in the Authorization header:
```http
Authorization: Bearer <your_access_token>
```

## API Endpoints

### Users

#### Register User
```http
POST /api/users/register/
Content-Type: application/json

{
    "email": "newuser@example.com",
    "password": "password123",
    "role": "RECEPTIONIST"
}
```

**Roles Available:**
- `ADMIN`: Full system access
- `DOCTOR`: Can manage patients and appointments
- `RECEPTIONIST`: Can manage patients and appointments
- `LAB`: Can manage lab reports

#### List Users (Admin Only)
```http
GET /api/users/users/
Authorization: Bearer <token>
```

### Patients

#### List Patients
```http
GET /api/patients/
Authorization: Bearer <token>
```

#### Create Patient
```http
POST /api/patients/
Authorization: Bearer <token>
Content-Type: application/json

{
    "name": "John Doe",
    "dob": "1990-01-01",
    "gender": "Male",
    "contact_number": "+1234567890",
    "email": "john.doe@example.com",
    "address": "123 Main St, City, State"
}
```

**Patient Model:**
- `name`: Patient's full name
- `dob`: Date of birth (YYYY-MM-DD)
- `gender`: Gender (Male/Female/Other)
- `contact_number`: Phone number
- `email`: Unique email address
- `address`: Full address

### Appointments

#### List/Create Appointments
```http
GET /api/appointments/appointments/
Authorization: Bearer <token>
```

**Query Parameters:**
- `doctor`: Filter by doctor ID
- `patient`: Filter by patient ID
- `date`: Filter by date (YYYY-MM-DD)

#### Create Appointment
```http
POST /api/appointments/appointments/
Authorization: Bearer <token>
Content-Type: application/json

{
    "patient": 1,
    "doctor": 2,
    "date": "2024-01-15",
    "time": "14:30:00",
    "issue": "Regular checkup"
}
```

**Appointment Model:**
- `patient`: Patient ID (required)
- `doctor`: Doctor ID (required, must be a user with DOCTOR role)
- `date`: Appointment date (YYYY-MM-DD)
- `time`: Appointment time (HH:MM:SS)
- `status`: Status (SCHEDULED/CANCELLED/COMPLETED)
- `issue`: Description of patient's issue

### Lab Reports

#### List Lab Reports
```http
GET /api/lab-reports/reports/
Authorization: Bearer <token>
```

**Query Parameters:**
- `report_date`: Filter by report date
- `status`: Filter by status (pending/in_progress/completed/scheduled)
- `patient`: Filter by patient ID
- `search`: Search in patient name or test type

#### Create Lab Report
```http
POST /api/lab-reports/reports/
Authorization: Bearer <token>
Content-Type: application/json

{
    "patient": 1,
    "test_type": "Blood Test",
    "status": "scheduled",
    "report_date": "2024-01-20"
}
```

#### Update Lab Report
```http
PUT /api/lab-reports/reports/{id}/
Authorization: Bearer <token>
Content-Type: application/json

{
    "patient": 1,
    "test_type": "Blood Test",
    "status": "completed",
    "result": "Normal",
    "remarks": "All parameters within normal range",
    "report_date": "2024-01-20"
}
```

**Lab Report Model:**
- `patient`: Patient ID (required)
- `test_type`: Type of lab test
- `status`: Status (pending/in_progress/completed/scheduled)
- `result`: Test results
- `remarks`: Additional notes
- `report_date`: Date of report
- `report_file`: Uploaded report file

### Billing

#### List Bills
```http
GET /api/billing/bills/
Authorization: Bearer <token>
```

#### Create Bill
```http
POST /api/billing/bills/
Authorization: Bearer <token>
Content-Type: application/json

{
    "bill_number": "BILL-2024-001",
    "patient": 1,
    "bill_amount": "150.00",
    "patient_status": "Unpaid"
}
```

#### Get Bill Details
```http
GET /api/billing/bills/{bill_number}/
Authorization: Bearer <token>
```

#### Update Bill
```http
PUT /api/billing/bills/{bill_number}/
Authorization: Bearer <token>
Content-Type: application/json

{
    "bill_number": "BILL-2024-001",
    "patient": 1,
    "bill_amount": "150.00",
    "patient_status": "Paid"
}
```

**Bill Model:**
- `bill_number`: Unique bill identifier (primary key)
- `patient`: Patient ID (required)
- `bill_amount`: Amount in decimal
- `patient_status`: Status (Paid/Unpaid/Pending)
- `bill_date`: Date of bill generation

### Dashboard

#### Dashboard Home
```http
GET /api/dashboard/
Authorization: Bearer <token>
```

## Data Models

### User Roles and Permissions

| Role | Permissions |
|------|-------------|
| ADMIN | Full system access, can view all users |
| DOCTOR | Manage patients, create appointments |
| RECEPTIONIST | Manage patients, create appointments |
| LAB | Manage lab reports |

### Status Values

**Appointment Status:**
- `SCHEDULED`: Appointment is scheduled
- `CANCELLED`: Appointment is cancelled
- `COMPLETED`: Appointment is completed

**Lab Report Status:**
- `pending`: Test is pending
- `in_progress`: Test is being processed
- `completed`: Test is completed
- `scheduled`: Test is scheduled

**Bill Status:**
- `Paid`: Bill has been paid
- `Unpaid`: Bill is unpaid
- `Pending`: Bill is pending payment

## Error Handling

The API returns standard HTTP status codes:

- `200`: Success
- `201`: Created
- `400`: Bad Request
- `401`: Unauthorized
- `403`: Forbidden
- `404`: Not Found
- `500`: Internal Server Error

**Error Response Format:**
```json
{
    "error": "Error message description"
}
```

## Development

### Branch Strategy

- Create feature branches for development
- No direct pushes to main branch
- Submit pull requests for code review

```bash
git checkout -b feature/your-feature-name
# Make your changes
git add .
git commit -m "Your commit message"
git push -u origin feature/your-feature-name
```

### Running Tests

```bash
python manage.py test
```

### Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
