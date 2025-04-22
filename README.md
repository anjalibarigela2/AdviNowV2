# AdviNow Interview Challenge

It uses **FastAPI**, **SQLAlchemy**, **Alembic**, and **PostgreSQL** to simulate importing and querying business + symptom data.

FastAPI automatically generates interactive API documentation at: 

🔗 [http://127.0.0.1:8013/docs]

## Setup Instructions

## **Create a virtual environment and install the requirements - "requirements\requirements.txt"**

## 1. Clone the Repository

git clone https://gitfront.io/r/user-8330764/24pYzvQfcYBi/interview-challenge-v2.git

cd AdviNowV2-master

## 2. Create and Activate Virtual Environment

python -m venv venv

venv\Scripts\activate     # Windows
<br> or <br/>
source venv/bin/activate    # macOS/Linux

## 3. Install Requirements

pip install -r requirements/requirements.txt


## **Create data models - example with sqlalchemy in "app\models.py"**

Defined three core models using SQLAlchemy:
Business: Stores business name and ID
Symptom: Stores symptom code and name
BusinessSymptom: Association table connecting businesses to symptoms with a diagnostic label

## 4. Set Environment Variables

Edit the .env file in the project root with:

DB_HOST=127.0.0.1
DB_NAME=Database_name
DB_USER=postgres
DB_PWD=your_password_here

## **Generate migration script and run migration to create database tables - alembic files provided**
  - To create a migration file: "alembic revision --autogenerate -m some_comment"
  - To update database with migration file: "alembic upgrade head"

## 1. Generate a Migration File

python -m alembic revision --autogenerate -m "initial tables"

## 2. Apply Migration to Create Tables

python -m alembic upgrade head

## Running the App

python -m app.run

## **Create an endpoint that returns business and symptom data**
  - Endpoint should take two optional parameters - business_id & diagnostic
  - Endpoint should return Business ID, Business Name, Symptom Code, Symptom Name, and Symptom Diagnostic values based on filter

Open Swagger UI: http://127.0.0.1:8013/docs

Use /import-csv/ to upload your CSV file

Use /symptoms/ to fetch and filter symptom data
