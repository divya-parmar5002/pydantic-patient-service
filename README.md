# Pydantic Patient Service

A backend-focused Python project built using Pydantic for robust patient data validation, serialization, and business rule enforcement.

This project demonstrates how modern backend systems validate and process structured healthcare-related data using strongly typed schemas, nested models, custom validators, computed fields, and JSON serialization.

---

## Features

- Strong data validation using Pydantic
- Nested models for structured address handling
- Email validation with custom domain checking
- Business rule validation using model validators
- Computed BMI calculation
- JSON serialization support
- Clean modular backend architecture
- Type-safe schema definitions
- Field metadata and constraints

---

## Project Structure

```text
pydantic-patient-service/
│
├── main.py
│
├── models/
│   ├── patient.py
│   └── address.py
│
├── services/
│   └── patient_services.py
│
├── requirements.txt
│
└── README.md
```

---

## Technologies Used

- Python
- Pydantic v2
- Type Hints
- Data Validation
- Object Serialization

---

## Concepts Implemented

### Pydantic Features
- BaseModel
- Field Constraints
- Annotated Types
- Nested Models
- Computed Fields
- Field Validators
- Model Validators
- JSON Serialization
- Type Coercion

### Backend Engineering Concepts
- Schema Validation
- Business Rule Enforcement
- Clean Service Layer Architecture
- Data Processing
- Structured API-ready Models

---

## Example Validations

### Email Domain Validation
Only approved domains such as `gmail.com` are allowed.

### Emergency Contact Validation
Patients older than 60 must provide an emergency contact number.

### BMI Calculation
BMI is automatically computed using:
```python
BMI = weight / (height²)
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows
```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python main.py
```

---

## Example Output

```python
Divya
21
{'phone': '1234567890', 'emergency': '9876544563'}
city='Mumbai' state='Maharastra' pin='123456' country='India'
21.39
```

---

## Learning Outcome

This project was created to strengthen backend engineering fundamentals including:

- Data modeling
- Validation architecture
- Service-based design
- Type-safe Python development
- Real-world schema handling

---

## Author

Divya Parmar