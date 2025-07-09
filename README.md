# Product Manager CLI

A Python-based command-line application for managing products. It allows users to add, remove, sort, search, and compare products with full input validation and timestamp logging. Product data is stored persistently in a local CSV file, making it lightweight and easy to use without any database setup.

---

## Features

- Add products with name, category, price, and timestamp
- Remove products by name (case-insensitive)
- Sort product list by category, price, name, or timestamp
- Search for specific product details by name
- Compare prices between any two products
- Clear all data in the CSV file with confirmation
- Fully object-oriented design using a custom `Items` class
- Uses only standard Python libraries (`csv`, `os`, `datetime`, `sys`)

---

## How to Use

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/marketplace_project.git
   cd marketplace_project


2. **Run the application in the terminal**
   ```bash
   python marketplace.py



Choose from options to add, remove, sort, find, compare, clear, or exit.

Requirements
Python 3.7 or higher

No external packages or dependencies

File Structure
marketplace_project/
├── marketplace.py      # Main CLI application
├── README.md           # Project documentation
└── marketplace.csv     # Auto-created CSV file storing product data


**Notes
The program automatically prevents duplicate product names.
Timestamp is automatically recorded at the moment of adding a product.
Sorting by timestamp uses actual time comparison, not string order.
CSV file is created if it doesn't exist when the program runs.
All operations are performed through a simple terminal interface.