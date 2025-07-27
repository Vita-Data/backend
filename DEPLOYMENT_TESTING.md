# Deployment Testing Guide

This document provides testing examples and documentation for the deployed Vita Data Healthcare Backend API.

**Live API URL**: https://backend-k5a7.onrender.com/

## Quick Start

### Base URL
```
https://backend-k5a7.onrender.com
```

### Authentication
The API uses JWT authentication. Get your access token by logging in:

```bash
curl -X POST https://backend-k5a7.onrender.com/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@test.com",
    "password": "admin123"
  }'
```

## API Testing Examples

### 0. User Creation
```bash
curl -X POST https://backend-k5a7.onrender.com/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123",
    "role": "ADMIN"
  }'
```
### 1. User Authentication

#### Login
```bash
curl -X POST https://backend-k5a7.onrender.com/api/users/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123"
  }'
```

**Expected Response:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

#### Register New User
```bash
curl -X POST https://backend-k5a7.onrender.com/api/users/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newdoctor@example.com",
    "password": "password123",
    "role": "DOCTOR"
  }'
```

### 2. Patient Management

#### List All Patients
```bash
curl -X GET https://backend-k5a7.onrender.com/api/patients/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Create New Patient
```bash
curl -X POST https://backend-k5a7.onrender.com/api/patients/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Smith",
    "dob": "1985-03-15",
    "gender": "Male",
    "contact_number": "+1234567890",
    "email": "john.smith@example.com",
    "address": "123 Oak Street, City, State 12345"
  }'
```

### 3. Appointment Management

#### List Appointments
```bash
curl -X GET https://backend-k5a7.onrender.com/api/appointments/appointments/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Filter Appointments by Date
```bash
curl -X GET "https://backend-k5a7.onrender.com/api/appointments/appointments/?date=2024-01-15" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Create Appointment
```bash
curl -X POST https://backend-k5a7.onrender.com/api/appointments/appointments/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "patient": 1,
    "doctor": 2,
    "date": "2024-01-20",
    "time": "14:30:00",
    "issue": "Regular health checkup"
  }'
```

### 4. Lab Reports

#### List Lab Reports
```bash
curl -X GET https://backend-k5a7.onrender.com/api/lab-reports/reports/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Filter Lab Reports by Status
```bash
curl -X GET "https://backend-k5a7.onrender.com/api/lab-reports/reports/?status=completed" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Create Lab Report
```bash
curl -X POST https://backend-k5a7.onrender.com/api/lab-reports/reports/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "patient": 1,
    "test_type": "Blood Test",
    "status": "scheduled",
    "report_date": "2024-01-25"
  }'
```

#### Update Lab Report
```bash
curl -X PUT https://backend-k5a7.onrender.com/api/lab-reports/reports/1/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "patient": 1,
    "test_type": "Blood Test",
    "status": "completed",
    "result": "Normal",
    "remarks": "All parameters within normal range",
    "report_date": "2024-01-25"
  }'
```

### 5. Billing

#### List Bills
```bash
curl -X GET https://backend-k5a7.onrender.com/api/billing/bills/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Create Bill
```bash
curl -X POST https://backend-k5a7.onrender.com/api/billing/bills/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bill_number": "BILL-2024-001",
    "patient": 1,
    "bill_amount": "150.00",
    "patient_status": "Unpaid"
  }'
```

#### Get Bill Details
```bash
curl -X GET https://backend-k5a7.onrender.com/api/billing/bills/BILL-2024-001/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Update Bill Status
```bash
curl -X PUT https://backend-k5a7.onrender.com/api/billing/bills/BILL-2024-001/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bill_number": "BILL-2024-001",
    "patient": 1,
    "bill_amount": "150.00",
    "patient_status": "Paid"
  }'
```

### 6. Dashboard

#### Dashboard Home
```bash
curl -X GET https://backend-k5a7.onrender.com/api/dashboard/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

## Testing with Postman

### Import Collection
You can import these endpoints into Postman for easier testing:

1. Create a new collection in Postman
2. Set the base URL variable: `{{base_url}}` = `https://backend-k5a7.onrender.com`
3. Set the auth token variable: `{{auth_token}}` = `your_jwt_token`

### Postman Environment Variables
```json
{
  "base_url": "https://backend-k5a7.onrender.com",
  "auth_token": "your_jwt_token_here"
}
```

## Testing with JavaScript/Fetch

### Authentication Example
```javascript
// Login
const loginResponse = await fetch('https://backend-k5a7.onrender.com/api/users/login/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    email: 'admin@test.com',
    password: 'admin123'
  })
});

const loginData = await loginResponse.json();
const token = loginData.access;

// Use token for authenticated requests
const patientsResponse = await fetch('https://backend-k5a7.onrender.com/api/patients/', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
```

### Create Patient Example
```javascript
const createPatient = async (patientData, token) => {
  const response = await fetch('https://backend-k5a7.onrender.com/api/patients/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify(patientData)
  });
  
  return await response.json();
};

// Usage
const newPatient = await createPatient({
  name: "Jane Doe",
  dob: "1990-05-20",
  gender: "Female",
  contact_number: "+1987654321",
  email: "jane.doe@example.com",
  address: "456 Pine Avenue, City, State 54321"
}, token);
```

## Testing with Python/Requests

### Python Example
```python
import requests

BASE_URL = "https://backend-k5a7.onrender.com"

# Login
login_data = {
    "email": "admin@test.com",
    "password": "admin123"
}

response = requests.post(f"{BASE_URL}/api/users/login/", json=login_data)
token = response.json()["access"]

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Get patients
patients_response = requests.get(f"{BASE_URL}/api/patients/", headers=headers)
patients = patients_response.json()

# Create appointment
appointment_data = {
    "patient": 1,
    "doctor": 2,
    "date": "2024-01-20",
    "time": "14:30:00",
    "issue": "Regular checkup"
}

appointment_response = requests.post(
    f"{BASE_URL}/api/appointments/appointments/", 
    json=appointment_data, 
    headers=headers
)
```

## Health Check

### API Status
```bash
curl -X GET https://backend-k5a7.onrender.com/api/dashboard/
```

**Expected Response:**
```json
{
  "message": "Dashboard is working"
}
```

## Error Handling

### Common Error Responses

**401 Unauthorized:**
```json
{
  "detail": "Authentication credentials were not provided."
}
```

**403 Forbidden:**
```json
{
  "error": "Only Admin can view users"
}
```

**400 Bad Request:**
```json
{
  "email": ["This field is required."],
  "password": ["This field is required."]
}
```
