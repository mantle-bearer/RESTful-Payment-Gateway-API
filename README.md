# RESTful Payment Gateway API for Small Businesses

## Overview

This project is a RESTful API built using Django REST Framework, designed to allow small businesses to accept payments from customers using the Paystack payment gateway. The API focuses on minimal customer information (name, email, amount) and supports versioning and automated CI/CD processes.

## Features

- Initiate payments using Paystack
- Retrieve payment status
- Automated testing and deployment with GitHub Actions

## Endpoints

### Initiate Payment

**Endpoint:** `POST /api/v1/payments`

**JSON Request Body:**

```json
{
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "amount": 50.0
}
```

**JSON Response:**

```json
{
  "reference": "unique-generated-reference",
  "data": {
    "status": true,
    "message": "Authorization URL created",
    "data": {
      "authorization_url": "https://paystack.com/pay/unique-generated-reference",
      "access_code": "unique-access-code",
      "reference": "unique-generated-reference"
    }
  }
}
```

### Retrieve Payment Status
**Endpoint:** `GET /api/v1/payments/{reference}`

**JSON Response:**

```json
{
  "payment": {
    "id": "PAY-123",
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "amount": 50.00,
    "status": "completed"
  },
  "status": "success",
  "message": "Payment details retrieved successfully."
}
```

## Setup and Installation
### Prerequisites
- Python 3.x

- Django

- Django REST Framework

- Paystack API

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/mantle-bearer/RESTful-Payment-Gateway-API.git
   cd RESTful-Payment-Gateway-API
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your environment variables:
   ```Plaintext
   PAYSTACK_SECRET_KEY=your_actual_paystack_secret_key
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```

7. Run the server:
   ```bash
   python manage.py runserver
   ```

## Running Tests
**Run the following command to execute tests:**
```bash
  python manage.py test
```

## CI/CD Setup
A GitHub Actions workflow is included to automate testing and deployment. The workflow file is located in `.github/workflows/django.yml`.

## Deployment
Deploy your application to a platform like PythonAnywhere, Vercel, Netlify Or Any Hosting Provider that can run a Python Application. Make sure your environment variables (e.g., `PAYSTACK_SECRET_KEY`) are securely set up in the deployment environment.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Django
- Django REST Framework
- Paystack

***By following these instructions and understanding this documentation, create a Django based, basic RESTful API that allows small businesses to accept payments from customers using Paystack Payment Gateway while focusing on minimal customer information (name, email, amount). You'll also be able to test your API in the development environment.***

***If you need any further assistance, feel free to ask! 😊🚀***

