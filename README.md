# Personal Stock Tracker Backend

This backend application serves as a robust personal stock tracker, built using Python, Flask, SQL, and Peewee ORM. It provides full CRUD (Create, Read, Update, Delete) functionality for managing stocks.

## Features

- **CRUD Operations:** Perform Create, Read, Update, and Delete operations on stock data.
- **Flexible API Endpoints:** Well-defined API endpoints for easy integration with front-end or other services.
- **Efficient Database Handling:** Uses SQL and Peewee ORM for seamless database interactions.

## Tech Stack

- **Python**: Programming language used for the backend logic.
- **Flask**: Web framework for building RESTful APIs.
- **SQL**: Database management system for storing stock data.
- **Peewee**: Lightweight ORM for interacting with the database.

## API Endpoints

GET /stocks: Retrieve all stocks.
GET /stocks/{stock_id}: Retrieve a specific stock by ID.
POST /stocks: Add a new stock.
PUT /stocks/{stock_id}: Update an existing stock.
DELETE /stocks/{stock_id}: Delete a stock.

## Author

Mike Fox
