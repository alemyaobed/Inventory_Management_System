# Inventory Management System

## Overview

The Inventory Management System (IMS) is a web application designed to efficiently track stock levels, manage products, suppliers, and orders. It is built using FastAPI for the API layer, PostgreSQL for the database, and Celery with RabbitMQ for background job processing. The system is deployed on AWS with SSL encryption to ensure secure communication.

## Features

- **Product Management**: Create, read, update, and delete products.
- **Supplier Management**: Manage suppliers and their details.
- **Order Management**: Track and manage orders between products and suppliers.
- **Background Processing**: Handle high-volume data uploads asynchronously with Celery and RabbitMQ.
- **Secure Deployment**: Deployed on AWS with SSL encryption using Certbot.

## Technologies

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **Asynchronous Tasks**: Celery
- **Message Broker**: RabbitMQ
- **Deployment**: AWS
- **SSL/TLS Encryption**: Certbot

## Installation

### Clone the Repository

```bash
git clone https://github.com/alemyaobed/Inventory_Management_System.git
cd Inventory_Management_System
```

### Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory with the following variables:

```ini
DATABASE_URL=postgresql://username:password@localhost/dbname
CELERY_BROKER_URL=pyamqp://guest@localhost//
SECRET_KEY=your-secret-key
```

### Initialize Database

Run the Alembic migrations to set up the database schema:

```bash
alembic upgrade head
```

### Run the Application

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

### Start Celery Worker

In a separate terminal, start the Celery worker:

```bash
celery -A app.tasks.celery_app worker --loglevel=info
```

## Deployment

### Docker

To build and run the application using Docker, navigate to the `docker/` directory and use Docker Compose:

```bash
docker-compose up --build
```

### AWS Deployment

Follow these steps to deploy the application on AWS:
1. **Launch an EC2 instance** and install the necessary dependencies.
2. **Set up PostgreSQL on RDS** and configure the database connection.
3. **Configure Nginx** to handle SSL using Certbot for HTTPS support.
4. **Deploy the FastAPI application** on the EC2 instance.

## API Endpoints

- **`POST /products/`**: Create a new product.
- **`GET /products/{id}`**: Retrieve a product by ID.
- **`PUT /products/{id}`**: Update a product by ID.
- **`DELETE /products/{id}`**: Delete a product by ID.
- **`POST /suppliers/`**: Create a new supplier.
- **`GET /suppliers/{id}`**: Retrieve a supplier by ID.
- **`PUT /suppliers/{id}`**: Update a supplier by ID.
- **`DELETE /suppliers/{id}`**: Delete a supplier by ID.
- **`POST /orders/`**: Create a new order.
- **`GET /orders/{id}`**: Retrieve an order by ID.

## Testing

To run the test suite, use:

```bash
pytest
```

## Contributing

Feel free to open issues or submit pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- FastAPI
- PostgreSQL
- Celery
- RabbitMQ
- Docker
- AWS
- Certbot

For further information or questions, please contact [alemyaobed@gmail.com](mailto:alemyaobed@gmail.com).
