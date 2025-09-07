
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
│   └── docker-compose.yml
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

### Loading Animation
The app uses a simple loading animation for a better user experience when performing actions:

```python
from utilities import loading_animation
loading_animation()  # Shows a brief loading spinner in the CLI
```
This function is called before displaying data or after certain actions to indicate progress.

## Data Files
- All data is stored in CSV files in the `data/` folder.
- No external database setup is required.

## Docker Support
This project includes a `docker-compose.yml` file (located in the `data/` folder) for containerized deployment or development. You can use Docker to run supporting services if needed (e.g., a database or other dependencies).

### How to Use Docker Compose
1. Make sure Docker is installed and running on your system.
2. From the project root, run:
	```powershell
	docker-compose -f data/docker-compose.yml up
	```
3. This will start all services defined in the compose file. Adjust the compose file as needed for your environment.

> Note: The CLI app itself is run with Python as described above. Docker Compose is optional and only needed if you want to use the services defined in `docker-compose.yml`.

## License
This project is licensed under the terms of the LICENSE file.

## Author
YusufS-hub
