from sqlalchemy import create_engine, String, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, relationship
from typing import List

# Database connection
engine = create_engine('sqlite:///shop.db')

# Base class for ORM models
class Base(DeclarativeBase):
    pass

# Create session factory
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal() # Open a session to interact with the database

# Create 'User' table
class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    
    # Define relationship [one-to-many] with 'Orders'
    orders: Mapped[List['Order']] = relationship(back_populates="user", cascade="all, delete-orphan")
    
# Create 'Product' table
class Product(Base):
    __tablename__ =  'products'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    
    # Define relationship [one-to-many] with 'Orders'
    orders: Mapped[List['Order']] = relationship(back_populates="product", cascade="all, delete-orphan")
    
# Create 'Order' table
class Order(Base):
    __tablename__ = 'orders'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    status: Mapped[bool] = mapped_column(default=False) # True = shipped, False = pending
    
    # Define relationships with 'User' and 'Product'
    user: Mapped['User'] = relationship(back_populates="orders")
    product: Mapped['Product'] = relationship(back_populates="orders")
    
# Create tables in the database
Base.metadata.create_all(engine)

### -------------------------- ###
### |        STEP ONE        | ###
### -------------------------- ###
### RUN THE CODES BELOW FIRST TIME TO POPULATE THE DATABASE WITH SAMPLE DATA, THEN COMMENT THEM OUT TO AVOID DUPLICATION OF ENTRIES IN THE DATABASE. ###

# Create new users
user1 = User(name="Stephana Pudjowargono", email="sepudjowargono@gmail.com")
user2= User(name="Robin De Los Santos", email="robin.delossantos@hotmail.com")
session.add_all([user1, user2])
session.commit()

# Create new products
product1 = Product(name="Laptop", price=1000)
product2 = Product(name="Smartwatch", price=600)
product3 = Product(name="Headphones", price=200)
session.add_all([product1, product2, product3])
session.commit()

# Create new orders 
order1 = Order(user_id=1, product_id=1, quantity=1, status=False)
order2 = Order(user_id=1, product_id=3, quantity=2, status=False)
order3 = Order(user_id=2, product_id=2, quantity=1, status=True)
order4 = Order(user_id=2, product_id=3, quantity=3, status=True)
session.add_all([order1, order2, order3, order4])
session.commit()

# Query all users and print information
users = session.execute(select(User)).scalars().all()

print ("\n=== USERS ===\n")
for user in users:
    print(f"User: {user.name}\nEmail: {user.email}\n")
    
# Query all products and price information
products = session.execute(select(Product)).scalars().all()

print ("\n=== PRODUCTS ===\n")
for product in products:
    print(f"Product: {product.name}\nPrice: ${product.price}\n")
    
# Query all orders and print details
orders = session.execute(select(Order)).scalars().all()

print ("\n=== ORDERS ===\n")
for order in orders:
    print(f"Order ID: {order.id}\nUser: {order.user.name}\nProduct: {order.product.name}\nQuantity: {order.quantity}\nStatus: {'Shipped' if order.status else 'Pending'}\n")

### -------------------------- ###
### |        STEP TWO        | ###
### -------------------------- ###
### UNCOMMENT THE BELOW CODE (update product price) AND RUN SECOND TO TEST UPDATE THEM COMMENT IT OUT AFTERWARDS TO AVOID UNINTENDED CHANGES TO THE DATABASE. ###

# # Update a products price
# update_product = session.get(Product, 3) # Get the product with id 3 (Headphones)
# update_product.price = 250 # Update price
# session.commit() # Commit changes to the database
# print(f"The price of {update_product.name} has been updated to ${update_product.price}.")

### -------------------------- ###
### |      STEP FOUR         | ###
### -------------------------- ###
# ### UNCOMMENT THE BELOW CODE (delete user by ID) AND RUN FORTH TO TEST UPDATE. THEN COMMENT IT OUT AFTERWARDS TO AVOID UNINTENDED CHANGES TO THE DATABASE. ###    

# # Delete a user by ID
# delete_user = session.get(User, 1) # Get the user with id 1 (Stephana Pudjowargono)
# session.delete(delete_user)
# session.commit()
# print(f"User {delete_user.name} has been deleted from the database.")

### -------------------------- ###
### |      STEP THREE        | ###
### -------------------------- ###
# ### UNCOMMENT THE BELOW CODES (Query orders that are pending and Count number of orders) AND RUN THIRD TO TEST UPDATE. THEN COMMENT IT OUT AFTERWARDS TO AVOID UNINTENDED CHANGES TO THE DATABASE. ###   

# # Query all orders that are pending(status=False)
# pending_orders = session.execute(select(Order).where(Order.status == False)).scalars().all()
# print("\n=== PENDING ORDERS ===\n")
# for order in pending_orders:
#     print(f"Order ID: {order.id}\nUser: {order.user.name}\nProduct: {order.product.name}\nQuantity: {order.quantity}\n")
    
# # Count number of orders per user
# count_orders = session.query(User).all()
# print("\n=== NUMBER OF ORDERS PER USER ===\n")
# for user in count_orders:
#     print(f"User: {user.name}\nNumber of Orders: {len(user.orders)}\n")
    
session.close() # Close the session when done

### -------------------------- ###
### |      STEP FIVE         | ###
### -------------------------- ###
### UNCOMMENT THE BELOW CODE TO DROP ALL TABLES. THEN COMMENT IT OUT AFTERWARDS TO AVOID UNINTENDED CHANGES TO THE DATABASE. ###   

# Base.metadata.drop_all(engine) # Drop all tables in the database (optional, use with caution)