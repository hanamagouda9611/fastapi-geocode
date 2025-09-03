# FastAPI Geocode Service

A lightweight geocoding API built with **FastAPI** that supports both **forward geocoding** (address ➝ coordinates) and **reverse geocoding** (coordinates ➝ address).  
Data is stored in a database for persistence and faster lookups.

---

## Features

- 🌍 **Forward Geocoding** – Convert an address or place name into latitude & longitude.
- 📍 **Reverse Geocoding** – Convert latitude & longitude into an address.
- 🗄 **Database Support** – Store geocoded results for caching and analytics.
- ⚡ **FastAPI** – Async, production-ready API.
- 🧪 Built-in interactive docs with Swagger (`/docs`) and ReDoc (`/redoc`).

---

## Project Structure
```
fasapi-geocode/
│── database.py           # Database connection and ORM models
│── forward.py            # Forward geocoding logic
│── reverse.py            # Reverse geocoding logic
│── main.py               # FastAPI entry point
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
```
---

## Installation

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/fasapi-geocode.git
cd fasapi-geocode
```
2. Create and activate virtual environment
 ```bash
 python -m venv venv
 source venv/bin/activate   # Mac/Linux
 venv\Scripts\activate      # Windows
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the App

Start the FastAPI server with Uvicorn:
```bash
uvicorn main:app --reload
```
