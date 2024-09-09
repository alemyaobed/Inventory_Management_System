from sqlalchemy.orm import Session
from app import models, schemas

# CRUD for Products

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(name=product.name, description=product.description, price=product.price, quantity=product.quantity)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product_update: schemas.ProductCreate):
    product = get_product(db, product_id)
    if product:
        product.name = product_update.name
        product.description = product_update.description
        product.price = product_update.price
        product.quantity = product_update.quantity
        db.commit()
        db.refresh(product)
        return product
    return None

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    if product:
        db.delete(product)
        db.commit()
        return product
    return None

# CRUD for Suppliers

def get_supplier(db: Session, supplier_id: int):
    return db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()

def get_suppliers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Supplier).offset(skip).limit(limit).all()

def create_supplier(db: Session, supplier: schemas.SupplierCreate):
    db_supplier = models.Supplier(name=supplier.name, contact_info=supplier.contact_info)
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

def update_supplier(db: Session, supplier_id: int, supplier_update: schemas.SupplierCreate):
    supplier = get_supplier(db, supplier_id)
    if supplier:
        supplier.name = supplier_update.name
        supplier.contact_info = supplier_update.contact_info
        db.commit()
        db.refresh(supplier)
        return supplier
    return None

def delete_supplier(db: Session, supplier_id: int):
    supplier = get_supplier(db, supplier_id)
    if supplier:
        db.delete(supplier)
        db.commit()
        return supplier
    return None

# CRUD for Orders

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Order).offset(skip).limit(limit).all()

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(product_id=order.product_id, supplier_id=order.supplier_id, quantity_ordered=order.quantity_ordered)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def update_order(db: Session, order_id: int, order_update: schemas.OrderCreate):
    order = get_order(db, order_id)
    if order:
        order.product_id = order_update.product_id
        order.supplier_id = order_update.supplier_id
        order.quantity_ordered = order_update.quantity_ordered
        db.commit()
        db.refresh(order)
        return order
    return None

def delete_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    if order:
        db.delete(order)
        db.commit()
        return order
    return None
