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

**Request Body:**

```json
{
  "customer_name": "John Doe",
  "customer_email": "john@example.com",
  "amount": 50.0
}
```
