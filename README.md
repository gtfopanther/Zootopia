# Zootopia – Animal Website Generator

Zootopia is a Python-based project that generates a simple HTML website displaying information about animals.
The data is fetched dynamically from the API Ninjas Animals API based on user input.

The project demonstrates a clean separation of concerns:
- Data fetching (API communication)
- Website generation (HTML creation)

This makes the code modular, easy to extend, and easy to maintain.

---

## Features

- Fetches real animal data from an external API
- Generates a styled HTML website (`animals.html`)
- Handles invalid or unknown animal names gracefully
- Uses environment variables to keep API keys secure
- Modular multi-file architecture

---

## Project Structure

Zootopia/
│
├── animals_web_generator.py # Website generator
├── data_fetcher.py # Data fetching logic (API)
├── animals_template.html # HTML template
├── requirements.txt # Project dependencies
├── .env # Environment variables (ignored by Git)
├── .gitignore # Git ignore rules
└── README.md # Project documentation


---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/gtfopanther/Zootopia.git
cd Zootopia

Create a virtual environment
python -m venv .venv

Install dependencies
pip install -r requirements.txt

Create a .env file in the root directory and add your API Ninjas key:
API_KEY=your_api_key_here

Run the website generator:
python animals_web_generator.py
You will be prompted to enter an animal name:
Please enter an animal: Fox
