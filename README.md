# 12FactorApp

This project is a demo implementation of [12-Factor App](https://12factor.net/). It consists of:

- A **FastAPI** backend that serves a machine learning model.
- A **Flutter** frontend that interacts with the backend to provide a simple user interface.
- A **MySQL** database to import the dataset and to store the model.
- Environment-based configuration using a `.env` file.
- Docker support for easy deployment and consistency across environments.

---

## Features

- **Machine Learning Model**: Built using `scikit-learn`.
- **FastAPI Backend**:
  - Connects to a MySQL database.
  - Loads and uses the trained ML model.
  - Exposes a POST endpoint to make predictions.
- **Flutter Frontend**:
  - Simple UI for users to input data.
  - Sends requests to the backend and displays the response.
- **12-Factor Compliance**:
  - Config via `.env`.
  - Shows Logs:
    ![image](https://github.com/user-attachments/assets/a85c7874-e344-4439-baf4-6c3e7ada28fe)
  - Tested using **Pytest**:
    ![image](https://github.com/user-attachments/assets/0aa8ef63-c106-4e34-aefd-7e16e738d34d)

---

## Video Demo:
https://youtu.be/ZXhfa5UX73c

## Installation & Usage

### 1. Clone the repository and create a python virtual environment.

```bash
git clone https://github.com/upahar-khatiwada/12-Factor-App.git
cd 12-Factor-App

python -m venv env
env/scripts/activate
```

### 2. Set up the database by the provided **test.sql** file

```bash 
mysql -u root -p test < test.sql
```

### 3. Set up .env file at root directory

```bash
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=

API_URL=
HOST=
PORT=
```

### 4. Run either with docker or locally.

```bash
cd backend
docker-compose up --build
```

### 5. For running the flutter frontend, create a .env file at flutter's root directory as following:
```bash
API_URL=
```

### 6. To run the backend locally, simply configure the .env file as per need and run the following command.

```bash
cd backend
python api_creation.py
```

