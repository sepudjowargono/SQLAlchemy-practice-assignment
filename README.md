# 🛒 Shop Order Database (SQLAlchemy Assignment)

## 📌 Overview
This project demonstrates how to create and manage a relational database using **Python** and **SQLAlchemy** with **SQLite**.  

The application models a simple shop system with:
- Users
- Products
- Orders

It showcases:
- Database setup
- Table relationships
- CRUD operations (Create, Read, Update, Delete)
- Basic and advanced queries

---

## 🎯 Objectives
- Practice using SQLAlchemy ORM
- Understand relationships between tables
- Perform CRUD operations in a database
- Work with SQLite for local database storage

---

## 🧱 Database Structure

### 👤 Users
- `id` (Primary Key)
- `name`
- `email` (Unique)

### 📦 Products
- `id` (Primary Key)
- `name`
- `price`

### 🧾 Orders
- `id` (Primary Key)
- `user_id` (Foreign Key → Users)
- `product_id` (Foreign Key → Products)
- `quantity`
- `status` (Boolean: shipped or pending)

---

## 🔗 Relationships
- One **User** can have many **Orders**
- One **Product** can appear in many **Orders**
- Each **Order** belongs to one **User** and one **Product**

---

## ⚙️ Technologies Used
- Python
- SQLAlchemy (ORM)
- SQLite

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pythin install -r requirements.txt
```

---

## ▶️ Running the Project
Run the script:

```bash
python shop-order-database.py
```

---

## 🗄️ Database File
The SQLite database will be created automatically:

```bash
shop.db
```

---

## 🧪 How to Use
### Step 1: Populate Database
Run the script once to insert sample users, products, and orders
Comment out the insert section afterward to avoid duplicate entries

### Step 2: View Data
The script will print:
- All users
- All products
- All orders (with user + product details)

### Step 3: Test Updates
Uncomment the update section to:
- Modify a product price

### Step 4: Bonus Features
Uncomment the following sectons:
- View all pending (not shipped) orders
- Count number of orders per user

### Step 5: Test Deletion
Uncomment the delete section to:
- Remove a user by ID

```bash
🔍 Example Output
=== USERS ===
User: Alice
Email: alice@example.com

=== PRODUCTS ===
Product: Laptop
Price: $1000

=== ORDERS ===
User: Alice
Product: Laptop
Quantity: 1
Status: Pending
```

---

## ⚠️ Notes
Running the script multiple times may cause duplicate entry errors due to unique constraints (e.g., email)
To reset the database:
- Delete shop.db
- Or use:
```bash
Base.metadata.drop_all(engine)
```

---

## 📦 Requirements
Dependencies (from `requirements.txt`):

greenlet==3.3.2
<br>mysql-connector-python==9.6.0
<br>SQLAlchemy==2.0.48
<br>typing_extensions==4.15.0

---

## 👨‍💻 Author

Stephana Pudjowargono
