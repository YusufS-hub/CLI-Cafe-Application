
# Cafe CLI Application

Welcome to the Cafe CLI Application! This is a full-featured command-line interface (CLI) app for managing a pop-up cafe, built as a Python learning project.

## Features
- Product management: Add, view, update, and delete products
- Order management: Create, view, update, and delete customer orders
- Courier management: Add, view, update, and delete couriers
- Data persistence using CSV files
- User-friendly CLI menus and ASCII art

## Project Structure
```
Cafe App/
├── data/
│   ├── couriers.csv
│   ├── orders.csv
│   ├── products-database.sql
│   └── products.csv
├── notes/
│   └── mini-project-week-5.md
├── source/
│   ├── app.py
│   ├── couriers.py
│   ├── demo.py
│   ├── my_mini_db.py
│   ├── orders.py
│   ├── products.py
│   ├── utilities.py
│   └── __pycache__/
├── LICENSE
├── README.md
├── requirements.txt
└── .env
```

## Getting Started

### Prerequisites
- Python 3.7+

### Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory:
	```powershell
	cd "Cafe CLI Application/Cafe App"
	```
3. (Optional) Create and activate a virtual environment:
	```powershell
	python -m venv venv
	.\venv\Scripts\activate
	```
4. Install required packages:
	```powershell
	pip install -r requirements.txt
	```

## How to Run the App

Run the main application from the `source` directory:

```powershell
python source/app.py
```

## Usage

When you start the app, you'll see a welcome message and a main menu:

```
╔═════════════════════════════════╗
║            Main Menu            ║
╠═════════════════════════════════╣
║  [0] Exit Application           ║
║  [1] Enter Product Menu         ║
║  [2] Enter Orders Menu          ║
║  [3] Enter Couriers Menu        ║
╚═════════════════════════════════╝
```

Select an option by entering the corresponding number. Each submenu allows you to manage products, orders, or couriers interactively.

## Data Files
- All data is stored in CSV files in the `data/` folder.
- No external database setup is required.

## License
This project is licensed under the terms of the LICENSE file.

## Author
YusufS-hub
